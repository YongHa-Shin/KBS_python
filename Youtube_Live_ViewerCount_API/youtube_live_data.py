import requests # pip install requests
import json
from datetime import datetime, timedelta


class YT_Live:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.type = "video"
        self.event_type = "live"

    def get_search_snippet(self):
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={self.channel_id}&key={self.api_key}&type={self.type}&event_type={self.event_type}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        sum = 0

        try:
            if int(data["pageInfo"]["resultsPerPage"]) == 0 :
                return "LiveEvent is not exist"

            else :
                live_event_count = int(data["pageInfo"]["resultsPerPage"])
                for i in range(live_event_count) :
                    video_id = data["items"][i]["id"]["videoId"]
                    sum += int(self.get_video_concurrentViewer(video_id))
                return sum
        except:
            sum = None
            return sum
    
    def get_video_concurrentViewer(self, video_id):
        url = f"https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&key={self.api_key}&id={video_id}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)

        try:
            data = data["items"][0]["liveStreamingDetails"]["concurrentViewers"]

        except:
            data = None    

        return data