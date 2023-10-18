# CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation
This repository contains the code implementation for the paper titled "CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation"
<img src="img/pipeline2.png">

## Abstract
Annotated data plays a critical role in Natural Language Processing (NLP) in training models and evaluating their performance. Given recent developments in Large Language Models (LLMs), models such as ChatGPT demonstrate zero-shot capability on many text-annotation tasks, comparable with or even exceeding human annotators. Such LLMs can serve as alternatives for manual annotation, due to lower costs and higher scalability. However, limited work has leveraged LLMs as a complementary annotator nor explored how annotation work is best allocated among humans and LLMs to achieve both quality and cost objectives. We propose CoAnnotating, a novel paradigm for Human-LLM co-annotation of unstructured texts at scale. Under this framework, we utilize uncertainty to estimate LLMs' annotation capability. Our empirical study shows CoAnnotating to be an effective means to allocate work from results on different datasets.

## Usage
This section explains how you can apply human--LLM collaboration for data annotation.
** 1. Prompt LLM several times using different types of prompts.
Detailed implementation in #### **`LLM_Inferencing.py`**
** 2. Postprocess the output and calculate entropy in responses.
Detailed implementation in #### **`Expertise_Estimation.py`**
** 3. Sort instances by entropy in ascending order and allocate top x% for LLM for annotation. Finetune a pretrained classifier using data that is created with human--LLM collaboration.
Detailed implementation in #### **`Work_Allocation.ipynb`**

## Citation and Contact
If you find this repository helpful, please cite our paper.

```
@inproceedings{li2023coannotating,
    title={CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation},
    author={Minzhi Li and Taiwei Shi and Caleb Ziems and Min-Yen Kan and Nancy F. Chen and Zhengyuan Liu and Diyi Yang},
    booktitle={Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing},
    year={2023},
}
```

Feel free to contact Minzhi at li.minzhi@u.nus.edu, if you have any questions about the paper.
