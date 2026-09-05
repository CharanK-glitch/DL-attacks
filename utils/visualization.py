import matplotlib.pyplot as plt
import numpy as np
import torch

def plot_adversarial_examples(orig_img: torch.Tensor, adv_img: torch.Tensor, 
                             orig_label: str, adv_label: str, 
                             eps: float = None, save_path: str = None):
    """
    Plots the original image, adversarial perturbation (scaled x5), and perturbed image.
    """
    orig_np = torch.clamp(orig_img, 0, 1).permute(1, 2, 0).cpu().numpy()
    adv_np = torch.clamp(adv_img, 0, 1).permute(1, 2, 0).cpu().numpy()
    perturbation = np.clip(adv_np - orig_np, -1, 1)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    axes[0].imshow(orig_np)
    axes[0].set_title(f"Original\n({orig_label})", fontsize=12, fontweight='bold')
    axes[0].axis('off')

    eps_str = f"\neps={eps:.4f}" if eps is not None else ""
    axes[1].imshow(np.clip(perturbation * 5 + 0.5, 0, 1)) # Scale for visibility
    axes[1].set_title(f"Perturbation (scaled x5){eps_str}", fontsize=12, fontweight='bold')
    axes[1].axis('off')

    axes[2].imshow(adv_np)
    axes[2].set_title(f"Adversarial\n({adv_label})", fontsize=12, fontweight='bold', color='red' if orig_label != adv_label else 'green')
    axes[2].axis('off')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[+] Plot saved to {save_path}")
    plt.close()

def plot_accuracy_vs_epsilon(epsilons: list, fgsm_accs: list, pgd_accs: list, save_path: str = "./results/accuracy_vs_epsilon.png"):
    """
    Plots Accuracy vs. Perturbation Strength (Epsilon) robustness curve.
    """
    plt.figure(figsize=(9, 5.5))
    eps_labels = [f"{e:.3f}" if isinstance(e, float) else str(e) for e in epsilons]
    
    plt.plot(eps_labels, [a * 100 for a in fgsm_accs], 'o-', label='FGSM Attack', color='#e74c3c', linewidth=2.5, markersize=8)
    plt.plot(eps_labels, [a * 100 for a in pgd_accs], 's--', label='PGD Attack (10-step)', color='#8e44ad', linewidth=2.5, markersize=8)

    plt.title("Model Accuracy vs. Perturbation Strength (Epsilon)", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Perturbation Bound (Epsilon ε)", fontsize=12, labelpad=10)
    plt.ylabel("Classification Accuracy (%)", fontsize=12, labelpad=10)
    plt.ylim(-5, 105)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=11, loc='upper right')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[+] Accuracy vs. Epsilon curve saved to {save_path}")
    plt.close()

def plot_adversarial_grid(images: torch.Tensor, adv_fgsm: torch.Tensor, adv_pgd: torch.Tensor,
                          labels: torch.Tensor, preds_fgsm: torch.Tensor, preds_pgd: torch.Tensor,
                          classes: tuple, num_samples: int = 4, save_path: str = "./results/adversarial_grid.png"):
    """
    Plots a multi-sample grid comparing Original, FGSM, and PGD images with predicted labels.
    """
    num_samples = min(num_samples, len(images))
    fig, axes = plt.subplots(num_samples, 3, figsize=(10, 3.2 * num_samples))

    if num_samples == 1:
        axes = [axes]

    for idx in range(num_samples):
        orig_img = torch.clamp(images[idx], 0, 1).permute(1, 2, 0).cpu().numpy()
        fgsm_img = torch.clamp(adv_fgsm[idx], 0, 1).permute(1, 2, 0).cpu().numpy()
        pgd_img = torch.clamp(adv_pgd[idx], 0, 1).permute(1, 2, 0).cpu().numpy()

        true_cls = classes[labels[idx].item()]
        fgsm_cls = classes[preds_fgsm[idx].item()]
        pgd_cls = classes[preds_pgd[idx].item()]

        axes[idx][0].imshow(orig_img)
        axes[idx][0].set_title(f"True: {true_cls}", fontsize=11, fontweight='bold')
        axes[idx][0].axis('off')

        axes[idx][1].imshow(fgsm_img)
        fgsm_color = 'red' if fgsm_cls != true_cls else 'green'
        axes[idx][1].set_title(f"FGSM: {fgsm_cls}", fontsize=11, fontweight='bold', color=fgsm_color)
        axes[idx][1].axis('off')

        axes[idx][2].imshow(pgd_img)
        pgd_color = 'red' if pgd_cls != true_cls else 'green'
        axes[idx][2].set_title(f"PGD: {pgd_cls}", fontsize=11, fontweight='bold', color=pgd_color)
        axes[idx][2].axis('off')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[+] Adversarial Grid comparison saved to {save_path}")
    plt.close()

def plot_confidence_bar(clean_probs: torch.Tensor, fgsm_probs: torch.Tensor, pgd_probs: torch.Tensor,
                        classes: tuple, true_idx: int, save_path: str = "./results/confidence_bar.png"):
    """
    Plots a class prediction confidence bar chart comparing Clean vs FGSM vs PGD probability outputs.
    """
    x = np.arange(len(classes))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 5))
    
    clean_p = torch.softmax(clean_probs, dim=0).cpu().numpy()
    fgsm_p = torch.softmax(fgsm_probs, dim=0).cpu().numpy()
    pgd_p = torch.softmax(pgd_probs, dim=0).cpu().numpy()

    ax.bar(x - width, clean_p, width, label='Clean Image', color='#2ecc71')
    ax.bar(x, fgsm_p, width, label='FGSM Perturbed', color='#e67e22')
    ax.bar(x + width, pgd_p, width, label='PGD Perturbed', color='#e74c3c')

    ax.set_title(f"Class Prediction Probability Distribution (True Class: '{classes[true_idx]}')", fontsize=13, fontweight='bold')
    ax.set_xlabel("CIFAR-10 Classes", fontsize=11, labelpad=8)
    ax.set_ylabel("Softmax Probability", fontsize=11, labelpad=8)
    ax.set_xticks(x)
    ax.set_xticklabels(classes, rotation=30, ha='right')
    ax.set_ylim(0, 1.05)
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)
    ax.legend(fontsize=11)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"[+] Prediction confidence bar plot saved to {save_path}")
    plt.close()
