import requests # pip install requests
import json
from datetime import datetime, timedelta
from tqdm import tqdm
from Oauth2_test import oauth2_set
from googleapiclient.discovery import build


class YTstats:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None
        self.video_data = None

    def get_oauth(self):
        CLIENT_SECRET_FILE = 'client_secrets.json'
        SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        ouath2 = oauth2_set(CLIENT_SECRET_FILE, SCOPES)
        credentials = ouath2.local_server_oauth2_set()
        youtube = build("youtube", "v3", credentials = credentials)
        return youtube

    def get_channel_statistics(self):

        youtube = self.get_oauth()
        request = youtube.channels().list(part = "statistics", id = self.channel_id)
        data = request.execute()

        try:
            data = data["items"][0]["statistics"]
        except:
            data = None

        self.channel_statistics = data
        return print(data)

    def get_channel_video_data(self):
        channel_videos = self._get_channel_videos(limit=50)
        print(len(channel_videos))
        
        parts = ["snippet", "statistics", "contentDetails"]
        for video_id in tqdm(channel_videos):
            for i in parts:
                data = self._get_single_video_data(video_id, i)
                channel_videos[video_id].update(data) # append를 사용하지 않고 update를 사용하는 이유는 중복된 데이터 처리가 가능하다.
        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self, video_id, i):            
        try:
            youtube = self.get_oauth()
            request = youtube.videos().list(part = i, id = video_id)
            data = request.execute()
            data = data['items'][0][i]

        except:
            print('API response is Error')
            data = dict()            
        return data

    def _get_channel_videos(self, limit=None):
  
        day_before, day_after = self.get_date()
        day_before = "2022-06-12T15:00:00Z"
        day_after = "2022-06-05T15:00:00Z"
        youtube = self.get_oauth()
        request = youtube.search().list(part = "id", channelId = self.channel_id, publishedBefore = day_before, publishedAfter = day_after)
        if limit is not None and isinstance(limit, int):
            request = youtube.search().list(part = "id", channelId = self.channel_id, publishedBefore = day_before, publishedAfter = day_after, maxResults = str(limit))

        vid, npt = self._get_channel_videos_per_page(request)
        idx = 1
        while(npt is not None and idx < 20):
            next_request = youtube.search().list(part = "id", channelId = self.channel_id, publishedBefore = day_before, publishedAfter = day_after, pageToken= npt)
            next_vid, npt = self._get_channel_videos_per_page(next_request)
            vid.update(next_vid)
            idx += 1
        return vid

    def _get_channel_videos_per_page(self, request):
        
        data = request.execute()
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
        Day_Before = today + "T15:00:00Z"
        Day_After = yesterday + "T15:00:00Z"
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