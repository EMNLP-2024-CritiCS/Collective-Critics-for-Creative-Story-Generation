# 📖 CritiCS

Code for Proceedings of EMNLP 2024 paper ["Collective Critics for Creative Story Generation"](https://arxiv.org/abs/2410.02428) Minwook Bae, Hyounghun Kim.

## Prerequisites
To set up your environment to run the code, please follow these steps:

```Shell
conda create -n critics python=3.9
conda activate critics
pip install -r requirements.txt
pip install -e .
```

## Getting Started
To start the application, run the following commands:

```Shell
cd scripts
bash server_load.sh
cd ..
bash app.sh
```
Within the `scripts/output` directory, you can find generated contents including premises, plans, and long stories. The visualization and interaction with the generated content is facilitated through a Streamlit interface.

## GPT-4 Automatic Evaluation
For detailed instructions on running the automatic evaluation scripts, please refer to the separate [automatic](evaluation/automatic.md) located within the `evaluation` folder.

```Shell
cd evalauation
bash run_evalaution.sh
```

## Acknowledgments
Base code is from ["DOC: Improving Long Story Coherence With Detailed Outline Control" paper's code repository](https://github.com/yangkevin2/doc-story-generation), thanks.

## Citation

If you find our results and code useful, please consider citing our paper:

```latex
@misc{min2024Cri,
      title={Collective Critics for Creative Story Generation}, 
      author={Minwook Bae, Hyounghun Kim},
      year={2024},
      eprint={2410.02428},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2410.02428}, 
}
```