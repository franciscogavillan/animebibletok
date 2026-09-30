"""Generate per-episode posting kits (TikTok, YouTube Shorts, Instagram Reels, Facebook Reels).

Usage:  python3 tools/posting_kits.py
Output: marketing/posting_kits/epXX.md (one per episode) + marketing/posting_kits/README.md

Rules baked in (see marketing/tiktok_launch_playbook.md):
  * TikTok: 5-7 hashtags; hook = verbatim KJV line; one genuine question; "Next" line.
  * YouTube Shorts: keyword-first title <= 100 chars; full KJV passage in the description; 3 hashtags.
  * Instagram Reels: hard limit of 5 hashtags (enforced by Instagram since Dec 2025).
  * Facebook Reels: 3 hashtags, conversational.
  * Every hook line is checked to be an exact substring of the KJV passage.
To add an episode, append a dict to EPISODES and re-run.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KJV = json.load(open(os.path.join(ROOT, "scripture", "genesis_kjv.json")))["verses"]
KEYS = list(KJV)
OUT = os.path.join(ROOT, "marketing", "posting_kits")

# ep, label, title, range (first-last verse), hook (verbatim KJV), question, tags (episode-specific, no #),
# yt_keywords (extra YouTube tag keywords), cover text
EPISODES = [
    dict(ep="01", label="1", title="In the Beginning", rng="1:1-1:5",
         hook="In the beginning God created the heaven and the earth.",
         q="What moment in Genesis are you most excited to see animated?",
         tags=["creation", "inthebeginning"], yt=["creation story", "in the beginning", "genesis 1", "let there be light"]),
    dict(ep="02A", label="2A", title="The Heavens", rng="1:6-1:8",
         hook="And God called the firmament Heaven.",
         q="Which day of creation do you most want to see next?",
         tags=["creation", "firmament"], yt=["creation story", "genesis 1", "firmament", "second day of creation"]),
    dict(ep="02B", label="2B", title="The Dry Land", rng="1:9-1:13",
         hook="And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.",
         q="Where is the place in God's creation that takes your breath away?",
         tags=["creation", "nature"], yt=["creation story", "genesis 1", "third day of creation", "dry land"]),
    dict(ep="03A", label="3A", title="Signs and Seasons", rng="1:14-1:19",
         hook="And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.",
         q="Sunrise or a sky full of stars: which one makes you think of God more?",
         tags=["creation", "stars"], yt=["creation story", "genesis 1", "fourth day of creation", "sun moon and stars"]),
    dict(ep="03B", label="3B", title="The Living World", rng="1:20-1:25",
         hook="And God created great whales,",
         q="Which animal do you think shows God's creativity best?",
         tags=["creation", "animals"], yt=["creation story", "genesis 1", "fifth day of creation", "great whales"]),
    dict(ep="04A", label="4A", title="In His Image", rng="1:26-1:28",
         hook="So God created man in his own image, in the image of God created he him; male and female created he them.",
         q="What does \"in his own image\" mean to you?",
         tags=["imageofgod", "adamandeve"], yt=["image of god", "genesis 1 26", "creation of man", "adam and eve"]),
    dict(ep="04B", label="4B", title="Very Good", rng="1:29-1:31",
         hook="And God saw every thing that he had made, and, behold, it was very good.",
         q="What's one thing in creation you're thankful for today?",
         tags=["creation", "verygood"], yt=["creation story", "genesis 1 31", "sixth day of creation", "it was very good"]),
    dict(ep="05", label="5", title="The Seventh Day", rng="2:1-2:3",
         hook="And on the seventh day God ended his work which he had made; and he rested on the seventh day from all his work which he had made.",
         q="How do you keep a day of rest?",
         tags=["sabbath", "rest"], yt=["seventh day", "sabbath", "genesis 2", "god rested"]),
    dict(ep="06A", label="6A", title="A Living Soul", rng="2:4-2:7",
         hook="And the LORD God formed man of the dust of the ground, and breathed into his nostrils the breath of life; and man became a living soul.",
         q="What stands out to you more: the dust, or the breath?",
         tags=["adam", "breathoflife"], yt=["creation of adam", "genesis 2 7", "breath of life", "dust of the ground"]),
    dict(ep="06B", label="6B", title="The Garden", rng="2:8-2:15",
         hook="And the LORD God planted a garden eastward in Eden; and there he put the man whom he had formed.",
         q="What do you imagine Eden looked like?",
         tags=["gardenofeden", "eden"], yt=["garden of eden", "genesis 2", "tree of life", "tree of knowledge"]),
    dict(ep="07A", label="7A", title="The Command", rng="2:16-2:20",
         hook="But of the tree of the knowledge of good and evil, thou shalt not eat of it: for in the day that thou eatest thereof thou shalt surely die.",
         q="Why do you think God gave Adam a choice?",
         tags=["gardenofeden", "treeofknowledge"], yt=["tree of knowledge of good and evil", "genesis 2 17", "adam names the animals"]),
    dict(ep="07B", label="7B", title="The Woman", rng="2:21-2:25",
         hook="This is now bone of my bones, and flesh of my flesh:",
         q="Tag the person who is your \"bone of my bones.\"",
         tags=["adamandeve", "marriage"], yt=["creation of eve", "genesis 2 23", "bone of my bones", "adam and eve"]),
    dict(ep="08", label="8", title="The Serpent", rng="3:1-3:5",
         hook="Now the serpent was more subtil than any beast of the field which the LORD God had made.",
         q="What do you notice about how the serpent twists God's words?",
         tags=["theserpent", "gardenofeden"], yt=["the serpent", "genesis 3", "garden of eden", "ye shall not surely die"]),
    dict(ep="09A", label="9A", title="The Fall", rng="3:6-3:8",
         hook="she took of the fruit thereof, and did eat, and gave also unto her husband with her; and he did eat.",
         q="Why do you think they hid?",
         tags=["thefall", "adamandeve"], yt=["the fall of man", "genesis 3 6", "forbidden fruit", "adam and eve"]),
    dict(ep="09B", label="9B", title="Where Art Thou?", rng="3:9-3:13",
         hook="And the LORD God called unto Adam, and said unto him, Where art thou?",
         q="If God asked you \"Where art thou?\" today, what would you answer?",
         tags=["thefall", "adamandeve"], yt=["where art thou", "genesis 3 9", "the fall of man", "adam and eve"]),
    dict(ep="10A", label="10A", title="Enmity", rng="3:14-3:16",
         hook="And I will put enmity between thee and the woman, and between thy seed and her seed; it shall bruise thy head, and thou shalt bruise his heel.",
         q="Genesis 3:15 is one of the most discussed verses in the Bible. What do you see in it?",
         tags=["genesis315", "theserpent"], yt=["genesis 3 15", "enmity", "the serpent cursed", "protoevangelium"]),
    dict(ep="10B", label="10B", title="Dust Thou Art", rng="3:17-3:20",
         hook="for dust thou art, and unto dust shalt thou return.",
         q="Why do you think Adam named her Eve right after this?",
         tags=["adamandeve", "eve"], yt=["dust thou art", "genesis 3 19", "mother of all living", "adam names eve"]),
    dict(ep="10C", label="10C", title="Exile From Eden", rng="3:21-3:24",
         hook="So he drove out the man; and he placed at the east of the garden of Eden Cherubims, and a flaming sword which turned every way, to keep the way of the tree of life.",
         q="That's the end of Arc I. Which moment hit you hardest?",
         tags=["gardenofeden", "cherubim"], yt=["expelled from eden", "genesis 3 24", "cherubim flaming sword", "tree of life"]),
]
NEXT_AFTER_ARC = "Two Brothers"

def verses(rng):
    a, b = rng.split("-")
    return KEYS[KEYS.index(a):KEYS.index(b) + 1]

def ref(rng):
    a, b = rng.split("-")
    ca, va = a.split(":"); cb, vb = b.split(":")
    return f"Genesis {ca}:{va}–{vb}" if ca == cb else f"Genesis {a}–{b}"

def kit(e, nxt):
    vs = verses(e["rng"])
    passage = " ".join(KJV[v] for v in vs)
    assert e["hook"] in passage, f"hook not verbatim KJV in {e['ep']}"
    R = ref(e["rng"])
    ch = e["rng"].split(":")[0]
    tt_tags = " ".join("#" + t for t in ["genesis", "bible", "anime", "kjv"] + e["tags"] + ["animebibletok"])
    ig_tags = " ".join("#" + t for t in ["animebibletok", "genesis", "bible", "anime", e["tags"][0]])
    fb_tags = "#Genesis #Bible #Anime"
    yt_title = f"{e['title']} | {R.replace('–', '-')} KJV | Bible Anime Ep {e['label']}"
    assert len(yt_title) <= 100, yt_title
    yt_tags = ", ".join(dict.fromkeys(
        ["genesis", "bible", "kjv", "king james bible", "bible anime", "anime", "bible story",
         f"genesis {ch}", R.lower().replace("–", "-"), "animebibletok"] + e["yt"]))
    verse_lines = "\n".join(f"{v} {KJV[v]}" for v in vs)
    cover = f"GENESIS · EP {e['label']}\n{e['title'].upper()}"
    return f"""# Posting kit — Genesis Episode {e['label']}: {e['title'].upper()}

