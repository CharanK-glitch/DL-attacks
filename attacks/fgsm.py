import torch
import torch.nn as nn

class FGSM:
    """
    Fast Gradient Sign Method (FGSM) Attack
    Exploits the gradient sign of loss with respect to input image.
    """
    def __init__(self, model: nn.Module, eps: float = 8/255):
        self.model = model
        self.eps = eps
        self.loss_fn = nn.CrossEntropyLoss()

    def generate(self, images: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        images = images.clone().detach().to(next(self.model.parameters()).device)
        labels = labels.clone().detach().to(next(self.model.parameters()).device)
        images.requires_grad = True

        outputs = self.model(images)
        loss = self.loss_fn(outputs, labels)
        self.model.zero_grad()
        loss.backward()

        data_grad = images.grad.data
        perturbed_images = images + self.eps * data_grad.sign()
        perturbed_images = torch.clamp(perturbed_images, 0, 1)
        return perturbed_images.detach()
