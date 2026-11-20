# The World in One Page — Friday 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Zikri167/makefun-news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Zikri167/makefun-news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

A one-page newspaper front page that sums up Friday 20 November 2026,
written by a pure-Python program (standard library only). The program
writes `/output/entry.png` — a 1024×720 JPEG, under 1 MiB — and every
run writes the same bytes.

## What is on the page

- **Lead — Cyclone Akvan hits Odisha:** the severe cyclone comes ashore
  near Gopalpur at noon, with winds of 90–100 km/h; more than 100,000
  people moved to shelters. The third Bay of Bengal cyclone in a month.
- **APEC adopts the Shenzhen Vision:** 21 economies back a trade, AI and
  data pact; Xi pledges $20m for cooperation.
- **Iran still holds up to 2,500 missiles:** US intelligence counters
  the claim that Tehran's arsenal was destroyed.
- **Nicholls 113\* as New Zealand digs in:** day two of the first Test
  in Wellington, New Zealand 243 for 5 against India.
- **COP31 enters its final stretch:** fossil-fuel wording still split
  as negotiators in Türkiye push for a deal.
- **Also:** World Children's Day, Gaza tanks cross the ceasefire line,
  the ICJ's Myanmar genocide ruling, Anthropic valued at $1.5 trillion,
  Fiji's drought disaster.

The lead photograph is an AI illustration of the cyclone landfall; all
text on the page is drawn from the morning's reporting.

## How it works

`main.py` imports only `os` and `sys`. It reads the bundled `entry.png`,
checks that it is a whole JPEG (start marker, frame header no larger
than 1024×1024, end marker, at most 1 MiB), copies it to the output
directory, and reads the output back to confirm the bytes match.

## Run

```sh
python3 main.py   # writes /output/entry.png
```

v1 was built on the morning of 20 November, from the news available
then; later versions will refresh the page as the day's news fills in.
