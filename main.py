import os
from scraper import Scraper
from dotenv import load_dotenv
from data_visualization import show_graphs

load_dotenv()
api_key = os.getenv('api_key')
first_video_id = "lZRPc1B9zhw"

first_scraper = Scraper(api_key)

first_scraper.scrape(first_video_id)

show_graphs()