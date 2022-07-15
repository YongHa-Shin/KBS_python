# from Oauth2_test import oauth2_set
# from googleapiclient.discovery import build

# CLIENT_SECRET_FILE = 'client_secrets.json'
# SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
# ouath2 = oauth2_set(CLIENT_SECRET_FILE, SCOPES)
# credentials = ouath2.local_server_oauth2_set()
# youtube = build("youtube", "v3", credentials = credentials)

# # 유튜브 이벤트 생성하는 명령어
# request = youtube.channels().list(
#     part = "statistics",
#     id = "UCcQTRi69dsVYHN3exePtZ1A"
# )

# response = request.execute()
# print(response)


# import os
# import sys
# import urllib.request
# import json

# client_id = "4GGZaLGX4YRq8ufnEtV0" # 개발자센터에서 발급받은 Client ID 값
# client_secret = "XZ1FFffklI" # 개발자센터에서 발급받은 Client Secret 값
# encText = urllib.parse.quote("안녕? 디지몬~ 내 꿈을 꾸면서 잠이 들래? 친구들 모두 안녕~")
# data = "source=ko&target=en&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id",client_id)
# request.add_header("X-Naver-Client-Secret",client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()

# if(rescode==200):
#     response_body = response.read()
#     response_body = json.loads(response_body.decode('utf-8'))
#     response_body = response_body["message"]["result"]["translatedText"]
#     print(response_body)
# else:
#     print("Error Code:" + rescode)

# duration = "PT2M45S"
# duration = duration[2:]

# if duration.find('H') == -1 :
#     if duration.find('M') == -1:
#         print()


# dateDict = [{0: '(월)',1: '(화)',2: '(수)',3: '(목)',4: '(금)',5: '(토)',6: '(일)'}, {1: '(월)',3: '(화)',5: '(수)',7: '(목)',9: '(금)',11: '(토)',13: '(일)'}, {0: '(월)',1: '(화)',2: '(수)',3: '(목)',4: '(금)',5: '(토)',6: '(일)'}]

# print(dateDict[0][0])


# f = open('현장영상_백업.txt', 'a')
# f.write("gkdl")
# f.close()

import datetime
print(str(datetime.timedelta(seconds= 2000)))
url = 'https://youtu.be/0cekCVAG6sU'
id = url.rsplit('/')[3]
print(id) 