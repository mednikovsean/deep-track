# deep-track

> A 24-week deep dive into how modern AI systems work, from autograd to production inference.
> Every line here is rebuilt by hand from a blank file. No AI-generated code.

---

## Roadmap

| Phase | Weeks | Focus | Capstone |
|:-----:|:-----:|-------|----------|
| **1** | 1–6   | Neural net foundations · storage engines · evals | Eval harness · key-value store |
| **2** | 7–12  | Transformers · RAG · agents | Vector search + RAG/agent system with evals |
| **3** | 13–18 | Pretraining · fine-tuning | LoRA fine-tune vs. prompted large model |
| **4** | 19–24 | Inference · production | Served model with caching, monitoring, cost tracking |

## Progress

- [ ] **Phase 1:** Foundations
- [ ] **Phase 2:** Transformers, RAG, agents
- [ ] **Phase 3:** Training and fine-tuning
- [ ] **Phase 4:** Running AI in production

## Repo layout

```text
deep-track/
├── w01-micrograd/
│   ├── micrograd.py
│   └── NOTES.md        # what I learned, what was hard
├── w02-.../
└── ...
```

## Sources

| Resource | Author | Covers |
|----------|--------|--------|
| [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | Andrej Karpathy | Backprop, language models, GPT from scratch |
| [Build a Large Language Model (From Scratch)](https://github.com/rasbt/LLMs-from-scratch) | Sebastian Raschka | Tokenization, attention, pretraining, fine-tuning |
| [AI Engineering](https://github.com/chiphuyen/aie-book) | Chip Huyen | Evals, RAG, agents, inference optimization |
| [Designing Data-Intensive Applications](https://dataintensive.net) | Martin Kleppmann | Storage, replication, transactions, distributed systems |

## Method

1. Watch or read a section, then implement it.
2. Rebuild it the next session from a blank file, with no video or book open.
3. Write `NOTES.md`: three things I can explain now, and one thing still unclear.
