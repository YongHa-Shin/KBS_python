from youtube_live_data import YT_Live
import matplotlib.pyplot as plt
import numpy as np
import time

# API_KEY = "AIzaSyDIRXONB_JFvavwf7XFJ3esQrF9tKTd6Jw" # API키
API_KEY = "AIzaSyDPafGCd3dlAzfH9Wa1vDDWirchypWbGdg" # API 예비키
channel_id = {"KBS News" : "UCcQTRi69dsVYHN3exePtZ1A", "MBC News" : "UCF4Wxdo3inmxP-Y59wXDsFw", "SBS News" : "UCkinYTS9IHqOEwR1Sze2JTw", "JTBC News" : "UCsU-I-vHLiaMfV_ceaYz5rQ"}

sum = 0
x = []
y = []
num = np.arange(4)
now = time.localtime()
current_time = "{}.{}.{}. {}:{}".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min)

for key, value in channel_id.items() :
    yt = YT_Live(API_KEY, value)
    sum = yt.get_search_snippet()
    print("--------", key, ": 시청자수", sum, "--------")

    if sum == "LiveEvent is not exist" or sum == None :
        sum = 0
        x.append(key)
        y.append(sum)

    else :
        x.append(key)
        y.append(sum)

plt.title(current_time + ' Youtube Live current viewers', fontsize=12)
bar = plt.bar(num, y, color=['navy','m','dodgerblue','b'], width=0.6)
plt.xticks(num, x)

# 그래프 수를 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.0f' % height, ha='center', va='bottom', size = 8)

plt.show()
# plt.savefig("image.png") # 이미지 저장
    