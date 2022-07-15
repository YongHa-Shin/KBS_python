import pyautogui
import time
import pygetwindow

titles = pygetwindow.getAllTitles()
# print(titles)
wininfo = pygetwindow.getWindowsWithTitle('제목 없음 - Windows 메모장')[0]   
print(wininfo)
wininfo.activate() #윈도우 활성화

while(True) :
    pyautogui.press('c')
    time.sleep(3)

# pyautogui.click(wininfo.left+50, wininfo.top+ 540)

# while(True) :
#     time.sleep(3)
#     wininfo.activate()
#     print(wininfo)
#     pyautogui.click(wininfo.left, wininfo.top)
#     # pyautogui.press('right')
#     # pyautogui.click(wininfo.left + 100, wininfo.top+ 100)
#     # pyautogui.press('right')


# # fw = pyautogui.getActiveWindow()
# # fw.close()   # 현재 활성화 상태인 창 닫기