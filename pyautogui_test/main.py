import pyautogui
import time

def mouseclick(x, y):
    pyautogui.click(x, y, clicks = 2)

print("10초 후에 클릭 매크로 실행합니다.")

for i in range(1, 11):
    print(str(i) + " 초")
    time.sleep(1)

print('실행!')

mouse_location = {
    2407 : 193,
    3337 : 189,
    2436 : 529,
    3458 : 601,
    2276 : 899,
    2889 : 940,
    3504 : 869
}

while True:
    for key, value in mouse_location.items():
        mouseclick(key, value)
        time.sleep(10)
        mouseclick(2880, 540)
        time.sleep(1)


