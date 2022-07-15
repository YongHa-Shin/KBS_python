import requests # pip install requests
import json
from datetime import datetime, timedelta
from tqdm import tqdm

class YTstats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_channel_statistics(self):
        url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}"
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data["items"][0]["statistics"]
        except:
            data = None
        self.channel_statistics = data
        return data

    def get_channel_video_data(self):
        channel_videos = self._get_channel_videos(limit=50)
        print(len(channel_videos))
        
        parts = ["snippet", "statistics", "contentDetails"]
        for video_id in tqdm(channel_videos):
            for part in parts:
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data) # append를 사용하지 않고 update를 사용하는 이유는 중복된 데이터 처리가 가능하다.
        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self, video_id, part):            
        try:
            url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            data = data['items'][0][part]
        except:
            print('API response is Error')
            data = dict()            
        return data

    #publishedBefore=2022-03-21T00:00:00Z&publishedAfter=2022-03-20T00:00:00Z
    def _get_channel_videos(self, limit=None):
        Day_Before, Day_After = self.get_date()
        url = f"https://www.googleapis.com/youtube/v3/search?channelId={self.channel_id}&key={self.api_key}&part=id" + Day_Before + Day_After

        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)
  
        vid, npt = self._get_channel_videos_per_page(url)

        idx = 1
        while(npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, npt = self._get_channel_videos_per_page(nexturl)
            vid.update(next_vid)
            idx += 1
        return vid

    def _get_channel_videos_per_page(self, url):
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        #print(data)
        channel_videos = dict()
        if 'items' not in data:
            return channel_videos, None
        
        item_data = data['items']
        nextPageToken = data.get("nextPageToken", None)
        for item in item_data:
            try:
                kind = item['id']['kind']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    channel_videos[video_id] = dict()
            except KeyError:
                print("error")
        return channel_videos, nextPageToken

    def get_date(self):
        today = str(datetime.today() - timedelta(1))
        today = today[0:10]
        yesterday = str(datetime.today() - timedelta(2))
        yesterday = yesterday[0:10]
        Day_Before = "&publishedBefore=" + today + "T15:00:00Z"
        Day_After = "&publishedAfter=" + yesterday + "T15:00:00Z"
        return Day_Before, Day_After
        
    def dump(self):
        try:
            if self.channel_statistics is None or self.video_data is None:
                print('data is none')
                return

            fused_data = {self.channel_id: {"channel_statistics": self.channel_statistics, "video_data": self.video_data}}
            
            today = str(datetime.today())
            today = today[0:10]
            
            channel_title = self.video_data.popitem()[1].get('channelTitle', self.channel_id) 
            # channel_title = "KBS News" # TODO: get channel name from data
            channel_title = channel_title.replace(" ","_").lower()
            file_name = today+ "_" + channel_title + '.json'
            with open(file_name, 'w') as f:
                json.dump(fused_data, f, indent = 4)

            print('file dumped')
        except:
            print('file dump is failed')