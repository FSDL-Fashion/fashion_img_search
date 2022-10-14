import os
from typing import List

import gradio as gr
import numpy as np
from datasets import load_dataset
from PIL.Image import Image as Img

from fis.feature_extraction.pipeline.pipeline import factory
from fis.utils.constants import ORGANISATION
from fis.utils.s3 import read_image_from_s3

# Ugly fix of "OMP: Error #15: Initializing libomp.a, but found libiomp5.dylib already initialized."
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


PIPELINE_NAME = "dummy_swin_pipe"

pipeline = factory.get(PIPELINE_NAME)

DATASET_PATH = os.path.join(ORGANISATION, "dummy_swin_pipe_debug")
dataset = load_dataset(path=DATASET_PATH, split="train")
dataset.add_faiss_index(column="embedding")


def find_most_similar(image: np.ndarray) -> List[Img]:
    image_embeddings = pipeline.encode(image)[0]

    scores, samples = dataset.get_nearest_examples("embedding", image_embeddings, k=5)

    images = []
    for image_path in samples["path"]:
        image = read_image_from_s3(image_path)
        images.append(image)

    return images


description = """
Upload an image, and see the **top 5** most similar items in our database.

Supported categories are clothing, shoes and bags.
"""

images = [image for image in os.listdir("./images") if ".jpeg" in image]
images = [os.path.join("./images", image) for image in images]

gr.Interface(
    title="Fashion image search",
    description=description,
    fn=find_most_similar,
    inputs="image",
    outputs=["image" for i in range(5)],
    examples=images,
    cache_examples=True,
).launch()
