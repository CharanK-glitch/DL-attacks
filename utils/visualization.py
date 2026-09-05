import matplotlib.pyplot as plt
import torch

def plot_adversarial_examples(orig_img: torch.Tensor, adv_img: torch.Tensor, 
                             orig_label: int, adv_label: int, 
                             eps: float, save_path: str = None):
    """
    Plots the original image, adversarial perturbation (scaled), and perturbed image.
    """
    orig_np = orig_img.permute(1, 2, 0).cpu().numpy()
    adv_np = adv_img.permute(1, 2, 0).cpu().numpy()
    perturbation = adv_np - orig_np

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    
    axes[0].imshow(orig_np)
    axes[0].set_title(f"Original (Class: {orig_label})")
    axes[0].axis('off')

    axes[1].imshow(perturbation * 5 + 0.5) # Scale for visibility
    axes[1].set_title(f"Perturbation (scaled x5)\neps={eps}")
    axes[1].axis('off')

    axes[2].imshow(adv_np)
    axes[2].set_title(f"Adversarial (Class: {adv_label})")
    axes[2].axis('off')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
        print(f"[+] Plot saved to {save_path}")
    plt.close()
