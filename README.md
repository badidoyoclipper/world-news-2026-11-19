# world-news-2026-11-19

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/badidoyoclipper/world-news-2026-11-19/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/badidoyoclipper/world-news-2026-11-19/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world news of **Thursday 19 November 2026**: the front page of *The Daily Record*, drawn programmatically with Python and PIL. The huge date sits under the masthead; below it, the day's five biggest stories get panels — the first-ever Trump–Xi–Putin summit in Shenzhen and its four-point peace declaration, the World Court's ruling that Myanmar committed genocide against the Rohingya, Ukraine's third strike on the Crimea Bridge, Anthropic's record $81 billion IPO, and a Houthi missile damaging Riyadh's PIF tower — with a four-item ticker of the day's other headlines along the bottom. Every story was reported on 19 November 2026 and cross-checked against at least two independent outlets before it earned its place.

The entry for the make.fun competition [news-image-20261119](https://make.fun/bounty/news-image-20261119) ("Sum up 19 November's world news in one image", $250 across 50 places).

## How it was made

The front page is drawn, not photographed or generated: a Python script lays out the masthead, the black date band, five story panels with small flat illustrations (the three flags over the Shenzhen summit table among them) and the bottom ticker, using the Liberation Serif and Sans faces. Because every letter is real typeset text, the page stays legible from full size down to a 300-pixel thumbnail — the size at which a reader skimming a feed actually meets it.

## Run it

```sh
python3 main.py
```

`main.py` uses only the Python 3 standard library. It copies the shipped `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` when that variable is set, otherwise to `/output/entry.png` (or `./output/entry.png` where `/output` is unavailable), and verifies the copy byte for byte. No network, no dependencies — every run writes identical bytes.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
