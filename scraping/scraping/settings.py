from fis.utils import config as cfg

BOT_NAME = "scraping"

SPIDER_MODULES = ["scraping.spiders"]
NEWSPIDER_MODULE = "scraping.spiders"

LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(name)-s]: %(message)s"

USER_AGENT = "Mozilla/5.0 (X11; Linux armv7l) AppleWebKit/537.36 (KHTML, like Gecko) Raspbian Chromium/74.0.3729.157 Chrome/74.0.3729.157 Safari/537.36"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

IMAGES_STORE = cfg.S3_BUCKET_IMAGES

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 60000

ITEM_PIPELINES = {
    "scraping.pipelines.AddDefaultValuesPipeline": 800,
    "scrapy.pipelines.images.ImagesPipeline": 801,
    "scraping.pipelines.JsonWriterPipeline": 802,
}

AUTOTHROTTLE_ENABLED = False
