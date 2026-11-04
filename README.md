# deep-track

A 24-week deep dive into how modern AI systems work, from autograd to production inference.
Everything here is rebuilt by hand from a blank file, without AI-generated code.

| Phase | Focus | Capstone |
| 1 | Neural net foundations, storage engines, evals | Eval harness, key-value store |
| 2 | Transformers, RAG, agents | Vector search + RAG/agent system with evals |
| 3 | Pretraining and fine-tuning | LoRA fine-tune vs. prompted large model |
| 4 | Inference and production | Served model with caching, monitoring, cost tracking |

**Sources:** Karpathy's *Neural Networks: Zero to Hero*, Raschka's *Build a Large Language Model (From Scratch)*,
Huyen's *AI Engineering*, Kleppmann's *Designing Data-Intensive Applications*.

Each `wNN-*` folder holds that week's code and a `NOTES.md` covering what I learned and what was hard.
