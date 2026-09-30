"""Spec-driven episode renderer (Ep 02A onward). Ep 01 keeps its own tools/render_ep01.sh.

Usage: python3 tools/render_episode.py <spec.json> <workdir>

The spec (see episodes/*/render_spec.json) describes:
  clips      [{file, in, dur, vf?}]       cut list in order; each trimmed to dur seconds (straight cuts)
  plate      {image, at, dissolve}        series end-card plate (golden mist); dissolves in at `at`
  runtime    total seconds (61-90)
  vo         [{file, at, gain_db?}]       narration files placed at absolute times
  captions   [{start, end, text}]         burned-in KJV captions ("line1 / line2")
  title      {text, start, end}           day title (optional)
  bed        {source, segments:[{at, src, dur, fin?, fout?}], tail_fade}   soundbed built from an approved bed
  watermark  {file, start, end}
  endcard    {file, start}
Outputs <workdir>/<spec name>_1080x1920.mp4 (master) and <spec name>_tiktok.mp4 (<= 29 MiB delivery).
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "assets", "fonts")
N = "scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1,format=yuv420p"

def run(args):
    print("+", " ".join(a if len(a) < 80 else a[:77] + "..." for a in args[:8]), "...")
    subprocess.run(args, check=True)  # raises on failure; do not pipe this script through tail

def ass_time(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"

def write_ass(spec, path):
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,EB Garamond SemiBold,62,&H00E4EDF2,&H00E4EDF2,&H70000000,&H80000000,0,0,0,0,100,100,0.5,0,1,3,2,2,90,90,580,1
Style: Title,EB Garamond SemiBold,66,&H00E4EDF2,&H00E4EDF2,&H80000000,&H90000000,0,0,0,0,100,100,14,0,1,2,2,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = [f"Dialogue: 0,{ass_time(c['start'])},{ass_time(c['end'])},Caption,,0,0,0,,{{\\blur6\\fad(150,150)}}"
          + c["text"].replace(" / ", "\\N") for c in spec["captions"]]
    if spec.get("title"):
        t = spec["title"]
        ev.append(f"Dialogue: 1,{ass_time(t['start'])},{ass_time(t['end'])},Title,,0,0,0,,{{\\pos(540,768)\\fad(500,400)\\blur5}}{t['text']}")
    open(path, "w").write(head + "\n".join(ev) + "\n")

def main(spec_path, wd):
    spec = json.load(open(spec_path))
    name = spec["name"]; R = spec["runtime"]
    os.chdir(wd)
    # 1. picture
    ins, fl = [], []
    for i, c in enumerate(spec["clips"]):
        ins += ["-i", c["file"]]
        extra = ("," + c["vf"]) if c.get("vf") else ""
        fl.append(f"[{i}:v]trim={c['in']}:{c['in'] + c['dur']},setpts=PTS-STARTPTS,{N}{extra}[c{i}]")
    k = len(spec["clips"])
    cat = "".join(f"[c{i}]" for i in range(k)) + f"concat=n={k}:v=1:a=0,settb=1/24[cut]"
    fl.append(cat)
    p = spec["plate"]
    ins += ["-loop", "1", "-t", str(R), "-i", p["image"]]
    fl.append(f"[{k}:v]{N},scale=w='trunc(1080*(1+0.04*t/{R})/2)*2':h=-2:eval=frame,crop=1080:1920,setsar=1,trim=0:{R - p['at'] + 1},setpts=PTS-STARTPTS,settb=1/24[pl]")
    fl.append(f"[cut][pl]xfade=transition=fade:duration={p['dissolve']}:offset={p['at']},noise=alls=5:allf=t,format=yuv420p[vout]")
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", ";".join(fl),
         "-map", "[vout]", "-t", str(R), "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-r", "24", "picture.mp4"])
    # 2. overlays + captions
    write_ass(spec, "captions.ass")
    wm, ec = spec["watermark"], spec["endcard"]
    fc = (f"[1:v]format=rgba,colorchannelmixer=aa=0.70,fade=t=in:st=0:d=0.3:alpha=1,"
          f"fade=t=out:st={wm['end'] - wm['start'] - 0.7}:d=0.7:alpha=1,setpts=PTS+{wm['start']}/TB[wm];"
          f"[2:v]format=rgba,fade=t=in:st=0:d=0.7:alpha=1,setpts=PTS+{ec['start']}/TB[ec];"
          f"[0:v][wm]overlay=0:0:eof_action=pass[a];[a][ec]overlay=0:0:eof_action=pass,"
          f"ass=captions.ass:fontsdir={FONTS},format=yuv420p[v]")
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", "picture.mp4",
         "-loop", "1", "-t", str(wm["end"] - wm["start"]), "-i", wm["file"],
         "-loop", "1", "-t", str(R - ec["start"] + 0.5), "-i", ec["file"],
         "-filter_complex", fc, "-map", "[v]", "-c:v", "libx264", "-preset", "slow", "-crf", "19",
         "-maxrate", "10M", "-bufsize", "20M", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", "24", "-t", str(R), "video.mp4"])
    # 3. sound
    b = spec["bed"]; ains = ["-i", b["source"]]; afl = []; parts = []
    segs = b["segments"]
    afl.append(f"[0:a]aformat=sample_rates=44100:channel_layouts=stereo,asplit={len(segs)}" + "".join(f"[b{i}]" for i in range(len(segs))))
    for i, s in enumerate(segs):
        fin, fout = s.get("fin", 0.75), s.get("fout", 0.75)
        d = int(s["at"] * 1000)
        afl.append(f"[b{i}]atrim={s['src']}:{s['src'] + s['dur']},asetpts=PTS-STARTPTS,afade=t=in:d={fin},"
                   f"afade=t=out:st={s['dur'] - fout}:d={fout},adelay={d}|{d}[s{i}]")
        parts.append(f"[s{i}]")
    afl.append("".join(parts) + f"amix=inputs={len(parts)}:normalize=0,apad=whole_dur={R},atrim=0:{R},"
               f"afade=t=out:st={R - b.get('tail_fade', 3.0)}:d={b.get('tail_fade', 3.0)}[bed]")
    vparts = []
    for j, v in enumerate(spec["vo"], 1):
        ains += ["-i", v["file"]]; d = int(v["at"] * 1000)
        afl.append(f"[{j}:a]aformat=sample_rates=44100:channel_layouts=stereo,volume={v.get('gain_db', 0)}dB,adelay={d}|{d}[v{j}]")
        vparts.append(f"[v{j}]")
    afl.append("".join(vparts) + f"amix=inputs={len(vparts)}:normalize=0,apad=whole_dur={R},atrim=0:{R},asplit[vo][key]")
    afl.append("[bed][key]sidechaincompress=threshold=0.04:ratio=3:attack=30:release=450:makeup=1[duck]")
    afl.append("[duck][vo]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *ains, "-filter_complex", ";".join(afl),
         "-map", "[aout]", "-c:a", "pcm_s16le", "-t", str(R), "mix.wav"])
    # 4. mux master + delivery encode
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", "video.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", "-shortest", f"{name}_1080x1920.mp4"])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", "video.mp4", "-c:v", "libx264", "-preset", "slow",
         "-b:v", "3400k", "-pass", "1", "-passlogfile", "p2", "-an", "-f", "null", "/dev/null"])
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", "video.mp4", "-i", "mix.wav", "-map", "0:v", "-map", "1:a",
         "-c:v", "libx264", "-preset", "slow", "-b:v", "3400k", "-maxrate", "5000k", "-bufsize", "7000k", "-pass", "2",
         "-passlogfile", "p2", "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", "-t", str(R), f"{name}_tiktok.mp4"])
    print("done:", os.path.abspath(f"{name}_tiktok.mp4"))

if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]), sys.argv[2])
