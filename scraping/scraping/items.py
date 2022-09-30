"""Generic container for scraped data."""


import scrapy


class ProductItem(scrapy.Item):
    """Format of the scraped items for all spiders."""

    shop = scrapy.Field()
    product_name = scrapy.Field()
    product_url = scrapy.Field()
    image_urls = scrapy.Field()
