import os
import urllib.request
import zipfile

from fis.utils.config import DIR_DATA

# Download from S3
RAW_TRAIN_IMAGES = "https://s3.amazonaws.com/ifashionist-dataset/images/train2020.zip"
RAW_VAL_IMAGES = "https://s3.amazonaws.com/ifashionist-dataset/images/val_test2020.zip"
RAW_TRAIN_ANNOTATIONS = "https://s3.amazonaws.com/ifashionist-dataset/annotations/instances_attributes_train2020.json"
RAW_VAL_ANNOTATIONS = "https://s3.amazonaws.com/ifashionist-dataset/annotations/instances_attributes_val2020.json"

# to local disk
TRAIN_ANNOTATIONS = "train.json"
VAL_ANNOTATIONS = "val.json"


def download(url: str, target: str) -> None:
    """Download image and annotations.

    Args:
        url: url to download from.
        target: file or directory to download to.
    """
    print(f"Downloading from {url}")

    # Images
    if url.split(".")[-1] == "zip":
        path, _ = urllib.request.urlretrieve(url=url)  # noqa
        with zipfile.ZipFile(path, "r") as f:
            f.extractall(target)

        os.remove(path)

    # Annotations
    else:
        urllib.request.urlretrieve(url=url, filename=target)  # noqa


def download_fashionpedia(destination_dir: str = DIR_DATA) -> None:
    """Download the Fashionpedia dataset.

    Args:
        destination_dir: directory where the dataset will be saved.
    """
    os.makedirs(destination_dir, exist_ok=True)

    download(url=RAW_TRAIN_ANNOTATIONS, target=os.path.join(destination_dir, TRAIN_ANNOTATIONS))
    download(url=RAW_VAL_ANNOTATIONS, target=os.path.join(destination_dir, VAL_ANNOTATIONS))

    download(url=RAW_TRAIN_IMAGES, target=destination_dir)
    download(url=RAW_VAL_IMAGES, target=destination_dir)


if __name__ == "__main__":
    download_fashionpedia()
