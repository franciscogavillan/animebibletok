"""Build and verify the KJV script, caption table and SRT for each episode.

Usage:
  python3 tools/tracks.py            # verify all cue sheets, print runtime table
  python3 tools/tracks.py --write    # also fill episode markdown markers and write SRT files

Checks (Phase 3 review, automated part):
  * cue text, concatenated, equals the narrated KJV verses exactly (range minus OMIT list)
  * caption lines <= 34 characters, max 2 lines
  * runtime between 61 and 90 seconds (TikTok monetization window)
  * every "> " quoted line in an episode's FULL SCRIPT is a substring of the KJV passage
"""
import json, os, re, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cues_arc01 as C

KJV = json.load(open(os.path.join(ROOT, "scripture", "genesis_kjv.json")))["verses"]
KEYS = list(KJV)
SPK = {"NARRATOR": "NARRATOR", "GOD": "GOD", "ADAM": "ADAM", "EVE": "EVE", "SERPENT": "SERPENT"}

def verses(rng):
    a, b = rng.split("-")
    return KEYS[KEYS.index(a):KEYS.index(b) + 1]

def norm(t):
    return re.sub(r"\s+", " ", t.replace(" / ", " ")).strip()

def ts(t, srt=False):
    m, s = divmod(t, 60)
    if srt:
        ms = int(round((s - int(s)) * 1000))
        return f"00:{int(m):02d}:{int(s):02d},{ms:03d}"
    return f"{int(m)}:{s:04.1f}"

def build(ep):
    rng, cues = C.EP[ep]
    omit = C.OMIT.get(ep, [])
    vs = [v for v in verses(rng) if v not in omit]
    # timing
    t, timed = 0.0, []
    for gap, sp, txt in cues:
        w = len(norm(txt).split())
        start = t + gap
        end = start + max(1.2, w / C.RATE[sp] + 0.25)
        timed.append(dict(start=start, end=end, sp=sp, txt=txt, words=w))
        t = end
    runtime = t + C.TAILS.get(ep, C.TAIL)
    errors = []
    narrated = " ".join(KJV[v] for v in vs)
    spoken = " ".join(norm(c["txt"]) for c in timed)
    if norm(narrated) != norm(spoken):
        a, b = norm(narrated), norm(spoken)
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        errors.append(f"KJV mismatch at char {i}: KJV='...{a[max(0,i-30):i+30]}' CUES='...{b[max(0,i-30):i+30]}'")
    # assign verse numbers to cues by walking the text
    pos, bounds = 0, []
    for v in vs:
        bounds.append((pos, pos + len(KJV[v]), v)); pos += len(KJV[v]) + 1
    pos = 0
    for c in timed:
        n = norm(c["txt"])
        c["verse"] = next((v for s, e, v in bounds if s <= pos < e), "?")
        pos += len(n) + 1
        for line in c["txt"].split(" / "):
            if len(line) > 34:
                errors.append(f"caption line too long ({len(line)}): {line}")
        if len(c["txt"].split(" / ")) > 2:
            errors.append(f"more than 2 caption lines: {c['txt']}")
    if not (61 <= runtime <= 90):
        errors.append(f"runtime {runtime:.1f}s outside 61-90s")
    return dict(ep=ep, rng=rng, omit=omit, verses=vs, cues=timed, runtime=runtime, errors=errors,
                words=sum(c["words"] for c in timed))

def md_captions(b):
    rows = ["| # | In | Out | Voice | Caption |", "|---|---|---|---|---|"]
    for i, c in enumerate(b["cues"], 1):
        rows.append(f"| {i} | {ts(c['start'])} | {ts(c['end'])} | {c['sp']} | {c['txt']} |")
    return "\n".join(rows)

def md_script(b):
    out, last = [], None
    for c in b["cues"]:
        key = (c["sp"], c["verse"])
        if key != last:
            if out:
                out.append(">")
            ref = f" (Genesis {c['verse']})" if (last is None or c["verse"] != last[1]) else ""
            out.append(f"> **{SPK[c['sp']]} — KJV**{ref}  ")
            out.append("> " + norm(c["txt"]))
            last = key
        else:
            out[-1] += " " + norm(c["txt"])
    return "\n".join(out) + "\n\n**Adaptation lines:** none. Every spoken word in this episode is KJV."

def md_passage(b):
    out = []
    for v in verses(b["rng"]):
        mark = " *(not narrated; retained here and in the long-form cut)*" if v in b["omit"] else ""
        out.append(f"**{v}** {KJV[v]}{mark}  ")
    return "\n".join(out)

def srt(b):
    out = []
    for i, c in enumerate(b["cues"], 1):
        out += [str(i), f"{ts(c['start'], True)} --> {ts(c['end'], True)}", *c["txt"].split(" / "), ""]
    return "\n".join(out)

def fill(path, tag, body):
    s = open(path).read()
    pat = re.compile(rf"(<!-- BEGIN:{tag} -->\n).*?(<!-- END:{tag} -->)", re.S)
    if not pat.search(s):
        return False
    s = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), s)
    open(path, "w").write(s)
    return True

def quoted_lines_ok(path, b):
    s = open(path).read()
    m = re.search(r"<!-- BEGIN:SCRIPT -->(.*?)<!-- END:SCRIPT -->", s, re.S)
    if not m:
        return []
    passage = norm(" ".join(KJV[v] for v in verses(b["rng"])))
    bad = []
    for line in m.group(1).splitlines():
        line = line[1:].strip() if line.startswith(">") else ""
        if not line or line.startswith("**"):
            continue
        if norm(line) not in passage:
            bad.append(line)
    return bad

def main():
    write = "--write" in sys.argv
    ok = True
    print(f"{'EP':5} {'SOURCE':11} {'WORDS':>5} {'RUNTIME':>8}  OMITTED")
    for ep in C.EP:
        b = build(ep)
        print(f"{ep:5} {b['rng']:11} {b['words']:5d} {b['runtime']:7.1f}s  {','.join(b['omit']) or '-'}")
        files = glob.glob(os.path.join(ROOT, "episodes", f"ep{ep.lower()}-*", "*.md"))
        pkg = [f for f in files if os.path.basename(f).startswith("genesis_")]
        if write and pkg:
            d = os.path.dirname(pkg[0])
            fill(pkg[0], "CAPTIONS", md_captions(b))
            fill(pkg[0], "SCRIPT", md_script(b))
            fill(pkg[0], "PASSAGE", md_passage(b))
            open(os.path.join(d, f"ep{ep.lower()}_captions_planned.srt"), "w").write(srt(b))
        if pkg:
            b["errors"] += [f"script line not KJV: {l}" for l in quoted_lines_ok(pkg[0], b)]
        for e in b["errors"]:
            ok = False
            print("   ERROR:", e)
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
