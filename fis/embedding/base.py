from abc import ABC, abstractmethod

from PIL import Image


class BaseEncoder(ABC):
    """Base class for encoders."""

    @abstractmethod
    def __call__(self, image: Image) -> None:
        """Get embeddings from an image.

        Args:
            image: Image to encode

        Returns:
            Embedding
        """
