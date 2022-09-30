"""Loader specific to the mrporter spider, for pre- and post-processing the data."""


from itemloaders.processors import Identity, MapCompose, TakeFirst
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags


class NetaporterLoader(ItemLoader):
    default_input_processor = Identity()
    default_output_processor = TakeFirst()

    product_name_in = MapCompose(remove_tags, str.strip)

    image_urls_out = Identity()
