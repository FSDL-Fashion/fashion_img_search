import os

import gradio as gr
from datasets import load_dataset

from fis.feature_extraction.pipeline.pipeline import factory
from fis.utils.constants import ORGANISATION

# Ugly fix to "OMP: Error #15: Initializing libomp.a, but found libiomp5.dylib already initialized."
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


PIPELINE_NAME = "dummy_swin_pipe"

pipeline = factory.get(PIPELINE_NAME)

DATASET_PATH = os.path.join(ORGANISATION, "dummy_swin_pipe_debug")
dataset = load_dataset(path=DATASET_PATH, split="train")
dataset.add_faiss_index(column="embedding")


def find_most_similar(image):
    image_embeddings = pipeline.encode(image)[0]
    print(image_embeddings)
    print(image_embeddings.shape)

    scores, samples = dataset.get_nearest_examples("embedding", image_embeddings, k=5)


gr.Interface(fn=find_most_similar, inputs="image", outputs="image").launch()
