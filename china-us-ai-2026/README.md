# Is China's AI catching up, or copying? Two claims tested

Written 2026-11-13. Research and drafting: Claude Opus 5.5. Evidence
search, fact check and verdict review: Claude Fable 5.2. The page is
`index.html`; every source is listed at its end.

## The two claims

- A: "Chinese AI is a lot more scalable than US AI, it's more optimized.
  US AI is only better because of raw processing power, so either way
  they're gonna win."
- B: "China is always 6 months behind Anthropic and OpenAI because they're
  mainly just distilling their models. Always lagging, no real innovation."

## Answer

- **The gap is about 4 to 8 months, centred near 6, with no clear trend.**
  Epoch AI: 7 months on average since 2023 (range 4 to 14). CAISI: DeepSeek
  V4 Pro about 8 months behind (May 2026). The 4-month figures compare open
  with closed models, not China with the US.
- **Claim A is mostly wrong.** Chinese labs published real efficiency
  methods (MLA, open GRPO reasoning recipe, MuonClip, sparse attention).
  But they are short of compute: they ration service (Caixin, Apr 2026) and
  DeepSeek raised prices in Aug 2026. The US has 7.6x the AI chips shipped
  since 2022 (Epoch) and about 16x the training compute (IFP). Published
  efficiency helps both sides. China scales better only in electricity.
- **Claim B: the number is right, the reason is half right.** Anthropic
  attributes about 190 million exchanges in May-July 2026 to Chinese labs
  (Alibaba 151 million). IFP estimates distillation halves the gap, from
  about 13 to about 6.5 months. "No real innovation" is false. Most
  distillation evidence comes from interested parties, and the post says so.
- **China leads in open models**: 41% of Hugging Face downloads, Qwen
  derivatives 2.6x Meta's, over half of OpenRouter tokens in Sep 2026.

## Files

| File | What |
| --- | --- |
| `page.html` | The page text, with `{{chart:NAME}}` markers |
| `data.json` | Every number in the charts, with a source key |
| `build.py` | Draws the charts as static SVG (wide and phone layouts) and writes `index.html` |
| `index.html` | The built page. Do not edit by hand |
| `card.png` | Social preview image |

Rebuild: `python3 build.py` in this folder.

## How the sources were checked

The cloud container could load only anthropic.com directly. Anthropic's
February, September and October 2026 reports and its pricing page were read
in full. Everything else was seen through web search results, and the page
tags each source `read` or `search`.
