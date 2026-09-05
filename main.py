import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
from models.classifier import get_pretrained_model
from attacks.fgsm import FGSM
from attacks.pgd import PGD
from utils.visualization import plot_adversarial_examples
import os

class NormalizedModel(nn.Module):
    """
    Wraps model with CIFAR-10 normalization so attack generators can operate 
    directly on unnormalized pixel tensors in [0, 1] with eps in [0, 1].
    """
    def __init__(self, model, mean=(0.4914, 0.4822, 0.4465), std=(0.2470, 0.2435, 0.2616)):
        super().__init__()
        self.model = model
        self.register_buffer('mean', torch.tensor(mean).view(1, 3, 1, 1))
        self.register_buffer('std', torch.tensor(std).view(1, 3, 1, 1))

    def forward(self, x):
        x_norm = (x - self.mean.to(x.device)) / self.std.to(x.device)
        return self.model(x_norm)

def run_experiment():
    # Limit PyTorch CPU threads so processor doesn't overheat or slow down PC
    torch.set_num_threads(4)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"[*] Running Adversarial Benchmark on device: {device} (using 4 CPU threads max)")

    # Load pre-trained ResNet18 model fine-tuned on CIFAR-10 (~95% accuracy)
    base_model = get_pretrained_model("resnet18", pretrained=True, num_classes=10).to(device)
    model = NormalizedModel(base_model).to(device)

    # CIFAR-10 data preprocessing (keep images in [0, 1] for attacks)
    transform = transforms.Compose([
        transforms.ToTensor(),
    ])

    print("[*] Loading CIFAR-10 test dataset...")
    test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)

    # CIFAR-10 Class Labels
    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

    # Initialize Attacks
    fgsm_attack = FGSM(model, eps=8/255)
    pgd_attack = PGD(model, eps=8/255, alpha=2/255, steps=10)

    # Run attack evaluation on first batch
    images, labels = next(iter(test_loader))
    images, labels = images.to(device), labels.to(device)

    # Clean accuracy
    with torch.no_grad():
        outputs = model(images)
        preds = outputs.argmax(dim=1)
        clean_acc = (preds == labels).float().mean().item()

    # FGSM Attack
    adv_fgsm = fgsm_attack.generate(images, labels)
    with torch.no_grad():
        outputs_fgsm = model(adv_fgsm)
        preds_fgsm = outputs_fgsm.argmax(dim=1)
        fgsm_acc = (preds_fgsm == labels).float().mean().item()

    # PGD Attack
    adv_pgd = pgd_attack.generate(images, labels)
    with torch.no_grad():
        outputs_pgd = model(adv_pgd)
        preds_pgd = outputs_pgd.argmax(dim=1)
        pgd_acc = (preds_pgd == labels).float().mean().item()

    print("\n" + "="*50)
    print("      ADVERSARIAL ATTACK BENCHMARK RESULTS      ")
    print("="*50)
    print(f" Clean Accuracy       : {clean_acc * 100:.2f}%")
    print(f" FGSM Accuracy (eps=8/255): {fgsm_acc * 100:.2f}%")
    print(f" PGD Accuracy  (eps=8/255): {pgd_acc * 100:.2f}%")
    print("="*50 + "\n")

    # Generate and save visual comparison plot
    os.makedirs("./results", exist_ok=True)
    plot_adversarial_examples(
        images[0], adv_fgsm[0], 
        classes[labels[0].item()], classes[preds_fgsm[0].item()], 
        eps=8/255, save_path="./results/fgsm_sample.png"
    )
    plot_adversarial_examples(
        images[0], adv_pgd[0], 
        classes[labels[0].item()], classes[preds_pgd[0].item()], 
        eps=8/255, save_path="./results/pgd_sample.png"
    )
    print("[+] Evaluation complete! Plots saved in ./results/")

if __name__ == "__main__":
    run_experiment()
