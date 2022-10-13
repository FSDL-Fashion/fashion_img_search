from typing import Any, List

import numpy as np
import torch
from PIL import Image
from PIL.Image import Image as Img

from fis.feature_extraction.detection.base import BaseDetector
from fis.feature_extraction.embedding.base import BaseEncoder


class EncodingPipeline:
    """Apply the detection and embedding models to an image."""

    def __init__(self, name: str, detection_model: BaseDetector, embedding_model: BaseEncoder) -> None:
        """Initialize the encoding pipeline.

        Args:
            name: Name of the pipeline.
            detection_model: Model used to detect the fashion items in the images.
            embedding_model: Model used to generate embeddings for each detected item.
        """
        self._name = name
        self._detection_model = detection_model
        self._embedding_model = embedding_model

    def encode(self, image: str) -> List[torch.Tensor]:
        """Encode each item from an image into a embedding.

        Args:
            image: path to the image.

        Returns:
            Embeddings for each detected item in the image.
        """
        image = self._load_images(image)
        bboxes = self._detection_model(image)
        items = self._crop_images(image, bboxes)

        embeddings = []
        for item in items:
            embedding = self._embedding_model(item)
            embeddings.append(embedding)

        return embeddings

    def _load_images(self, image: Any) -> Img:
        """Read an image from disk.

        Args:
            image: Path to the image on disk.

        Raises:
            TypeError: if the type of image is incorrect.

        Returns:
            PIL Image.
        """
        if isinstance(image, Img):
            pass
        elif isinstance(image, np.ndarray):
            image = Image.fromarray(image)
        elif isinstance(image, str):
            image = Image.open(image)
        else:
            raise TypeError(f"Unknown type for image: {type(image)}")

        return image

    def _crop_images(self, image, bboxes) -> List[Img]:
        """Crop an image based on bounding boxes.

        Args:
            image: Image to crop items from.
            bboxes: Bounding box containing an item.

        Returns:
            List of cropped images.
        """
        items = []
        for bbox in bboxes:
            cropped_image = image.crop(bbox)
            items.append(cropped_image)

        return items
