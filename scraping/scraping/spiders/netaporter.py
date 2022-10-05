"""Spider to srape products from https://www.net-a-porter.com/en-us/.

The following categories are supported:
    - Clothing
    - Shoes
    - Accessories
    - Bags
"""


import scrapy

from ..items import ProductItem
from ..loaders.netaporter import NetaporterLoader


class NetaporterSpider(scrapy.Spider):
    name = "netaporter"
    allowed_domains = ["net-a-porter.com"]
    start_urls = [
        "https://www.net-a-porter.com/en-us/shop/clothing",
        "https://www.net-a-porter.com/en-us/shop/shoes",
        "https://www.net-a-porter.com/en-us/shop/accessories",
        "https://www.net-a-porter.com/en-us/shop/bags",
    ]
    base_domain = "https://www.net-a-porter.com"
    known_urls = []

    def parse(self, response):
        product_urls = response.css("div.ProductListWithLoadMore52__listingGrid > a::attr(href)")
        yield from response.follow_all(urls=product_urls, callback=self.parse_product)

        yield from response.follow_all(css="a.Pagination7__next::attr(href)", callback=self.parse)

    def parse_product(self, response):
        def get_images(query):
            images_urls = response.css(query).getall()
            images_urls = [images_url for images_url in images_urls if "/variants/" in images_url]
            images_urls = ["https:" + image_url for image_url in images_urls]
            return images_urls

        product = NetaporterLoader(item=ProductItem(), response=response)

        product.add_value("shop", self.name)
        product.add_css("product_name", "p.ProductInformation86__name::text")
        product.add_value("product_url", response.url)
        product.add_value("image_urls", get_images(query="img.Image18__image[itemprop=image]::attr(src)"))

        return product.load_item()