**Source:** {R} (KJV) · **Next:** {nxt} · **Cover text:** `GENESIS · EP {e['label']}` / `{e['title'].upper()}`

Before posting on any platform, **switch on the AI-content disclosure**: TikTok "AI-generated content", YouTube "Altered or synthetic content" (disclose if unsure), Instagram/Facebook "AI info".

---

## TikTok
```
{e['hook']}
{R} (KJV) · Episode {e['label']} of the Book of Genesis as an anime, every word from the King James Bible.
{e['q']}
Next: {nxt} — follow so you don't miss it.
{tt_tags}
```
- **Pinned comment:** `Every spoken word in this series is from the King James Bible. Full series in order: see the "GENESIS — The Anime" playlist on our profile.`
- **Playlist:** add to `GENESIS — The Anime (in order)`
- **Sound name:** `{R} (KJV) · AnimeBibleTok`

## YouTube Shorts
**Title** ({len(yt_title)}/100)
```
{yt_title}
```
**Description**
```
{e['hook']}

{R} (KJV) — Episode {e['label']} of GENESIS, the Book of Genesis as an anime. Every spoken word is from the King James Bible.

📖 {R} (KJV)
{verse_lines}

▶ Watch the whole series in order: [playlist link]
Next episode: {nxt}

#genesis #bible #anime
```
**Tags**
```
{yt_tags}
```
- **Related video:** link the current arc compilation once it exists.
- **Pinned comment:** `Every word is from the King James Bible. Series in order: [playlist link]`

