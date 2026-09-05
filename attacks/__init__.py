"""Adversarial Attack Modules."""
from .fgsm import FGSM
from .pgd import PGD
from .cw import CarliniWagnerL2

__all__ = ['FGSM', 'PGD', 'CarliniWagnerL2']
