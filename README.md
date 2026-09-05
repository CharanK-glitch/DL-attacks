# DL-attacks: Deep Learning Adversarial Robustness & Attack Framework

`DL-attacks` is a PyTorch-based framework designed for evaluating the robustness of deep neural networks under adversarial attacks.

## 🚀 Implemented Attacks
- **FGSM (Fast Gradient Sign Method)**: Single-step gradient perturbation attack ($L_\infty$).
- **PGD (Projected Gradient Descent)**: Multi-step iterative attack bounded within an $L_\infty$ ball.
- **C&W (Carlini & Wagner)**: $L_2$ Optimization-based adversarial attack.

## 📦 Directory Structure
```text
DL-attacks/
├── models/         # Vision model loaders and definitions
├── attacks/        # FGSM, PGD, and CW attack algorithms
├── utils/          # Visualization tools and perturbation plots
├── requirements.txt
├── main.py         # Benchmark and experiment runner script
└── README.md
```

## 🛠️ Quickstart
```bash
cd DL-attacks
pip install -r requirements.txt
python main.py
```
