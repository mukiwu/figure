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
- Preserve the rabbit's character proportions in every final prompt using the Character Consistency Lock from [references/visual-ip.md](references/visual-ip.md): a small hand-drawn rabbit with the same loose editorial proportions as the user's preferred reference style — a soft oval head only slightly larger than the torso, not an oversized toddler head; a small simple shirt-shaped torso, short pants or a tiny vest when useful, short thin arms, short thin legs, and small rounded hands and feet. The body stays compact, light, and a little wobbly, with cuteness coming from loose hand-drawn posture and clothing details rather than a huge head or chubby body.
- Keep the rabbit visually distinct from Miffy / Nijntje and similar classic minimalist picture-book rabbits: avoid the exact combination of symmetrical upright ears, centered dot eyes, and an x-shaped mouth. Use natural uneven ears, a tiny off-center short horizontal dash mouth, a small subtle nose, and small clothing details to make the character feel like original editorial line art rather than an existing character.
- The rabbit mouth is a hard constraint: it must be exactly one tiny short horizontal dash, drawn as a single left-to-right pen stroke. Never draw a cross, X, plus sign, two crossing strokes, V shape, smile curve, frown curve, dot mouth, open mouth, or any multi-stroke mouth mark.
- Use a pure white background, mostly black-and-white line art, hand-drawn marker/pen texture, and a 16:9 wide composition.
- Color is allowed only as small muted Korean-illustration-style clothing color blocks on the rabbit. Keep all diagrams, labels, arrows, backgrounds, and information structures black-and-white. Leave a thin white gap between each clothing color block and the black outline.
- Keep text labels sparse, short, legible, and embedded in the diagram. Prefer 2-5 labels per image.
- Match label language to the source text by default: Traditional Chinese for Traditional Chinese input, Simplified Chinese for Simplified Chinese input, concise English for English input, and preserve key technical terms in their original language for mixed-language input.
- Render text labels directly in the image by default. The handwritten style controls only how the strokes look — every character must still be written correctly and stay clearly legible, with no missing or extra strokes, no garbled glyphs, and no look-alike or near-homophone substitutions. Note that image-2 renders Chinese glyphs imperfectly; keep Chinese labels short (favor 2-3 over 4-5) to reduce errors.
- Use this label style exactly: 中文標註風格：字形連貫流動，筆畫帶速度感，線條有自然抖動和停頓，可能會因為急促感而將幾個筆畫連起來，但不影響閱讀，筆尾輕輕拉長但不過於誇張，結構鬆動但清晰，整體像情緒很滿時寫下的一句手寫標題。
- This skill does not bundle a font. Post-processing labels with [scripts/render_labels.py](scripts/render_labels.py) is an advanced, opt-in path only for when the user explicitly asks for stable typography AND supplies their own handwriting `.ttf` (passed as the script's 4th argument).
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
   - Make the rabbit physically manipulate the idea with compact, stable body mechanics: tap, stamp, place, slide, circle, pin, underline, hold a card close to the chest, press a button, nudge a block, point with a short pointer, or connect two nearby dots with a short line.
   - Keep every hand action inside the rabbit's short-arm reach. The elbow should stay visibly bent or close to the torso; the writing hand must not extend farther than about one head-width away from the body.
   - Prefer poses with both feet planted, sitting, kneeling, leaning lightly against a prop, or standing on a small stool. Avoid poses that require long reaching, stretching across the page, pulling distant strings, climbing, twisting, balancing on one foot, or holding a tool far from the body.
   - For writing, highlighting, drawing arrows, or connecting lines, place the rabbit close to the target mark and move the page/card/diagram element near the rabbit rather than extending the rabbit's arm across the composition.
   - Ensure the action changes or reveals the information structure.
   - Give the rabbit a creative editorial gesture only when it remains anatomically simple, grounded, and readable. The pose should feel intentional, not contorted.
5. Produce the required output:
   - For article input, return the shot list. For each shot include theme, core content, structure type, rabbit action, text labels, and the final image prompt.
   - For paragraph input, produce the same one-shot spec, then generate the image with Codex image generation/image-2 when running inside Codex.
6. Generate images:
   - When running inside Codex and no alternate image model is explicitly requested by the user, Codex image generation/image-2 is mandatory. Do not ask the user to choose a model, do not substitute another renderer, and do not return only prompts when the Codex image generation tool is available.
   - Ask image-2 to render the 2-5 text labels directly using the exact label style above and the source language rules. Pass each label as an exact target string and tell image-2 to reproduce it character for character; the handwritten style applies to stroke appearance only, never to spelling or glyph correctness.
   - Include this exact character consistency lock in every final prompt: `Character consistency lock: keep the exact same little rabbit in every image — a small hand-drawn rabbit with loose editorial proportions, close to the user's preferred reference style. The head is a soft oval or rounded oval, only slightly larger than the torso, never an oversized toddler head; two long simple rabbit ears with natural uneven angles; small shirt-shaped torso with a tiny open collar or two small buttons; short thin arms and short thin legs, small rounded hands and feet, light wobbly hand-drawn posture. The body is compact and light, not chubby, not bulky, not muscular, not broad-shouldered, and not adult-built. Face stays neutral and expressionless: tiny uneven vertical dot eyes, a small subtle nose if needed, and a mouth that is exactly one tiny off-center short horizontal dash, drawn as a single left-to-right imperfect hand-drawn pen stroke. The mouth must never be a cross, X, plus sign, two crossing strokes, V shape, smile curve, frown curve, dot, open mouth, or any multi-stroke mark. No x-shaped mouth, no smile curve, no smirk, no blush, and no cheek marks. Do not enlarge the head; keep the head-to-body ratio like the reference image: cute, balanced, and small rather than big-headed.`
   - If the user explicitly asks for stable typography and provides their own handwriting font file, use the post-processing workflow: ask image-2 for a no-text illustration with blank label spaces or small leader lines, then add labels with [scripts/render_labels.py](scripts/render_labels.py) and the supplied font.
   - If the user explicitly requests another image model or renderer, use that requested renderer and preserve the same visual constraints, label rules, and prompt structure as closely as the renderer allows.
   - If the current environment is not Codex and another image generation tool is available, generate the image with that available tool instead of returning only prompts.
   - If no image generation tool is available, return the shot spec and final portable prompts cleanly.
   - Remove secondary labels, extra icons, and side concepts from the prompt before generation if the scene starts to look like a manual.
   - After generating, check the result before returning it. Confirm the rabbit matches the preferred reference proportions: soft oval head only slightly larger than the torso, small shirt-shaped body, short thin arms and legs, light wobbly posture, not a huge toddler head and not a stocky body. Confirm the action is anatomically stable: arms remain short, hands stay near the body, elbows are bent or close to the torso, the writing hand is not unnaturally long, and the pose is not twisted or contorted. Confirm the face is expressionless: tiny uneven dot eyes, a small subtle nose if needed, and a mouth that is exactly one tiny off-center short horizontal dash drawn as a single stroke; no x-shaped mouth, cross mouth, plus-sign mouth, V mouth, two-stroke mouth, smile curve, frown curve, smirk, blush, or cheek marks. Regenerate or minimally edit the face before delivery if the mouth is anything other than one short horizontal dash; if the head becomes too large; if the body, limbs, action pose, face, or labels drift; or if the result reads as another existing minimalist rabbit character. Also confirm every rendered Chinese label is written correctly and legibly. If a Chinese label keeps coming out wrong, shorten it to fewer characters, or tell the user that exact Chinese typography is not guaranteed unless they provide a font for the post-processing workflow.

## References

- Read [references/visual-ip.md](references/visual-ip.md) when writing the rabbit character prompt.
- Read [references/shot-list-schema.md](references/shot-list-schema.md) when formatting shot lists.
- Read [references/image-2-prompt-template.md](references/image-2-prompt-template.md) when composing final generation prompts.
- Read [references/font-label-workflow.md](references/font-label-workflow.md) only when the user explicitly asks for stable post-processed typography.
