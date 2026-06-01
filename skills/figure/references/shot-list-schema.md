# Shot List Schema

Return shot lists in the source language by default. Use Traditional Chinese for Traditional Chinese input, Simplified Chinese for Simplified Chinese input, concise English for English input, and preserve key technical terms in mixed-language input.

For a paragraph, return exactly one shot unless the user asks otherwise.

For a full article, return 5-8 shots. Cover the article's reasoning arc rather than every paragraph.

For Chinese input, use this structure:

```markdown
## Shot List

### 1. [short theme]
- 主題：
- 核心內容：
- 核心觀點：
- 結構類型：flow | state-map | comparison | method | system | decision
- 兔子動作：
- 文字標註：
- Image-2 prompt：
```

For English input, use this structure:

```markdown
## Shot List

### 1. [short theme]
- Theme:
- Core Content:
- Core Viewpoint:
- Structure Type: flow | state-map | comparison | method | system | decision
- Rabbit Action:
- Text Labels:
- Image-2 Prompt:
```

## Field Guidance

- `主題` / `Theme`: 6-14 Chinese characters for Chinese input or 2-6 English words for English input; describe the visual idea, not the source paragraph title.
- `核心內容` / `Core Content`: one sentence summarizing the insight being visualized.
- `核心觀點` / `Core Viewpoint`: the one viewpoint this image will defend. If there are two viewpoints, split or discard one.
- `結構類型` / `Structure Type`: choose one type from the allowed list.
- `兔子動作` / `Rabbit Action`: a concrete physical action that performs the insight.
- `文字標註` / `Text Labels`: 2-5 short labels in the source language, each usually 2-8 Chinese characters or 1-3 English words. Avoid long sentences.
- `Image-2 prompt` / `Image-2 Prompt`: final generation prompt, ready to send to image-2.

## Selection Heuristics

- Prefer passages with verbs, contrasts, dependencies, loops, prioritization, or state changes.
- Merge adjacent paragraphs when they express one cognitive movement.
- Avoid making separate shots for examples unless the example changes the reasoning.
- For each shot, choose one dominant structure and remove supporting details that would make the image read like a user manual.
- For 5-shot article sets, use: problem/state, hidden mechanism, method/operation, decision/tradeoff, final mental model.
- For 8-shot article sets, add: context trigger, failed approach, key transition, feedback loop.
