"""Validator for scraped data."""


from schematics.models import Model
from schematics.types import ListType, StringType, URLType


class ProductValidator(Model):
    shop = StringType(required=True)
    product_name = StringType(required=True)
    product_url = URLType(required=True)
    image_urls = ListType(URLType, required=True)
