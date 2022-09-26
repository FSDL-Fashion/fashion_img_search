from abc import ABC, abstractmethod
from typing import List, Tuple

from PIL import Image


class BaseDetector(ABC):
    """Base class for detection models."""

    @abstractmethod
    def __call__(self, image: Image) -> List[Tuple[int]]:
        """Get embeddings from an image.

        Args:
            image: Image to encode

        Returns:
            Embedding
        """
