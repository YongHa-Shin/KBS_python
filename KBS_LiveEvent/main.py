import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests # pip install requests
import json
from datetime import datetime
from datetime import timedelta

dateDict = {0: '(월)',1: '(화)',2: '(수)',3: '(목)',4: '(금)',5: '(토)',6: '(일)'}

def get_date(publishedAt):

    publishedAt = publishedAt.replace('T',' ').replace('Z','') # 문자 제거
    logdate = datetime.strptime(publishedAt, '%Y-%m-%d %H:%M:%S') - timedelta(hours=-9) # UTC시간에서 한국시간 계산
    day_week = dateDict[logdate.weekday()] # 딕셔너리로 요일 구하기
    logdate = str(logdate) # 인티저를 스트링으로 타입변환
    logdate = logdate.replace('-','.') # '-' 문자를 '.'으로 대체
    date = logdate[0:10] + '.' + day_week # 날짜와 요일을 합친다

    return date

# 라이브이벤트_비디오아이디
f = open('현장영상_비디오아이디_추가.txt', 'r')
data = f.read().splitlines()

# Youtube Video ID data 중복처리를 위한 list -> dict, dict -> list
data_dict = dict.fromkeys(data)
data = list(data_dict)

# Youtubue Video data를 저장할 수 있는 파일 열기
f = open('현장영상_리스트_추가.txt', 'w')

for i in data:
    url_statistics =  f"https://www.googleapis.com/youtube/v3/videos?key=AIzaSyDPafGCd3dlAzfH9Wa1vDDWirchypWbGdg&part=statistics&id={i}"
    json_url_statistics = requests.get(url_statistics)
    f_data_1 = json.loads(json_url_statistics.text)

    url_snippet =  f"https://www.googleapis.com/youtube/v3/videos?key=AIzaSyDPafGCd3dlAzfH9Wa1vDDWirchypWbGdg&part=snippet&id={i}"
    json_url_snippet = requests.get(url_snippet)
    f_data_2 = json.loads(json_url_snippet.text)

    if json_url_statistics.status_code == 200 and json_url_snippet.status_code == 200 :
        try:
            viewCount = f_data_1['items'][0]['statistics']['viewCount']
            likeCount = f_data_1['items'][0]['statistics']['likeCount']
            commentCount = f_data_1['items'][0]['statistics']['commentCount']
            title = f_data_2['items'][0]['snippet']['title']
            publishedAt = f_data_2['items'][0]['snippet']['publishedAt']
            publishedAt = get_date(publishedAt)
            # wk3.append_row([i, publishedAt, title, viewCount, likeCount, commentCount])
            f.write(i + ';' + publishedAt + ';' + title + ';' + viewCount + ';' + likeCount + ';' + commentCount + '\n')
            print(i, publishedAt, title)
        except:
            print(i, "This video has been deleted or made private.")
            f.write(i + '\n')

    else:
        print("Youtube API is not Response")
        break

f.close()