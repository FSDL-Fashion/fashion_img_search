"""Saves the extracted data."""


import json
import logging
import os

from itemadapter import ItemAdapter

from fis.utils import config as cfg

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
    """Saves extracted data to json file."""

    name = "write_json_lines"

    def open_spider(self, spider):
        os.makedirs(cfg.DIR_SCRAPING, exist_ok=True)
        self.file = open(os.path.join(cfg.DIR_SCRAPING, cfg.FILE_SCRAPING_DATA), "a+")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
