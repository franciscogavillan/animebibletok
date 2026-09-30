#!/usr/bin/env bash
# Render GENESIS Episode 01 "In the Beginning" (64 s, 1080x1920, 24 fps) from the
# approved Higgsfield clips, narration, soundbed, overlays and burned-in KJV captions.
#
# Usage: tools/render_ep01.sh <workdir>
#   <workdir> must contain: soundbed.wav wm_text.png wm_full.png endcard.png captions.ass
#   Clips and narration are fetched from Higgsfield's CDN unless already in <workdir>/clips, <workdir>/vo.
#   Font: EB Garamond SemiBold is fetched into <workdir>/fonts if missing.
# Output: <workdir>/genesis_ep01_in_the_beginning_1080x1920.mp4
set -euo pipefail
W=${1:?workdir}; cd "$W"; mkdir -p clips vo fonts
CDN=https://d8j0ntlcm91z4.cloudfront.net/user_3K1RFC9aMzk3kgUUAeEoHwAE2Q4
fetch(){ [ -s "$1" ] || curl -fsS --retry 3 -o "$1" "$CDN/$2"; }
# --- shots (Higgsfield Kling 3.0 pro, v1.2 style lock) ---
fetch clips/S01.mp4  hf_20260930_014513_adc5764d-e66a-40a3-a316-2f52ac4551a4.mp4   # darkness, tilt down
fetch clips/S02.mp4  hf_20260930_014513_abc2d04f-d5a7-4ac6-b11d-1e04d88f105f.mp4   # the Deep
fetch clips/S03.mp4  hf_20260930_014513_8dcdba33-9b43-48c7-a0b3-e8b8841b8e29.mp4   # the Spirit's path
fetch clips/S04a.mp4 hf_20260930_014527_e2a92a6b-1824-49ca-b0af-94eaf19be109.mp4   # silence + tremor
fetch clips/S04b.mp4 hf_20260930_014527_a93b0f4c-5c6c-4030-9ac5-b4d4d0d218d5.mp4   # light arrives
fetch clips/S05.mp4  hf_20260930_014527_5c054d08-d04e-4e32-896f-15ddc96d1891.mp4   # that it was good
fetch clips/S06.mp4  hf_20260930_014545_09d74d81-ad27-45ae-9a4b-f51511d7abf1.mp4   # division
fetch clips/S07.mp4  hf_20260930_014545_29595b90-0fe9-4ff6-bc19-5d6678195a08.mp4   # Day / Night
fetch clips/S08.mp4  hf_20260930_014545_261a91a0-537f-4382-a8b7-258a6e3196a2.mp4   # evening & morning
fetch clips/S09.mp4  hf_20260930_014545_57496f81-9cdd-4786-af4e-863a210c8665.mp4   # undivided waters
# --- narration: NARRATOR = Arthur (ElevenLabs), GOD = Desmond (Seed Audio) ---
fetch vo/n01.mp3 hf_20260930_011402_0179e722-f5eb-4182-8bc4-2ffc7b18fc2a.mp3
fetch vo/n02.mp3 hf_20260930_011415_c92c45af-eed6-44cf-a0fe-43a5dae5fa63.mp3
fetch vo/n03.mp3 hf_20260930_011414_89a172c0-fe4e-479c-a4a7-fabf48d7bd6d.mp3
fetch vo/n04.mp3 hf_20260930_011421_0e19bed4-6099-464f-80a4-a843b115b712.mp3
fetch vo/g01.wav hf_20260930_011230_2afb9e8a-375e-4689-b167-7976a13a8a7a.wav
fetch vo/n05.mp3 hf_20260930_011421_f48cad42-9d76-4d9e-97bc-61c871b28adf.mp3
fetch vo/n06.mp3 hf_20260930_011427_4e68338e-7c8c-4359-88e4-503b1fa4b519.mp3
fetch vo/n07.mp3 hf_20260930_011428_c694def6-14d0-4ba7-9f88-1ff461f5969c.mp3
fetch vo/n08.mp3 hf_20260930_011434_10106a0e-db6e-49a7-8e12-4b814ac33c63.mp3
fetch vo/n09.mp3 hf_20260930_011434_b9d5b0db-b9b9-439f-8d93-a5016fad5e0b.mp3
[ -s fonts/EBGaramond-SemiBold.ttf ] || curl -fsSL -o fonts/EBGaramond-SemiBold.ttf \
  https://github.com/google/fonts/raw/main/ofl/ebgaramond/static/EBGaramond-SemiBold.ttf || true

