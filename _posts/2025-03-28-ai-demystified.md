---
layout:     post
title:      "大模型应用初学指南"
subtitle:   "术语定义"
date:       2025-03-28 16:00:00
author:     "Andrew"
catalog: false
header-style: text
tags:
  - Cursor
---


# 技术人的大模型-术语定义

> 引用文章： [技术人的大模型应用初学指南](https://mp.weixin.qq.com/s/NeR1yPdmK6Z1hZVLRSgxrQ)

## 术语定义
AI：Artificial Intelligence的缩写，指“人工智能”，人工智能是指模拟人类智能的计算机系统或软件，使其能够执行诸如学习、推理、问题解决、感知、语言理解等复杂任务。

生成式AI：是一种人工智能技术，能够自动生成新的内容，如文本、图像、音频和视频等。与传统的AI不同，生成式AI不仅能分析和理解数据，还能基于其学习到的信息创造出新的内容。

AIGC：AI Generated Content的缩写，意指由人工智能生成的内容。在算法和数码内容制作领域，AIGC 涉及使用人工智能技术生成各种形式的内容，比如文字、图像、视频、音乐等。

NLP：Natural Language Processing的缩写，指“自然语言处理”，自然语言处理是人工智能的一个子领域，主要研究计算机如何理解、解释和生成人类语言。NLP技术包括文本分析、语言生成、机器翻译、情感分析、对话系统等。

Transformer：一种用于自然语言处理（NLP）任务的深度学习模型，最初由Vaswani等人在2017年的论文中提出。它引入了一种名为“自注意力”（self-attention）的机制，能够有效地处理序列数据，且在许多NLP任务，如机器翻译、文本生成和语言建模中取得了巨大的成功。

BERT：Bidirectional Encoder Representations from Transformers的缩写，是一种自然语言处理（NLP）的预训练模型。它由 Google AI 研究团队于2018年首次提出。BERT 的主要创新在于它使用了双向（即上下文敏感）的Transformer模型来对文本进行编码。

PEFT：Parameter-Efficient Fine-Tuning的缩写，中文高效参数微调，这是一种微调机器学习模型的方法，旨在减少需要更新的参数数量，从而降低计算成本和存储需求，同时保持模型性能。PEFT 技术在大型预训练模型（如 BERT、GPT 等）的下游任务适配中尤为重要，因为直接微调这些模型可能会耗费大量计算资源和时间。

LoRA：Low-Rank Adaptation的缩写，一种用于微调大规模语言模型的一种技术。它通过将模型的权重分解成低秩矩阵来显著减少参数数量和计算开销，从而使得模型在资源受限的环境中也能进行高效的适应性调整。

LLM：Large Language Model的缩写，指“大语言模型”，这类模型是基于机器学习和深度学习技术，特别是自然语言处理（NLP）中的一种技术。大语言模型通过大量的文本数据进行训练，以生成、理解和处理自然语言。一些著名的 LLM 示例包括 OpenAI 的 GPT（Generative Pre-trained Transformer）系列模型，如 GPT-3 和 GPT-4

RAG：Retrieval-Augmented Generation的缩写，指“检索增强生成”，这是一个跨越检索和生成任务的框架，通过先从数据库或文档集合中检索到相关信息，然后利用生成模型（如Transformer模型）来生成最终的输出。目前在技术发展趋势和应用落地上，RAG是工程同学较为值得探索的领域。

Agent：中文叫智能体，一个能独立执行任务和做出决策的实体，在人工智能中，Agent可以是一个机器人，一个虚拟助手，或是一个智能软件系统，它能够通过学习和推理来完成复杂任务。在多Agent系统中，多个独立的Agents相互协作或竞争，以共同解决问题或完成任务。

GPT：Generative Pre-trained Transformer的缩写，指“生成式预训练变换器”，GPT 模型利用大量文本数据进行预训练，然后可以通过微调来执行特定任务，例如语言生成、回答问题、翻译、文本摘要等。

LLaMA：Large Language Model Meta AI的缩写，是由Meta开发的一系列大型自然语言处理模型。这些模型在处理文本生成和理解任务方面表现出色，类似于其他著名的大型语言模型如GPT-3

chatGPT：由 OpenAI 开发的一种基于 GPT（生成预训练变换模型）架构的人工智能聊天机器人。它使用自然语言处理技术，能够理解并生成类似人类的文本回复。可以看做是一种Agent。

Prompt：指的是提供给模型的一段初始文本，用于引导模型生成后续的内容。

Embedding：中文叫嵌入，是一种将高维数据映射到低维空间的技术，但仍尽可能保留原数据的特征和结构。嵌入技术通常用于处理和表示复杂的数据如文本、图像、音乐以及其他高维度的数据类型。