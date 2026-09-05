import torch
import torch.nn as nn
import torchvision.models as models
from huggingface_hub import hf_hub_download
import os

def get_pretrained_cifar10_resnet18() -> nn.Module:
    """
    Loads a pre-trained ResNet-18 model specifically trained on CIFAR-10 (~95% clean accuracy).
    """
    model = models.resnet18()
    model.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1, bias=False)
    model.maxpool = nn.Identity()
    model.fc = nn.Linear(model.fc.in_features, 10)

    try:
        weights_path = hf_hub_download(repo_id="edadaltocg/resnet18_cifar10", filename="pytorch_model.bin")
        state_dict = torch.load(weights_path, map_location="cpu", weights_only=True)
        model.load_state_dict(state_dict)
        print("[+] Loaded pre-trained CIFAR-10 ResNet-18 weights (95%+ accuracy).")
    except Exception as e:
        print(f"[!] Warning: Could not load pre-trained weights ({e}). Using uninitialized model.")

    model.eval()
    return model

def get_pretrained_model(model_name: str = "resnet18", pretrained: bool = True, num_classes: int = 10) -> nn.Module:
    """
    Loads a vision model. If model_name is 'resnet18' and pretrained is True,
    loads the pre-trained CIFAR-10 model.
    """
    model_name = model_name.lower()
    if model_name == "resnet18":
        if pretrained and num_classes == 10:
            return get_pretrained_cifar10_resnet18()
        else:
            model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT if pretrained else None)
            model.fc = nn.Linear(model.fc.in_features, num_classes)
            model.eval()
            return model
    else:
        raise ValueError(f"Unsupported model architecture: {model_name}")
