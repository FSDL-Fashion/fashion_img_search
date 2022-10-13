import io
from typing import List

import boto3
from PIL import Image

from fis.utils import config as cfg

s3 = boto3.resource("s3")


def list_images_from_bucket(bucket: str = cfg.S3_BUCKET) -> List[str]:
    """List jpeg images from a bucket.

    Args:
        bucket: Name of the bucket. Defaults to cfg.S3_BUCKET.

    Returns:
        List of image names.
    """
    my_bucket = s3.Bucket(bucket)

    images = []
    for _object in my_bucket.objects.all():
        key = _object.key
        if ".jpg" in key:
            images.append(key)

    return images


def read_image_from_s3(key, bucket: str = cfg.S3_BUCKET):

    bucket = s3.Bucket(bucket)
    image = bucket.Object(key)
    img_data = image.get().get("Body").read()

    return Image.open(io.BytesIO(img_data))
