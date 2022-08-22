import os
from scraper import Scraper
from dotenv import load_dotenv
from gui import gui

load_dotenv()
api_key = os.getenv('api_key')

first_scraper = Scraper(api_key)

gui(first_scraper)