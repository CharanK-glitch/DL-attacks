import torch
import torch.nn as nn

class PGD:
    """
    Projected Gradient Descent (PGD) Attack
    Iterative multi-step adversarial attack bounded within an L-infinity ball.
    """
    def __init__(self, model: nn.Module, eps: float = 8/255, alpha: float = 2/255, steps: int = 10, random_start: bool = True):
        self.model = model
        self.eps = eps
        self.alpha = alpha
        self.steps = steps
        self.random_start = random_start
        self.loss_fn = nn.CrossEntropyLoss()

    def generate(self, images: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        device = next(self.model.parameters()).device
        images = images.clone().detach().to(device)
        labels = labels.clone().detach().to(device)

        adv_images = images.clone().detach()

        if self.random_start:
            adv_images = adv_images + torch.empty_like(adv_images).uniform_(-self.eps, self.eps)
            adv_images = torch.clamp(adv_images, 0, 1)

        for _ in range(self.steps):
            adv_images.requires_grad = True
            outputs = self.model(adv_images)
            loss = self.loss_fn(outputs, labels)

            self.model.zero_grad()
            loss.backward()

            grad = adv_images.grad.data
            adv_images = adv_images.detach() + self.alpha * grad.sign()
            delta = torch.clamp(adv_images - images, min=-self.eps, max=self.eps)
            adv_images = torch.clamp(images + delta, min=0, max=1).detach()

        return adv_images