## Instagram Reels (max 5 hashtags)
```
{e['hook']}
{R} (KJV) · Episode {e['label']} of the Book of Genesis as an anime.
{e['q']}
Next: {nxt} — follow @animebibletok
{ig_tags}
```

## Facebook Reels
```
{e['hook']}

Genesis Episode {e['label']}: {e['title']} ({R}, KJV). The Book of Genesis as an anime, every word from the King James Bible.
{e['q']}
{fb_tags}
```
"""

def main():
    os.makedirs(OUT, exist_ok=True)
    rows = ["# Posting kits", "",
            "One file per episode with ready-to-paste captions, titles, descriptions and tags for TikTok, YouTube Shorts, Instagram Reels and Facebook Reels. Generated by `tools/posting_kits.py`; edit the episode table there and re-run.", "",
            "| Ep | Title | Source | Kit |", "|---|---|---|---|"]
    for i, e in enumerate(EPISODES):
        nxt = EPISODES[i + 1]["title"] if i + 1 < len(EPISODES) else NEXT_AFTER_ARC
        open(os.path.join(OUT, f"ep{e['ep'].lower()}.md"), "w").write(kit(e, nxt))
        rows.append(f"| {e['label']} | {e['title']} | {ref(e['rng'])} | [ep{e['ep'].lower()}.md](ep{e['ep'].lower()}.md) |")
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(rows) + "\n")
    print(f"wrote {len(EPISODES)} kits to {OUT}")

if __name__ == "__main__":
    main()
