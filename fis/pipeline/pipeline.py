from fis.detection.dummy import DummyDetector
from fis.embedding.timm import TimmModel
from fis.pipeline.base import EncodingPipeline

detector = DummyDetector()
encoder = TimmModel(model_name="swinv2_base_window8_256")
pipeline = EncodingPipeline("dummy_swin_pipe", detection_model=detector, embedding_model=encoder)
