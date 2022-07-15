from googleapiclient.discovery import build
from urllib import response
from Oauth2 import oauth2_set

CLIENT_SECRET_FILE = 'client_secrets.json'
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
ouath2 = oauth2_set(CLIENT_SECRET_FILE, SCOPES)
credentials = ouath2.local_server_oauth2_set()
youtube = build("youtube", "v3", credentials = credentials)

# 유튜브 이벤트 생성하는 명령어
request = youtube.liveBroadcasts().insert(
    part = "snippet,contentDetails,status",

    body = {
        "etag": "",
        "id": "",
        "kind": "youtube#liveBroadcast",

        "contentDetails": {
            'monitorStream': {
                'enableMonitorStream': True, 
                'broadcastStreamDelayMs': 0, 
                }, 
            'enableEmbed': False, 
            'enableDvr': True, 
            'enableContentEncryption': False, 
            'startWithSlate': False, 
            'recordFromStart': True, 
            'enableClosedCaptions': False, 
            'closedCaptionsType': 'closedCaptionsDisabled', 
            'latencyPreference': 'normal', # 지연시간 설정 normal, low, ultraLow 중 1개를 선택(안넣으면 normal 프리셋으로 설정이 된다.)
            'projection': 'rectangular', 
            'enableAutoStart': False, 
            'enableAutoStop': False,
            "licensedContent": True
        },

        "snippet": {
            "actualEndTime": "",
            "actualStartTime": "",
            "channelId": "UC5zgg-h3t9bj9WS3CUcGCag",
            "description": "test_description_0518_03", # 이벤트 내용
            "isDefaultBroadcast": False,
            "liveChatId": "",
            "publishedAt": "",
            "scheduledEndTime": "2022-05-18T08:05:00Z", #2022-05-13T06:00:00Z # 이벤트 종료예정시간(꼭 UTC시간으로 넣어야만 한다.)
            "scheduledStartTime": "2022-05-18T08:00:00Z", #2022-05-13T05:55:00 # 이벤트 시작예정시간(꼭 UTC시간으로 넣어야만 한다.)
            "thumbnails": {
                "default": {},
                "high": {},
                "maxres": {},
                "medium": {},
                "standard": {}
            },
            "title": "test_title5_0518_03" # 이벤트 제목
        },

        "status": {
            "lifeCycleStatus": "created",
            "liveBroadcastPriority": "high",
            "privacyStatus": "public", # "private" -> 비공개
            "recordingStatus": "notRecording",
            "selfDeclaredMadeForKids": False,
            "license": "youtube"
        }
    }
)

# 유튜브 이벤트와 스트림키를 매칭 시켜주는 명령어
# request = youtube.liveBroadcasts().bind(
#     id="0Cz7gbOATD8", #유튜브 이벤트의 ID. liveBroadcasts().list()를 통해 확인할 수 있다.
#     part="snippet",
#     streamId="5zgg-h3t9bj9WS3CUcGCag1652424083039963" # 스트림키의 ID. stream.list()를 통해 확인할 수 있다.
# )

# # 유튜브 이벤트 스트림 송출 시작
# request = youtube.liveBroadcasts().transition(
#     broadcastStatus = "live", # 송출시작 명령을 의미한다. 
#     id="0Cz7gbOATD8", #유튜브 이벤트의 ID. liveBroadcasts().list()를 통해 확인할 수 있다.
#     part="id"
# )

# # 유튜브 이벤트 스트림 송출 종료
# request = youtube.liveBroadcasts().transition(
#     broadcastStatus = "complete", # 송출종료 명령을 의미한다. 
#     id="0Cz7gbOATD8", #유튜브 이벤트의 ID. liveBroadcasts().list()를 통해 확인할 수 있다.
#     part="id"
# )

response = request.execute()
print(response)

# # 썸네일을 입력하는 양식
# 'thumbnails': {
#     'default': {
#         'url': 'https://i9.ytimg.com/vi/5SWd1gW_g14/default_live.jpg?sqp=CIjj95MG&rs=AOn4CLBDHVX12F9Dx7YCLC8IkMCCPhSU0A', 
#         'width': 120, 
#         'height': 90
#         }, 
#     'medium': {
#         'url': 'https://i9.ytimg.com/vi/5SWd1gW_g14/mqdefault_live.jpg?sqp=CIjj95MG&rs=AOn4CLB3FkSKX_ZjVHr4V41t8mAQV0UyAA', 
#         'width': 320, 
#         'height': 180
#     }, 
#     'high': {
#         'url': 'https://i9.ytimg.com/vi/5SWd1gW_g14/hqdefault_live.jpg?sqp=CIjj95MG&rs=AOn4CLBBt9BuqFZ3kx1yRamaV6aVnAZ6nA', 
#         'width': 480, 
#         'height': 360
#     }
# }