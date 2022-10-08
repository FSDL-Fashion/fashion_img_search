from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DIR_ROOT = Path(__file__).resolve().parent.parent.parent
DIR_DATA = DIR_ROOT / "data"
DIR_SCRAPING = DIR_DATA / "scraping"
DIR_SCRAPING_IMAGES = DIR_SCRAPING / "images"

S3_BUCKET = "s3://fashion-img-search"
S3_BUCKET_IMAGES = f"{S3_BUCKET}/images/"

FILE_SCRAPING_DATA = "items.jsonl"