# --- 1. picture: normalize, cut to the edit, extend S09 to 7 s ---
# S03 is graded down to match the near-black S01/S02/S04a (mean luma ~92 -> ~38): before 1:3 the world stays dark.
N="scale=1080:-2:flags=lanczos,crop=1080:1920,fps=24,setsar=1,format=yuv420p"
ffmpeg -hide_banner -loglevel error -y \
  -i clips/S01.mp4 -i clips/S02.mp4 -i clips/S03.mp4 -i clips/S04a.mp4 -i clips/S04b.mp4 \
  -i clips/S05.mp4 -i clips/S06.mp4 -i clips/S07.mp4 -i clips/S08.mp4 -i clips/S09.mp4 \
  -filter_complex "
  [0:v]trim=0:6,setpts=PTS-STARTPTS,$N[v1]; [1:v]trim=0:8,setpts=PTS-STARTPTS,$N[v2];
  [2:v]trim=0:8,setpts=PTS-STARTPTS,$N,lutyuv=y='(val-16)*0.40+16':u='(val-128)*0.8+128':v='(val-128)*0.8+128'[v3]; [3:v]trim=0:5,setpts=PTS-STARTPTS,$N[v4];
  [4:v]trim=0:3,setpts=PTS-STARTPTS,$N[v5]; [5:v]trim=0:7,setpts=PTS-STARTPTS,$N[v6];
  [6:v]trim=0:6,setpts=PTS-STARTPTS,$N[v7]; [7:v]trim=0:7,setpts=PTS-STARTPTS,$N[v8];
  [8:v]trim=0:7,setpts=PTS-STARTPTS,$N[v9];
  [9:v]trim=0:3,setpts=PTS-STARTPTS,$N,tpad=stop_mode=clone:stop_duration=4,
       scale=w='trunc(1080*(1+0.05*t/7)/2)*2':h=-2:eval=frame:flags=bicubic,crop=1080:1920,setsar=1[v10];
  [v1][v2][v3][v4][v5][v6][v7][v8][v9][v10]concat=n=10:v=1:a=0,
  noise=alls=5:allf=t,format=yuv420p[vout]" \
  -map "[vout]" -c:v libx264 -preset fast -crf 16 -maxrate 40M -bufsize 80M -r 24 picture.mp4

# --- 2. overlays + captions ---
ffmpeg -hide_banner -loglevel error -y -i picture.mp4 \
  -loop 1 -t 28.5 -i wm_text.png -loop 1 -t 33 -i wm_full.png -loop 1 -t 5 -i endcard.png \
  -filter_complex "
  [1:v]format=rgba,colorchannelmixer=aa=0.65,fade=t=out:st=27.5:d=0.6:alpha=1[wt];
  [2:v]format=rgba,colorchannelmixer=aa=0.70,fade=t=in:st=0:d=0.5:alpha=1,fade=t=out:st=31.8:d=0.7:alpha=1,setpts=PTS+27.5/TB[wf];
  [3:v]format=rgba,fade=t=in:st=0:d=0.7:alpha=1,setpts=PTS+59.3/TB[ec];
  [0:v][wt]overlay=0:0:eof_action=pass[a];
  [a][wf]overlay=0:0:eof_action=pass[b];
  [b][ec]overlay=0:0:eof_action=pass,ass=captions.ass:fontsdir=fonts,format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -preset slow -crf 19 -maxrate 10M -bufsize 20M -profile:v high -pix_fmt yuv420p -r 24 -t 64 video.mp4

# --- 3. sound: soundbed extended to 64 s + narration placed on the caption timings ---
# GOD line: close the 0.85 s gap inside "Let there be ... light" to about 0.35 s; lift 7 dB to match the narrator.
ffmpeg -hide_banner -loglevel error -y -i soundbed.wav -i vo/n01.mp3 -i vo/n02.mp3 -i vo/n03.mp3 -i vo/n04.mp3 \
  -i vo/g01.wav -i vo/n05.mp3 -i vo/n06.mp3 -i vo/n07.mp3 -i vo/n08.mp3 -i vo/n09.mp3 \
  -filter_complex "
  [0:a]asplit[s1][s2];
  [s1]atrim=0:58.5,asetpts=PTS-STARTPTS[bedA];
  [s2]atrim=56.5:60,asetpts=PTS-STARTPTS,atempo=0.5[bedB];
  [bedA][bedB]acrossfade=d=1.5:c1=tri:c2=tri,afade=t=out:st=60.5:d=3.5,apad=whole_dur=64,atrim=0:64[bed];
  [5:a]aformat=sample_rates=44100:channel_layouts=stereo,asplit[g1][g2];
  [g1]atrim=0:1.30,asetpts=PTS-STARTPTS[ga]; [g2]atrim=1.80:3.2,asetpts=PTS-STARTPTS[gb];
  [ga][gb]concat=n=2:v=0:a=1,volume=7dB[god];
  [1:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=400|400[n1];
  [2:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=6400|6400[n2];
  [3:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=14400|14400[n3];
  [4:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=24420|24420[n4];
  [god]adelay=25600|25600[g];
  [6:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=28000|28000[n5];
  [7:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=31000|31000[n6];
  [8:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=37400|37400[n7];
  [9:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=43400|43400[n8];
  [10:a]aformat=sample_rates=44100:channel_layouts=stereo,adelay=50400|50400[n9];
  [n1][n2][n3][n4][g][n5][n6][n7][n8][n9]amix=inputs=10:normalize=0,apad=whole_dur=64,atrim=0:64,asplit[vo][key];
  [bed]aformat=sample_rates=44100:channel_layouts=stereo[bed2];
  [bed2][key]sidechaincompress=threshold=0.04:ratio=3:attack=30:release=450:makeup=1[duck];
  [duck][vo]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]" \
  -map "[aout]" -c:a pcm_s16le -t 64 mix.wav

# --- 4. mux ---
ffmpeg -hide_banner -loglevel error -y -i video.mp4 -i mix.wav -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 256k -movflags +faststart -shortest genesis_ep01_in_the_beginning_1080x1920.mp4
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height,r_frame_rate -of compact genesis_ep01_in_the_beginning_1080x1920.mp4
