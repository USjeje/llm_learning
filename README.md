# 📜 大语言模型（LLM）发展时间线（2003–2025）

整理内容包含：
- 模型结构演进
- 推理能力增强（Reasoning）
- 推理效率优化（Inference Optimization）
- 多模态与智能体趋势
- 国内大模型进展与 Agent 生态

---

## 🧱 2003–2013：语言模型的神经网络起点

- **2003**：NNLM  
  📄 [Neural Probabilistic Language Model](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)

- **2010**：RNNLM  
  📄 [Recurrent Neural Network Based Language Model](https://www.fit.vutbr.cz/research/view_pub.php?id=9848)

- **2013**：Word2Vec  
  📄 [Efficient Estimation of Word Representations](https://arxiv.org/abs/1301.3781)

---

## 🧠 2014–2016：词向量与上下文建模

- **2014**：GloVe  
  📄 [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf)

- **2016**：FastText  
  📄 [Enriching Word Vectors with Subword Information](https://arxiv.org/abs/1607.04606)

---

## 🧠 2017–2018：Transformer 与上下文革命

- **2017**：Transformer  
  📄 [Attention is All You Need](https://arxiv.org/abs/1706.03762)

- **2018**：ELMo  
  📄 [Deep Contextualized Word Representations](https://arxiv.org/abs/1802.05365)

- **2018**：GPT-1  
  📄 [Improving Language Understanding by Generative Pre-Training](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)

- **2018**：BERT  
  📄 [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805)

---

## 🚀 2019–2020：预训练语言模型爆发

- **2019**：GPT-2  
  📄 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

- **2019**：XLNet  
  📄 [XLNet: Generalized Autoregressive Pretraining](https://arxiv.org/abs/1906.08237)

- **2019**：RoBERTa  
  📄 [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)

- **2020**：T5  
  📄 [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://arxiv.org/abs/1910.10683)

- **2020**：ELECTRA  
  📄 [ELECTRA: Pre-training Text Encoders as Discriminators](https://arxiv.org/abs/2003.10555)

---

## 🧠 2020–2021：大模型与 Few-shot 能力

- **2020**：GPT-3  
  📄 [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)

- **2021**：Switch Transformer  
  📄 [Switch Transformers: Scaling to Trillion Parameter Models](https://arxiv.org/abs/2101.03961)

- **2021**：GShard / GLaM  
  📄 [GShard](https://arxiv.org/abs/2006.16668), [GLaM](https://arxiv.org/abs/2112.06905)

- **2021**：鹏城·盘古（PanGu-α）  
  ✅ 中国首个开源千亿级中文大模型，由华为/鹏城实验室发布

---

## 🧾 2022：指令微调与推理能力萌芽

- **InstructGPT**  
  📄 [Training language models to follow instructions](https://arxiv.org/abs/2203.02155)

- **FLAN-T5**  
  📄 [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416)

- **Chain-of-Thought Prompting**  
  📄 [Chain of Thought Prompting Elicits Reasoning](https://arxiv.org/abs/2201.11903)

- **Self-Consistency**  
  📄 [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)

- **FlashAttention**  
  📄 [FlashAttention: Fast and Memory-Efficient Exact Attention](https://arxiv.org/abs/2205.14135)

- **ERNIE 3.0 Titan（百度）**  
  ✅ 中英双语模型（260B），知识增强预训练框架，刷新54项NLP任务

- **GLM（清华）**  
  📄 [GLM: General Language Model Pretraining](https://arxiv.org/abs/2103.10360)  
  ✅ 成为 ChatGLM 系列基础

---

## 🤖 2023：开源模型爆发 + 推理能力升级

- **ChatGPT**  
  📄 [ChatGPT Blog](https://openai.com/blog/chatgpt)

- **Alpaca**  
  📄 [Alpaca Blog](https://crfm.stanford.edu/2023/03/13/alpaca.html)

- **LLaMA（Meta）**  
  ✅ 引爆全球开源社区（Alpaca/Vicuna等均基于此）

- **ChatGLM2-6B（清华智谱）**  
  ✅ 支持32K上下文，中英双语开源对话模型

- **Qwen（阿里通义）**  
  📄 [Qwen Technical Report](https://huggingface.co/Qwen)  
  ✅ 推出Qwen-7B与Qwen-72B（中英最强开源模型之一）

- **Baichuan（百川智能）**  
  📄 [Baichuan 2](https://huggingface.co/baichuan-inc)  
  ✅ 开源 Baichuan-7B/13B，升级 Baichuan2 系列

- **DeepSeek LLM（深度求索）**  
  📄 [DeepSeek Technical Report](https://github.com/deepseek-ai)  
  ✅ 支持128K上下文，中英性能领先

- **Tree-of-Thoughts (ToT)**  
  📄 [Tree of Thoughts](https://arxiv.org/abs/2305.10601)

- **ReAct**  
  📄 [ReAct: Reasoning and Acting](https://arxiv.org/abs/2210.03629)

- **Speculative Decoding**  
  📄 [Speculative Sampling](https://arxiv.org/abs/2302.01318)

- **QLoRA**  
  📄 [QLoRA: Efficient Finetuning](https://arxiv.org/abs/2305.14314)

- **vLLM**  
  📄 [vLLM](https://arxiv.org/abs/2309.06180)

- **VisualGLM（清华）**  
  ✅ 开源图文对话模型

---

## 🎯 2024：推理策略成熟 + 多模态融合

- **Think Twice**  
  📄 [Think Twice](https://arxiv.org/abs/2309.00653)

- **Reflection**  
  📄 [Self-Reflection](https://arxiv.org/abs/2302.12813)

- **GPT-4o**  
  📄 [GPT-4o Blog](https://openai.com/index/gpt-4o/)

- **Claude 3 / Gemini 1.5**  
  📄 [Claude](https://www.anthropic.com/index/introducing-claude), [Gemini](https://deepmind.google/technologies/gemini/)

- **Qwen1.5 系列**  
  ✅ 支持 MoE 架构，推理效率提升75%

- **DeepSeek-VL**  
  ✅ 图文理解 + 文档解析模型（高分辨率图像）

- **Yi（01.AI）**  
  📄 [Yi: Open Foundation Models](https://huggingface.co/01-ai)  
  ✅ Yi-1.5 系列登顶 HuggingFace 开源榜

- **CogVLM（智谱）**  
  ✅ 图文理解能力逼近 GPT-4V

- **Yi-VL（01.AI）**  
  ✅ 多模态模型 Yi-VL 发布

- **Megablocks**  
  📄 [Megablocks: Efficient MoE Inference](https://arxiv.org/abs/2401.08722)

- **DeepSeek-RWKV**  
  ✅ 基于 RNN 架构的百万上下文模型

---

## 🤖 2025：Agent 智能体与持续推理优化

- **LangGraph / AutoGPT**  
  📄 [LangGraph](https://www.langgraph.dev/), [AutoGPT](https://github.com/Torantulino/Auto-GPT)

- **Qwen-Agent（阿里）**  
  ✅ 通义多模态 Agent 框架，支持浏览器、代码解释器等工具调用

- **DeepSeek-Agent**  
  ✅ 具备长期记忆与规划能力（2025年3月开源）

- **OpenAgents（清华）**  
  📄 [OpenAgents](https://github.com/OpenAgents)  
  ✅ 开源真实环境 Agent 平台，支持 200+ 工具调用

---

