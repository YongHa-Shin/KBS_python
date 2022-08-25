from Youtube_data import Youtube_video_data
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Youtube_video_data 객체 생성 
Yd = Youtube_video_data()

print("시작_행")
range_text_B = input()

print("마지막_행")
range_text_F = input()

sheet_range = "B{}:F{}".format(range_text_B, range_text_F)

# ********************************************************************************************************************************************************************* #
# sheet_range = 'B184:F184' # ******************************************************************************************************************************************* #
# ********************************************************************************************************************************************************************* #

# 스프레드시트 구글 권한 처리
scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'Google_Spread_Sheet_Share\stoked-edition-337807-fe85722dd588.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1-Fj44MEAPv7T8qMNvqYSbSi_-elJEn4NsiavlRUhJHM/edit#gid=1554750920'

# 스프레드시트를 url을 통하여 오픈한다.
wks = gc.open_by_url(spreadsheet_url)

# '유튜브LIVE 일지' 시트를 선택한다.
worksheet = wks.worksheet('유튜브LIVE 일지')

# '유튜브LIVE 일지' 시트의 Cell 범위를 선택하여 range_list에 저장한다.
temp = []
range_list = worksheet.range(sheet_range) # 스프레드시트 video_id 영역과 유튜브 데이터 인서트 영역
for cell in range_list:

    if cell.__dict__['value'][0:16] == 'https://youtu.be' or cell.__dict__['value'][0:23] == 'https://www.youtube.com' :
        temp = Yd.get_youtube_data(cell.__dict__['value']) # 유튜브 url을 사용하여 유튜브 데이터 추출
    else :
        if temp :
            cell.__dict__['value'] = temp.pop(0)
        else :
            continue

# 구글 스프레드시트에 유튜브 데이터 삽입
worksheet.update_cells(range_list)



