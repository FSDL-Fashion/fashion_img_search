from typing import Callable, Tuple

import timm
import torch
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform

from fis.embedding.base import BaseEncoder


class TimmModel(BaseEncoder):
    """Base class for timm models."""

    def __init__(self, model_name: str) -> None:
        """Instantiate the model class.

        Args:
            model_name: Name of the model in the timm library.
        """
        model, transform = self._creat_timm_model(model_name=model_name)

        self._model_name = model_name
        self._model = model
        self._transform = transform

    @property
    def model_name(self) -> str:
        return self._model_name

    @staticmethod
    def _creat_timm_model(model_name: str) -> Tuple[torch.nn.Module, Callable]:
        """Create a model and its assitiated configuration.

        Args:
            model_name: Name of the model in the timm library.

        Returns:
            model and transformation function for input images.
        """
        model = timm.create_model(model_name=model_name, pretrained=True, num_classes=0)
        model.eval()

        config = resolve_data_config({}, model=model)
        transform = create_transform(**config)

        return model, transform

    def __call__(self, image: Image) -> torch.Tensor:
        """Get embeddings from an image.

        Args:
            image: Image to encode

        Returns:
            Embedding
        """
        tensor = self._transform(image).unsqueeze(0)  # transform and add batch dimension

        with torch.no_grad():
            embedding = self._model(tensor)

        return embedding
