from typing import List, Tuple

from PIL import Image

from fis.feature_extraction.detection.base import BaseDetector


class DummyDetector(BaseDetector):
    """Dummy detection model."""

    def __call__(self, image: Image) -> List[Tuple[int]]:
        """Return a bounding box with the same size as the image.

        Args:
            image: Image

        Returns:
            Dummy bounding box the same size as the image
        """
        x_min, y_min = 0, 0
        x_max, y_max = image.size

        return [(x_min, y_min, x_max, y_max)]
