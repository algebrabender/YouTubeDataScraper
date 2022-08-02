from scraper import Scraper
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('api_key')
video_id = "lZRPc1B9zhw"

first_scraper = Scraper(api_key)

first_scraper.scrape(video_id)