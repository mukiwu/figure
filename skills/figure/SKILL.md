---
name: figure
description: Turn article passages, technical concepts, or short explanations into 16:9 white-background, mostly black-and-white, hand-drawn line illustrations using Codex image generation/image-2. Use when the user wants a passage, section, or paragraph in Chinese, English, or mixed language transformed into visual explanation shots, methodology diagrams, process/state/action illustrations, or a shot list where a default hand-drawn rabbit IP participates in the core cognitive action rather than decorating the scene.
---

# Figure

## Overview

Use this skill to extract the single most important cognitive structure from article passages, technical concepts, or short explanations and turn it into focused explanatory illustration shots. The default output is a 5-8 shot list for full articles, or one generated 16:9 image for a single paragraph/passage.

## Core Rules

- Treat the illustration as a focused thinking diagram, not an article thumbnail or instruction manual.
- First converge on the single most important core viewpoint. Do not try to include every detail, example, tool, role, or branch from the source text.
- Each image must explain one core structure only: one flow, one state change, one comparison, one method, one system relation, or one decision.
- Identify the cognitive action after convergence: compare, sort, filter, connect, iterate, diagnose, choose, compress, expand, map, hand off, break down, or reframe.
- Make the rabbit IP perform the core action. Do not place the rabbit as a mascot, narrator, sticker, corner decoration, or unrelated observer.
- The rabbit's gender presentation is flexible: infer a suitable gender expression from the passage when the content clearly implies one; otherwise keep the rabbit gender-neutral.
- Preserve the rabbit's character proportions in every final prompt using the Character Consistency Lock from [references/visual-ip.md](references/visual-ip.md): small cute child-height rabbit, short and compact, rounded head clearly larger than torso but not huge, narrow shoulders, tiny hips, short thin limbs, tiny hands and feet, compact lightweight silhouette. The rabbit should feel closer to a young child's body height than an adult's: cute and small, but still simple editorial line art rather than a polished mascot. Do not make the rabbit adult-proportioned, tall, lanky, stocky, bulky, muscular, thick-limbed, broad-shouldered, heavy, or giant-headed.
- Use a pure white background, mostly black-and-white line art, hand-drawn marker/pen texture, and a 16:9 wide composition.
- Color is allowed only as small muted Korean-illustration-style clothing color blocks on the rabbit. Keep all diagrams, labels, arrows, backgrounds, and information structures black-and-white. Leave a thin white gap between each clothing color block and the black outline.
- Keep text labels sparse, short, legible, and embedded in the diagram. Prefer 2-5 labels per image.
- Match label language to the source text by default: Traditional Chinese for Traditional Chinese input, Simplified Chinese for Simplified Chinese input, concise English for English input, and preserve key technical terms in their original language for mixed-language input.
- Render text labels directly in the image by default.
- Use this label style exactly: 中文標註風格：字形連貫流動，筆畫帶速度感，線條有自然抖動和停頓，可能會因為急促感而將幾個筆畫連起來，但不影響閱讀，筆尾輕輕拉長但不過於誇張，結構鬆動但清晰，整體像情緒很滿時寫下的一句手寫標題。
- Use the bundled font [assets/fonts/ChenYuluoyan-2.0-Thin.ttf](assets/fonts/ChenYuluoyan-2.0-Thin.ttf) only as an optional post-processing fallback when the user explicitly asks for stable typography.
- Avoid color outside the rabbit's small muted clothing color blocks unless the user explicitly overrides the default.
- Prefer Traditional Chinese labels when the input uses Traditional Chinese; mirror the input's language and Chinese variant when clear.

## Workflow

1. Classify the input:
   - One paragraph or a selected passage: create 1 shot spec and generate 1 illustration unless the user only asks for a prompt or shot list.
   - A full article or multiple sections: create a 5-8 shot list with prompts; generate all images only if the user explicitly asks for image generation for the full set.
   - If uncertain, default to 1 shot for short inputs under roughly 500 Chinese characters or 300 English words, and 5-8 shots for longer structured articles.
2. Extract visual candidates:
   - Find claims that describe movement, transformation, tension, workflow, state change, decision-making, or method.
   - Skip purely atmospheric, anecdotal, or decorative lines unless they reveal the article's core thinking.
   - Rank candidates by explanatory value, then keep only the most important one for each image.
3. Choose each shot's structure type:
   - `flow`: steps, sequence, pipeline, feedback loop.
   - `state-map`: before/after, current/future, stuck/unstuck, health/status.
   - `comparison`: A/B, tradeoffs, spectrum, matrix.
   - `method`: framework, checklist, layered model, operating principle.
   - `system`: roles, inputs/outputs, dependencies, handoff.
   - `decision`: fork, criteria, prioritization, constraint sorting.
4. Design the rabbit's action:
   - Make the rabbit physically manipulate the idea: pull threads, move cards, connect dots, hold a magnifier, climb steps, balance tradeoffs, open nested boxes, untangle loops, point to a map, or carry a concept through a pipe.
   - Ensure the action changes or reveals the information structure.
   - Give the rabbit a creative, slightly odd editorial gesture when useful, but keep it intelligent, grounded, and non-childish.
5. Produce the required output:
   - For article input, return the shot list. For each shot include theme, core content, structure type, rabbit action, text labels, and the final image prompt.
   - For paragraph input, produce the same one-shot spec, then generate the image with Codex image generation/image-2 when running inside Codex.
6. Generate images:
   - When running inside Codex and no alternate image model is explicitly requested by the user, Codex image generation/image-2 is mandatory. Do not ask the user to choose a model, do not substitute another renderer, and do not return only prompts when the Codex image generation tool is available.
   - Ask image-2 to render the 2-5 text labels directly using the exact label style above and the source language rules.
   - Include this exact character consistency lock in every final prompt: `Character consistency lock: keep the same small cute child-height rabbit design in every image. Proportions excluding ears: rounded head 42-48% of body height, torso 30-34%, head clearly larger than torso but not huge, narrow shoulders, tiny hips, short thin arms and legs, tiny hands and feet, compact lightweight silhouette. Cute and small like a young child's body height, but still simple editorial line art, not a polished mascot. Not adult-proportioned, not tall, not lanky, not bulky, not stocky, not muscular, not thick-limbed, not broad-shouldered, not heavy, not giant-headed.`
   - If the user explicitly asks for stable typography, use the bundled font workflow: ask image-2 for a no-text illustration with blank label spaces or small leader lines, then add labels with [scripts/render_labels.py](scripts/render_labels.py).
   - If the user explicitly requests another image model or renderer, use that requested renderer and preserve the same visual constraints, label rules, and prompt structure as closely as the renderer allows.
   - If the current environment is not Codex and another image generation tool is available, generate the image with that available tool instead of returning only prompts.
   - If no image generation tool is available, return the shot spec and final portable prompts cleanly.
   - Remove secondary labels, extra icons, and side concepts from the prompt before generation if the scene starts to look like a manual.

## References

- Read [references/visual-ip.md](references/visual-ip.md) when writing the rabbit character prompt.
- Read [references/shot-list-schema.md](references/shot-list-schema.md) when formatting shot lists.
- Read [references/image-2-prompt-template.md](references/image-2-prompt-template.md) when composing final generation prompts.
- Read [references/font-label-workflow.md](references/font-label-workflow.md) only when the user explicitly asks for stable post-processed typography.
