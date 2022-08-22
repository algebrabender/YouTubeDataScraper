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
        url_stat = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={self.video_id}&key={self.api_key}'
        url_snippet = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={self.video_id}&key={self.api_key}'
        
        response_stat = self.get_url_response(url_stat)
        data_stat = json.loads(response_stat.text)
        response_snippet = self.get_url_response(url_snippet)
        data_snippet = json.loads(response_snippet.text)

        data_dict = {
            "viewCount": "",
            "likeCount": "",
            "commentCount": ""
        }
        title = ""

        for idx,item in enumerate(data_snippet["items"]):
            #print(item["snippet"]["title"])
            
            title = item["snippet"]["title"]

        for idx,item in enumerate(data_stat["items"]):
            #print(item["statistics"])
            
            data_dict["viewCount"] = item["statistics"]["viewCount"]
            data_dict["likeCount"] = item["statistics"]["likeCount"]
            data_dict["commentCount"] = item["statistics"]["commentCount"]

        return title, data_dict