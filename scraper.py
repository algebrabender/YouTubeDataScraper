from YouTubeAPI import YouTubeStats
from database import database_update, database_update_video_ids

class Scraper():
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def scrape(self, video_id) -> None:
        ytstats=YouTubeStats(self.api_key,video_id)

        title, data_dict = ytstats.get_video_stats()
        # print(data_dict)
        database_update(title, data_dict)
        database_update_video_ids(title, video_id)

        return title