from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

# 원하는 브라우저 주소를 입력하고 열기
driver.implicitly_wait(5)
driver.maximize_window()
url = "http://kncs.kbs.co.kr/#"
driver.get(url)

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#userId")
id.click()
id.send_keys("33134")

# 패스워드 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#passWd")
pw.click()
pw.send_keys("920202")

# 로그인 버튼
login_button = driver.find_element(By.CSS_SELECTOR, "#formLogin > div.login-state-default > div.login-util > button")
login_button.click()

time.sleep(2)
driver.switch_to.alert.accept()
# uselessWindows = driver.window_handles
# print(uselessWindows)
# driver.switch_to.window(uselessWindows[0])
# driver.close()
# time.sleep(2)

# da = Alert(driver)
# da.dismiss()

# time.sleep(2)

# print(driver.window_handles)

# time.sleep(2)

# da = Alert(driver)
# da.accept()

# # 팝업창                                       #jqxWidget8e2c67d0
# pop_up = driver.find_element(By.CSS_SELECTOR, "#jqxWidgetbb3435c3")
# pop_up.click()                                 #jqxWidgetcb8668cf
