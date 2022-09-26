from pymilvus import (
    Collection,
    CollectionSchema,
    DataType,
    FieldSchema,
    connections,
    utility,
)

connections.connect(host="127.0.0.1", port="19530")


def create_milvus_collection(collection_name: str, dim: int) -> Collection:
    """Create a Milvus collection.

    Inspired by https://github.com/milvus-io/bootcamp/blob/master/solutions/reverse_image_search/1_build_image_search_engine.ipynb

    Args:
        collection_name: name of the Milvus collection
        dim: number of dimentions

    Returns:
        Milvus collection
    """
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)

    fields = [
        FieldSchema(
            name="id",
            dtype=DataType.INT64,
            descrition="ids",
            is_primary=True,
            auto_id=False,
        ),
        FieldSchema(
            name="path",
            dtype=DataType.VARCHAR,
            descrition="path to image",
            max_length=500,
            # is_primary=True,
            # auto_id=False,
        ),
        FieldSchema(
            name="embedding",
            dtype=DataType.FLOAT_VECTOR,
            descrition="image embedding vectors",
            dim=dim,
        ),
    ]

    schema = CollectionSchema(fields=fields, description="reverse image search")
    collection = Collection(name=collection_name, schema=schema)

    index_params = {"metric_type": "L2", "index_type": "IVF_FLAT", "params": {"nlist": 2048}}
    collection.create_index(field_name="embedding", index_params=index_params)

    return collection
