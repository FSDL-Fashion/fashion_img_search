from fis.feature_extraction.detection.dummy import DummyDetector
from fis.feature_extraction.embedding.timm import TimmModel
from fis.feature_extraction.pipeline.factory import PipelineFactory

factory = PipelineFactory()

factory.register_pipeline(
    name="dummy_swin_pipe",
    detection_model=DummyDetector(),
    embedding_model=TimmModel(model_name="swinv2_base_window8_256"),
)
