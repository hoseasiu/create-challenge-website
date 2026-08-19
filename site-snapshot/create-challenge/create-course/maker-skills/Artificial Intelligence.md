---
title: "Artificial Intelligence"
url: https://beaver-works-assistive-tech.mit.edu/create-challenge/create-course/maker-skills/artificial-intelligence
snapshot_date: 2026-08-19
content_status: full
nav_parent: "Maker Skills"
source_html: maker-skills-artificial-intelligence.html
---

# Artificial Intelligence

Covers what AI actually is, how large language models work, the ethical and educational risks of using them, and how teams should think about using AI either as a development **tool** or as a **component** of their product.

---

## What Is Artificial Intelligence?

AI is hard to define precisely. Two modes matter for this course: **using AI to help build your product** (AI as tool) vs. **using AI as part of your product** (AI as component) — these raise different considerations (team learning vs. co-designer impact, respectively).

---

## AI Is Not Just Chatbots

Chatbots are one visible form of AI, but AI also covers speech recognition, OCR, image recognition/captioning/generation, game-playing (chess, Go, Starcraft 2, DotA2), protein design, code generation, and theorem proving.

Machine learning — where rules are learned from data rather than hand-programmed — underlies most modern AI. A nested diagram (`website-images/ai-diagram.png`) shows how AI ⊃ Machine Learning ⊃ Deep Learning ⊃ Generative AI ⊃ Large Language Models ⊃ Chatbots.

### Neural Networks
Includes 3Blue1Brown's "But what is a neural network? | Deep learning chapter 1" (YouTube: `aircAruvnKk`).

---

## Large Language Models

Includes 3Blue1Brown's "Large Language Models explained briefly" (YouTube: `LPZh9BOjkQs`), the fifth video in the Deep Learning series.

### What Can LLMs Do?
Natural-language conversation, writing, code generation, information retrieval, task automation. Biggest impact so far: software engineering and (negatively) take-home educational assessments.

---

## The Ethics of Large Language Models

- **Intellectual Property** — LLM training has relied heavily on copyrighted/pirated text; Anthropic paid $1.5B to settle a book-piracy suit; many lawsuits against major LLM providers are ongoing as of 2026.
- **Moderation and Training** — human content moderators (often in low-income countries) bear psychological costs of filtering harmful AI output.
- Recommended resources: *Empire of AI* (Karen Hao), *Magnifica Humanitas* (Pope Leo XIV, Ch. 3–4).

---

## Educational Risks

Cites a 2024 MIT experiment (Eric Klopner) where a ChatGPT-assisted group solved a coding problem fastest but failed a comprehension test afterward, and an MIT Media Lab brain-activity study finding ChatGPT-assisted essay writers were less engaged and produced more homogeneous work. Includes a 2025–2026 CRE[AT]E team anecdote about AI-generated code the team couldn't debug themselves.

---

## Privacy and Consent

Distinguishes **cloud** AI (data leaves your control; "if you're not paying, your data is the product") from **local/edge** AI (runs on your own hardware, less powerful but private).

### Local AI Models
Interfaces: llama.cpp, llamafile, ollama. Models: Gemma 4, Llama 4, Phi-4 (LLMs); DETR, YOLO26 (object detection); Nemotron 3.5, Whisper v3 (speech). HuggingFace hosts open models/datasets.

---

## AI and Disability

Key framing question: does the AI's input come from the co-designer (may need disability-specific fine-tuning, e.g. atypical speech or spasticity-affected movement) or from the external world (standard models may work fine, e.g. scene description for a blind user)?

---

## Your Team's Approach to AI as a Tool

**Required:** no LLM/image-gen use for course submissions or documentation (strictly prohibited); teams must follow AI providers' own policies; other project use must be disclosed per the team's own AI use policy.

**Assignment: Draft an AI Tool Use Policy** — a single set of team rules, a justification, and all team members' names as signatures. Teams may ban AI entirely if they choose, but must justify the choice either way.

---

## Your Team's Approach to AI as a Component of Your Project

**Required:** products for users who cannot legally consent (e.g. minors, some cognitive disabilities) may not use commercial cloud-based AI; where legal consent is possible, teams must explain data handling and get agreement (with adult-coach involvement for high school teams).

**Assignment: Draft an AI Component Policy** — list of risks, mitigations, and a co-designer-appropriate communication plan. Local models mitigate privacy risk but not all safety/ethical risk (the Challenge's existing ban on safety-critical projects still applies).

---

## Content Disclosure

Page states that site text is human-generated, with the exception that Claude Code helped convert plaintext to HTML and build certain UI elements (e.g. search bars), and that the Additional Resources page's link descriptions were AI-generated/gathered via Claude Code.

See also [[Additional Resources]], [[Software]].
