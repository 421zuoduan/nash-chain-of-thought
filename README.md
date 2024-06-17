# Nash Chain-of-Thought (CoT)

### Description: This is the official codebase for Nash CoT

### What's CoT

(If you have no related-background knowledge about CoT, please read these papers [1,2,3] first) CoT is a *step-by-step* manner inference approach. This approach is composed of two steps. Step1: Generating rationals 

Here, we provide single case for CoT:


### The framework of Nash CoT:

### Configuration

### How to run our code?

'''
sh run_nash_cot.sh data_setname random_seed tokenizer_path model_path
'''

### If you utilize our codebase, please cite below:

```c
@article{,
title={Nash CoT: Multi-Path Inference with Preference Equilibrium}, 
author={Ziqi Zhang and Cunxiang Wang and Xiong Xiao and Yue Zhang and Donglin Wang},
year={2024},
eprint={},
archivePrefix={arXiv},
}
```

### Thanks 

We utilize these models: GLM, MIS-7B, self-consistency, Auto-CoT for evaluation.

Our codebase is modified from the codebase of Automatic CoT

Addtionally, thanks my collerberator: Cunxiang Wang

This reseach is supported by milab.

### *Reference*

[1] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, Denny Zhou. 2022. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. Preprint. arXiv: 2201.11903.

[2] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou. 2022. Self-Consistency Improves Chain of Thought Reasoning in Language Models. Preprint. arXiv: 2203.11171.

[3] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou. 2022. Self-Consistency Improves Chain of Thought Reasoning in Language Models. Preprint. arXiv: 2203.11171.

# Collaberation 

If you can find out any kinds of new usages of Nash CoT, we are welcomed to be contacted and supplyment new emergence experimental results!
