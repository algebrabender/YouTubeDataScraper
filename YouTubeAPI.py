import requests
import json

class YouTubeStats():
    def __init__(self, api_key, video_id) -> None:
        self.api_key = api_key
        self.video_id = video_id

    def get_url_response(self, url) -> json:
        i = 0;
        while i < 3:
            try:
                res = requests.get(url, timeout=5)
                return res
            except (requests.exceptions.ChunkedEncodingError, requests.ConnectionError) as e:
                print("There is a error: %s" % e)
                i += 1
    
    def get_video_stats(self):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={self.video_id}&key={self.api_key}'
        response = self.get_url_response(url)
        data = json.loads(response.text)
        return data["items"]