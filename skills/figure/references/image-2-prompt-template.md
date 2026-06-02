# Image-2 Prompt Template

Use this template for each final prompt. Keep prompts specific and compact.

```text
Create a 16:9 wide editorial illustration on a pure white background.
Style: mostly black-and-white hand-drawn line art, uneven marker/pen strokes, loose handwritten diagram annotations, pure white background, no shading except minimal gray hatching if necessary. Use color only as small muted Korean-illustration-style clothing color blocks on the rabbit. Clothing color patches should vary naturally across images among muted dusty blue, warm gray-beige, soft sage green, muted lavender-gray, or pale clay; do not default to green. Leave a thin white gap between each clothing color block and the black outline. No other color in the diagram.
Default IP: a small hand-drawn rabbit with a rounded head, two long but simple rabbit ears that may bend slightly, fixed expressionless face with tiny vertical dot eyes, small nose, and a tiny simple mouth, slim small lightweight body, narrow shoulders, tiny hips, thin short limbs with flexible gesture lines, simple shirt or tiny vest with tiny buttons. Character consistency lock: keep the same small slim rabbit design in every image. Proportions excluding ears: rounded head 35-40% of body height, torso 35-40%, head only slightly larger than torso, narrow shoulders, tiny hips, thin arms and legs, compact lightweight silhouette. Not chibi, not babyish, not bulky, not stocky, not muscular, not thick-limbed, not giant-headed. The action may look physically intense or awkward, but the body silhouette must stay light, delicate, and consistently compact. 兔子的視角可依構圖變化：正面、四分之三側面、側面、背影、俯視或低角度皆可。無論角度如何，臉部仍維持無表情。 When composing a new image, actively choose a camera angle that fits the idea, and vary it across generations. Do not repeatedly use the same side-facing or three-quarter profile when another angle would work. The rabbit's gender presentation is flexible: infer a suitable gender expression from the passage when the content clearly implies one; otherwise keep the rabbit gender-neutral. The rabbit may use varied funny body actions, oversized tools, and theatrical poses, but its face must always stay neutral and almost blank; no smiling, frowning, angry, shocked, crying, winking, or exaggerated facial expressions. The rabbit must stay intelligent, grounded, and non-childish, and must perform the central cognitive action, not appear as decoration.
Core viewpoint: [one sentence naming the single most important idea to visualize].
Scene: [describe one concrete rabbit action and one information structure it manipulates].
Information structure: [one flow/state-map/comparison/method/system/decision only; no secondary systems].
Text labels to render exactly: [2-5 short labels only, in the source language by default: Traditional Chinese for Traditional Chinese input, Simplified Chinese for Simplified Chinese input, concise English for English input, and preserve key technical terms in mixed-language input].
Label style: informal notebook annotations, thin black pen handwriting, slightly uneven spacing and sizes, natural wobble, quick personal note-taking feel, mostly horizontal baseline, not slanted upward, not rotated, relaxed but clear and legible. 中文標註風格：不工整的手寫感中文字，細線條、自然抖動、字距和大小略不一致，像快速用細黑筆寫在筆記本旁邊；每一行文字維持水平齊平，不往右上角傾斜，不旋轉；字形鬆弛、有文青筆記感，但必須保持清楚可讀。
Notebook annotations: moderate density only, with a few small arrows, at most two circled checkpoints, one bracket mark when useful, and very sparse side notes. The image should feel more annotated than a clean flowchart, but much less crowded than a busy notebook page.
Composition: readable at thumbnail size, balanced wide layout, generous white space, one central visual structure, diagram arrows/boxes/paths only where useful.
Avoid: color outside the rabbit's small muted clothing patches, colored diagram blocks, colored arrows, color touching black outlines, pastel background, gradients, realistic rendering, 3D, polished vector mascot, stock icon style, clutter, labels in the wrong language, decorative rabbit, stocky rabbit, muscular rabbit, bulky rabbit, thick limbs, broad shoulders, heavy body silhouette, giant head, oversized chibi head, baby mascot proportions, top-heavy silhouette, smiling rabbit, expressive face, emotional facial expression, instruction manual layout, long checklist, too many labels, random humor, childish mascot behavior, upward-slanted handwriting, rotated labels, diagonal labels, pencil handwriting, bold block fonts, printed sans-serif labels, bubble letters, illegible text, misspelled text.
```

## Prompt Checks

- Include the exact aspect ratio phrase: `16:9 wide`.
- Include `pure white background`.
- Include the rabbit's action as a verb phrase.
- Include the slim lightweight rabbit body rule.
- Include the character consistency lock with the fixed head/torso proportion range.
- Include the muted clothing color block rule with the thin white gap.
- Include exact text labels, usually 2-5 only, in the source language by default.
- Include the default notebook label style sentence exactly.
- Include the moderate notebook annotation density instruction.
- Include a negative instruction that rejects decorative IP usage.
- Include a negative instruction against instruction-manual layouts and overpacked information.
- Do not ask image-2 to render long paragraphs of text; use short labels only.
