"""Spider to srape products from https://www.us.shein.com.

The following categories are supported:
    - Clothing
    - Shoes & Accessories (incl. bags)
"""


import scrapy

from ..items import ProductItem
from ..loaders.shein import SheinLoader


class SheinSpider(scrapy.Spider):
    """Spider to srape products from shein."""

    name = "shein"
    allowed_domains = ["us.shein.com"]
    start_urls = [
        *[f"https://us.shein.com/Men-Clothing-c-2026.html?page={page}" for page in range(1, 41)],
        *[f"https://us.shein.com/category/Men-Shoes-Accessories-sc-00811755.html?page={page}" for page in range(1, 41)],
        *[f"https://us.shein.com/Women-Clothing-c-2030.html?page={page}" for page in range(1, 41)],
        *[f"https://us.shein.com/category/Shoes-Bags-Accs-sc-00828516.htmlpage={page}" for page in range(1, 41)],
    ]
    base_domain = "https://us.shein.com/"
    known_urls = []

    def parse(self, response):
        product_urls = response.css("div.S-product-item__name > a::attr(href)")
        yield from response.follow_all(
            urls=product_urls,
            callback=self.parse_product,
            meta={"playwright": True},
        )

    def parse_product(self, response):
        def get_images(query):
            images_urls = response.css(query).getall()
            images_urls = [image_url.replace("220x293", "900x") for image_url in images_urls]
            images_urls = ["https:" + image_url for image_url in images_urls]
            return images_urls

        product = SheinLoader(item=ProductItem(), response=response)

        product.add_value("shop", self.name)
        product.add_css("product_name", "h1.product-intro__head-name")
        product.add_value("product_url", response.url)
        product.add_value("image_urls", get_images(query="div.product-intro__thumbs-item img::attr(src)"))

        return product.load_item()
