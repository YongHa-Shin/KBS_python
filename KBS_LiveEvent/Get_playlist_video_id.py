import requests # pip install requests
import json

playlistId = 'PL9a4x_yPK_87aeATLZsQM0XCjREJPz9zV'
playlistId_test = 'PL9a4x_yPK_86PmV1rKbItLy53F_YEUzsH'
video_id_list = []
num = 0

API_KEY = "AIzaSyDIRXONB_JFvavwf7XFJ3esQrF9tKTd6Jw"

url = f"https://www.googleapis.com/youtube/v3/playlistItems?key={API_KEY}&part=contentDetails&playlistId={playlistId}&maxResults=50"
json_url = requests.get(url)
data = json.loads(json_url.text)

index_data = data['items']
for i in index_data:
    video_id_list.append(i['contentDetails']['videoId'])
    print(i['contentDetails']['videoId'])
    num += 1

f = open("새파일.txt", 'w')

while 1 :
    if 'nextPageToken' in data :
        url = f"https://www.googleapis.com/youtube/v3/playlistItems?key={API_KEY}&part=contentDetails&playlistId={playlistId}&maxResults=50&pageToken={data['nextPageToken']}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        index_data = data['items']
        for i in index_data:
            video_id_list.append(i['contentDetails']['videoId'])
            print(i['contentDetails']['videoId'])
            f.write(i['contentDetails']['videoId']+'\n')
            num += 1

    else :
        break

print(num)