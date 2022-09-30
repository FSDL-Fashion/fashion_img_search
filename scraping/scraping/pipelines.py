"""Saves the extracted data."""


import json
import logging

from itemadapter import ItemAdapter

logger = logging.getLogger(__name__)


class AddDefaultValuesPipeline:
    """Adds default values to the extracted data."""

    name = "add_default_values"

    def process_item(self, item, spider):
        """Make sure all fields are present in the data returned by the spider, add default values if not."""
        for field in item.fields:
            item.setdefault(field, "NULL")

        return item


class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("items.jsonl", "a+")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
