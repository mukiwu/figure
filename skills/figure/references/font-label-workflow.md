# Font Label Workflow

Use this optional workflow only when the user explicitly asks for stable post-processed typography. The default workflow is to render text labels directly in image-2 with the label style from `image-2-prompt-template.md`.

## Bundled Font

Default font:

```text
assets/fonts/ChenYuluoyan-2.0-Thin.ttf
```

This bundled font is primarily useful for final Chinese labels when present. For English labels, prefer direct rendering unless a separate English handwriting font is added.

## Workflow

1. Generate a 16:9 no-text base illustration:
   - Ask image-2 not to render text labels.
   - Ask it to leave blank label spaces, leader lines, or simple empty tags.
   - Keep the visual structure simple enough that labels can be added after.
2. Decide 2-5 label positions:
   - Use normalized coordinates from 0 to 1 for `x` and `y`.
   - Keep labels near their visual target.
   - Avoid placing labels over the rabbit's face, hands, or the core action.
3. Run `scripts/render_labels.py`:

```bash
python3 scripts/render_labels.py input.png output.png labels.json
```

Example `labels.json`:

```json
[
  { "text": "AI 快", "x": 0.18, "y": 0.35, "size": 54 },
  { "text": "慢下來", "x": 0.48, "y": 0.22, "size": 54 },
  { "text": "品質", "x": 0.75, "y": 0.38, "size": 54 }
]
```

## Fallback

If post-processing is not practical, include labels directly in the image prompt with the default label style, but warn that exact typography and text accuracy are not guaranteed.
