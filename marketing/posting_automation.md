# Automating posting — TikTok, YouTube Shorts, Instagram Reels, Facebook Reels

*Researched September 2026. API terms change; confirm each platform's current developer docs before building.*

## What is already automated
For every episode the repo produces, without manual work:
- the finished video (`*_tiktok.mp4`, ≤ 29 MiB, 1080×1920) via `tools/render_episode.py`
- the cover image
- ready-to-paste text for every platform in `marketing/posting_kits/epXX.md` (`tools/posting_kits.py`)

What remains is the **upload + schedule** step. There are three ways to automate it.

---

## Option A — Scheduler app (recommended now)
Upload each episode once, paste the per-platform text from its posting kit, and schedule all four platforms at once.

| Tool | Notes |
|---|---|
| **Metricool** | Cheapest; has a free tier; TikTok, YouTube, Instagram, Facebook |
| **Buffer** | Simple "one video → Reels/Shorts/TikTok" workflow |
| **ShortSync** | Video-first; per-platform captions; direct Reels publishing |
| Publer, Planable, Sendible, Hootsuite | Also support all four |

**Why this first:** schedulers are already approved partners of each platform, so posts go **public** immediately. Building your own API integration means passing TikTok's and Google's app audits first (see Option B).

**Setup (one time):**
1. Connect TikTok, the YouTube channel, the Instagram Business/Creator account (linked to a Facebook Page) and the Facebook Page.
2. Create a queue with fixed slots, e.g. daily 7:30 pm in your main time zone (see the playbook's cadence).
3. For each episode, upload `*_tiktok.mp4` and the cover, then paste the four captions from the posting kit.
4. **Check that the tool can set each platform's AI disclosure.** If it can't for a platform, post that one natively or toggle the label after posting. Never skip it.

**Weekly routine (about 20 minutes):** upload the week's episodes into the queue, one post per slot.

---

## Option B — Your own API pipeline (full automation, more setup)
I can build `tools/publish.py` to read each episode's video and posting kit and post to all four platforms, run on a schedule. What each platform requires:

| Platform | API | AI disclosure field | Gate you must pass |
|---|---|---|---|
| **YouTube** | Data API v3 `videos.insert` (`publishAt` for scheduling) | `status.containsSyntheticMedia = true` | Google Cloud project + OAuth. **Uploads from unverified projects are locked to private** until the project passes Google's API audit. `videos.insert` now has its own quota bucket (100 calls/day default), which is plenty. |
| **TikTok** | Content Posting API → Direct Post | `is_aigc = true` (adds the "Creator labeled as AI-generated" tag) | TikTok developer app. **Unaudited apps can only post privately (SELF_ONLY)**; public posting requires passing TikTok's audit. |
| **Instagram** | Graph API content publishing (Reels container → publish) | None in the API (add the "AI info" label in-app) | Business/Creator account linked to a Facebook Page + Meta app. Reels via the API are capped at **90 s** (our episodes are 61–90 s ✓); 100 API posts per 24 h. |
| **Facebook** | Pages Reels publishing API | As for Instagram | Same Meta app/Page |

**How it would run:** credentials go in this environment's secrets. A scheduled Routine (e.g. daily 7:15 pm) picks the next unposted episode, posts it everywhere, records the post IDs in `marketing/published.json`, and pins the comment where the API allows.

**Realistic timeline:** YouTube and Meta can be working in days. TikTok public posting depends on audit approval, which takes weeks and isn't guaranteed. Until then, TikTok uploads can go in as drafts or private posts that you publish in the app.

---

## Option C — Hybrid (best balance right now)
- **Production is automated here:** render, posting kits, cover, delivery file.
- **Scheduling uses a scheduler (Option A)** until the channel has traction.
- **Build Option B later** once you're posting daily and the audits are worth the effort. Start the TikTok and Google audit applications early, since they take the longest.

## Rules that apply however you post
- **AI label ON everywhere**: TikTok `is_aigc` / AI-generated content, YouTube `containsSyntheticMedia`, Meta "AI info".
- Same master file everywhere, no re-uploads of another platform's watermarked export.
- Keep the posting time consistent; don't post the same episode twice to one platform.

## Sources
- [TikTok Content Posting API — Direct Post reference](https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post)
- [TikTok Content Sharing Guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines)
- [TikTok Content Posting API: Direct Post, Audit, Limits — Outstand](https://www.outstand.so/blog/tiktok-content-posting-api)
- [YouTube Data API — Videos: insert](https://developers.google.com/youtube/v3/docs/videos/insert)
- [YouTube Data API — Revision History](https://developers.google.com/youtube/v3/revision_history)
- [YouTube API quota changes 2026 — bundle.social](https://bundle.social/blog/youtube-api-quota-exceeded-limits-fixes)
- [Instagram Platform — Content Publishing](https://developers.facebook.com/docs/instagram-platform/content-publishing/)
- [Instagram Reels API guide 2026 — Phyllo](https://www.getphyllo.com/post/a-complete-guide-to-the-instagram-reels-api)
- [Best social media scheduling tools 2026 — Buffer](https://buffer.com/resources/social-media-scheduling-tools/)
- [Best Instagram Reels schedulers 2026 — ShortSync](https://www.shortsync.app/best/instagram-reels-scheduler)
