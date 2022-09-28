import requests # pip install requests
import json
from datetime import datetime
from datetime import timedelta

class Youtube_video_data:

    def __init__(self):
        self.api_key = 'AIzaSyDPafGCd3dlAzfH9Wa1vDDWirchypWbGdg'
        self.dateDict = {0: '(월)',1: '(화)',2: '(수)',3: '(목)',4: '(금)',5: '(토)',6: '(일)'}
        self.video_id = None
        self.data = []
        self.date = None
        self.start_time = None
        self.title = None
        self.video_duration = None
        
    def get_date(self, publishedAt):
        try:
            publishedAt = publishedAt.replace('T',' ').replace('Z','') # 문자 제거
            logdate = datetime.strptime(publishedAt, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9) # UTC시간에서 한국시간 계산
            # day_week = self.dateDict[logdate.weekday()] # 딕셔너리로 요일 구하기
            logdate = str(logdate) # 인티저를 스트링으로 타입변환
            # logdate = logdate.replace('-','.') # '-' 문자를 '.'으로 대체
            
            self.date = logdate[0:10]
            self.start_time = logdate[11:16]

        except:
            print('get_date is Error!')

    def get_video_duration(self, duration):
        try:
            day_time = duration.split('T')
            day_duration = day_time[0].replace('P', '')
            day_list = day_duration.split('D')
            if len(day_list) == 2:
                day = int(day_list[0]) * 60 * 60 * 24
                day_list = day_list[1]
            else:
                day = 0
                day_list = day_list[0]
            hour_list = day_time[1].split('H')
            if len(hour_list) == 2:
                hour = int(hour_list[0]) * 60 * 60
                hour_list = hour_list[1]
            else:
                hour = 0
                hour_list = hour_list[0]
            minute_list = hour_list.split('M')
            if len(minute_list) == 2:
                minute = int(minute_list[0]) * 60
                minute_list = minute_list[1]
            else:
                minute = 0
                minute_list = minute_list[0]
            second_list = minute_list.split('S')
            if len(second_list) == 2:
                second = int(second_list[0])
            else:
                second = 0

            sum_seconds = day + hour + minute + second
            self.video_duration = str(timedelta(seconds = sum_seconds))
        except:
            print("get_video_duration is Error!")

    def get_video_snippet(self):
        try:
            url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={self.video_id}&key={self.api_key}"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            self.title = data['items'][0]['snippet']['title']
            publishedAt = data['items'][0]['snippet']['publishedAt']
            self.get_date(publishedAt)

        except:
            print('video_id is Error(get_video_snippet)')

    def get_video_contentDetails(self):
        try:
            url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={self.video_id}&key={self.api_key}"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            duration = data['items'][0]['contentDetails']['duration']
            self.get_video_duration(duration)
            
        except:
            print('video_id is Error(get_video_contentDetails)')
    
    def get_youtube_data(self, Youtube_url):

        if Youtube_url[0:16] == 'https://youtu.be':
            self.video_id = Youtube_url.rsplit('/')[3]
        elif Youtube_url[0:23] == 'https://www.youtube.com' :
            print(Youtube_url.rsplit('=')[1])
            self.video_id = Youtube_url.rsplit('=')[1]
        else :
            print("Youtube url is invalid")
            return

        self.get_video_snippet()
        self.get_video_contentDetails()

        self.data.append(self.date)
        self.data.append(self.start_time)
        self.data.append(self.video_duration)
        self.data.append(self.title)

        return self.data