from fis.feature_extraction.detection.base import BaseDetector
from fis.feature_extraction.embedding.base import BaseEncoder
from fis.feature_extraction.pipeline.base import EncodingPipeline


class PipelineFactory:
    """Factory method for encoding pipelines.

    Example use:
        >>> from fis.feature_extraction.pipeline.factory import PipelineFactory
        >>> factory = PipelineFactory()
        >>> factory.register_pipeline(
        ...     name="example_pipeline",
        ...     detection_model=BaseDetector(),
        ...     embedding_model=BaseEncoder()
        ... )
        >>> pipeline = factory.get('example_pipeline')
    """

    def __init__(self):
        """Instantiate factory object."""
        self._pipelines = {}

    def register_pipeline(self, name: str, detection_model: BaseDetector, embedding_model: BaseEncoder) -> None:
        """Register a new pipeline to the factory.

        Args:
            name: Name of the pipeline to create.
            detection_model: Instance of a BaseDetector object.
            embedding_model: Instance of a BaseEncoder object.
        """
        pipeline = EncodingPipeline(name=name, detection_model=detection_model, embedding_model=embedding_model)
        self._pipelines[name] = pipeline

    def get(self, name: str) -> EncodingPipeline:
        """Get a pipeline from its name.

        Args:
            name: Name of the pipeline to get.

        Raises:
            ValueError: If no pipeline has been registered with the given name.

        Returns:
            Encoding pipeline.
        """
        pipeline = self._pipelines.get(name)
        if not pipeline:
            raise ValueError(name)

        return pipeline
