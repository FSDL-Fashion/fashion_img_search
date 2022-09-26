from abc import ABC, abstractmethod

import torch
from PIL import Image


class BaseEncoder(ABC):
    """Base class for encoders."""

    @abstractmethod
    def __call__(self, image: Image) -> torch.Tensor:
        """Get embeddings from an image.

        Args:
            image: Image to encode

        Returns:
            Embedding
        """
