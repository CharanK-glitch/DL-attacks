import torch
import torch.nn as nn

class CarliniWagnerL2:
    """
    Carlini & Wagner L2 Optimization Attack
    Targeted / Untargeted optimization based adversarial attack.
    """
    def __init__(self, model: nn.Module, c: float = 1e-4, kappa: float = 0, steps: int = 1000, lr: float = 0.01):
        self.model = model
        self.c = c
        self.kappa = kappa
        self.steps = steps
        self.lr = lr

    def generate(self, images: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        device = next(self.model.parameters()).device
        images = images.clone().detach().to(device)
        labels = labels.clone().detach().to(device)

        # Convert images to arctanh space for unconstrained optimization
        w = torch.zeros_like(images, requires_grad=True, device=device)
        optimizer = torch.optim.Adam([w], lr=self.lr)

        for _ in range(self.steps):
            adv_images = 0.5 * (torch.tanh(w) + 1)
            outputs = self.model(adv_images)

            # Untargeted loss formulation
            one_hot_labels = torch.nn.functional.one_hot(labels, num_classes=outputs.shape[1]).float()
            real = torch.sum(one_hot_labels * outputs, dim=1)
            other = torch.max((1 - one_hot_labels) * outputs - (one_hot_labels * 10000), dim=1)[0]
            
            loss_cw = torch.clamp(real - other + self.kappa, min=0)
            loss_dist = torch.sum((adv_images - images) ** 2, dim=[1, 2, 3])
            
            total_loss = torch.mean(loss_dist + self.c * loss_cw)

            optimizer.zero_grad()
            total_loss.backward()
            optimizer.step()

        return (0.5 * (torch.tanh(w) + 1)).detach()
