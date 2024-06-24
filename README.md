# AutoLP

This is the implementation of the paper [Solving Optimization Problems with Open Source Large Language Model](https://openreview.net/forum?id=4XzGkm1jK0)

## Running the scripts

### Create a virtual environment
```bash
conda env create -f environment.yml
```

### Inference
You can type `python main.py -c [config file]` to run the desired prompting technique. For example, to run chain-of-thought + self-consistency:
```bash
python main.py -c config/prompt/cot_5shot_self_consistency.json
```

## Experimental results

| Technique                                                                  | Accuracy     |
|----------------------------------------------------------------------------|--------------|
| `LLaMA-3-8B-Instruct` + 5-shot                                             | 57.48%       |
| `LLaMA-3-8B-Instruct` + Self-consistency (5-shot, k=15)                    | 60.81%       |
| `LLaMA-3-8B-Instruct` + Chain of Thoughts (5-shot, k=15)                   | **78.15%**   |
| `LLaMA-3-8B-Instruct` + Tree of Thoughts (5-shot, b_1 = 3, b_2 = 5)        | 62.00%       |
| `DeepSeekCoder-7B-Instruct` + Chain of Thoughts (2-shot, k=15)             | 71.50%       |
| `DeepSeekCoder-7B-Instruct` + Tree of Thoughts (2-shot, b_1 = 3, b_2 = 5)  | 61.52%       |
| `DeepSeekCoder-33B-Instruct` + Tree of Thoughts (5-shot, b_1 = 1, b_2 = 5) | 62.95%       |
| Ensemble Strategy                                                          | **80.52%**   |


## Citing
If you use our work in your research, please use the following bibtex

```bibtex
@inproceedings{
nguyen2024technical,
title={Technical Report for {ICML} 2024 Automated Math Reasoning Challenge: Solving Optimization Problems with Open Source Large Language Model},
author={Duc M. Nguyen and Sungahn Ko},
booktitle={AI for Math Workshop @ ICML 2024},
year={2024},
url={https://openreview.net/forum?id=4XzGkm1jK0}
}
```