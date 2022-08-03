import imp
from YouTubeAPI import YouTubeStats
from datetime import datetime
from database import database_update

class Scraper():
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def scrape(self, video_id) -> None:
        ytstats=YouTubeStats(self.api_key,video_id)
        items=ytstats.get_video_stats()
        for idx,item in enumerate(items):
            print(item["statistics"])
            
            data_dict = {
                "viewCount": item["statistics"]["viewCount"], 
                "likeCount": item["statistics"]["likeCount"], 
                "commentCount": item["statistics"]["commentCount"]
            }

            database_update(data_dict)