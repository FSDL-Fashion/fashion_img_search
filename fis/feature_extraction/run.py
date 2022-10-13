import pandas as pd
from datasets import Dataset
from tqdm import tqdm

from fis.feature_extraction.pipeline.pipeline import factory
from fis.utils.constants import ORGANISATION
from fis.utils.s3 import list_images_from_bucket, read_image_from_s3


def make_dataset(pipeline_name: str) -> Dataset:
    print("Listing images from S3...")
    images = list_images_from_bucket()
    images = images[:100000]
    print(f"{len(images)} images to process.")

    pipeline = factory.get(pipeline_name)
    data = []

    print("Encoding images...")
    for image_name in tqdm(images):
        image = read_image_from_s3(image_name)
        embeddings = pipeline.encode(image)

        for embedding in embeddings:
            image_data = {
                "path": image_name,
                "embedding": embedding,
            }

            data.append(image_data)

    df = pd.DataFrame(data)
    dataset = Dataset.from_pandas(df)

    return dataset


def upload_dataset(dataset: Dataset, pipeline_name: str) -> None:
    print("Uploading dataset...")
    repo_id = "{}/{}".format(ORGANISATION, pipeline_name)
    dataset.push_to_hub(repo_id=repo_id)


def main():
    pipeline_name = "dummy_swin_pipe"
    dataset = make_dataset(pipeline_name=pipeline_name)
    upload_dataset(dataset=dataset, pipeline_name=pipeline_name)


if __name__ == "__main__":
    main()
