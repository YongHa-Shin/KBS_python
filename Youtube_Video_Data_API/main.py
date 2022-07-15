from Youtube_video_data import YTstats

API_KEY = "AIzaSyDIRXONB_JFvavwf7XFJ3esQrF9tKTd6Jw" # API키
# API_KEY = "AIzaSyDPafGCd3dlAzfH9Wa1vDDWirchypWbGdg" # API 예비키

# channel_id = "UCcQTRi69dsVYHN3exePtZ1A" #KBS News 계정
# channel_id = "UCF4Wxdo3inmxP-Y59wXDsFw" #MBCNEWS 계정
# channel_id = "UCkinYTS9IHqOEwR1Sze2JTw" #SBS뉴스 계정
# channel_id = "UCsU-I-vHLiaMfV_ceaYz5rQ" #JTBC뉴스 계정

channel_id = ["UCcQTRi69dsVYHN3exePtZ1A", "UCF4Wxdo3inmxP-Y59wXDsFw", "UCkinYTS9IHqOEwR1Sze2JTw", "UCsU-I-vHLiaMfV_ceaYz5rQ"]

for i in channel_id :
    yt = YTstats(API_KEY, i)
    yt.get_channel_statistics()
    yt.get_channel_video_data() 
    yt.dump()

