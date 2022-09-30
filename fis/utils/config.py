import os

from dotenv import load_dotenv


load_dotenv()

DIR_ROOT = str(os.getenv("PROJECT_ROOT"))
DIR_DATA = os.path.join(DIR_ROOT, "data")
