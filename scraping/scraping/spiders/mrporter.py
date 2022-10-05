"""Spider to srape products from https://www.mrporter.com/en-us/.

The following categories are supported:
    - Clothing
    - Shoes
    - Accessories (incl. bags)
"""


import scrapy

from ..items import ProductItem
from ..loaders.mrporter import MrportertLoader


class MrporterSpider(scrapy.Spider):
    """Spider to srape products from mrporter."""

    name = "mrporter"
    allowed_domains = ["mrporter.com"]
    start_urls = [
        "https://mrporter.com/en-us/mens/clothing",
        "https://mrporter.com/en-us/mens/shoes",
        "https://mrporter.com/en-us/mens/accessories",
    ]
    base_domain = "https://www.mrporter.com"
    known_urls = []

    def parse(self, response):
        product_urls = response.css("div.ProductListWithLoadMore52__listingGrid > a::attr(href)")
        yield from response.follow_all(urls=product_urls, callback=self.parse_product)

        yield from response.follow_all(css="a.Pagination7__next::attr(href)", callback=self.parse)

    def parse_product(self, response):
        def get_images(query):
            images = response.css(query).getall()
            images_urls = [image for image in images if "//cache" in image]
            images_urls_no_dupplicates = list(dict.fromkeys(images_urls))
            images_urls_with_scheme = ["https:" + image for image in images_urls_no_dupplicates]
            return images_urls_with_scheme

        product = MrportertLoader(item=ProductItem(), response=response)

        product.add_value("shop", self.name)
        product.add_css("product_name", "p.ProductInformation84__name::text")
        product.add_value("product_url", response.url)
        product.add_value("image_urls", get_images(query="img.Image18__image[itemprop=image]::attr(src)"))

        return product.load_item()
