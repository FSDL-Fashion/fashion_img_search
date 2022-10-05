"""Crawl from multiple spiders.

Example use:
    $ cd scraping
    $ python -m scraping.engine
"""


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from .spiders.mrporter import MrporterSpider
from .spiders.netaporter import NetaporterSpider
from .spiders.shein import SheinSpider


def crawl():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(MrporterSpider)
    process.crawl(NetaporterSpider)
    process.crawl(SheinSpider)
    process.start()


if __name__ == "__main__":
    crawl()
