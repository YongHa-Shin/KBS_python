from Elemental_Live_REST_API import Elemental_API
import time
import urllib3
urllib3.disable_warnings() # https 인증서 관련 경고문 제거

enc_ip = '10.20.22.139' #Elemental Live: IP
enc_user = 'encoder' #Elemental Live: USER ID
enc_key = 'y5jYbKPpsnpt1bjs_MVp' #Elemental Live: Authentication Key
enc_event = '36'

enc_input_id = ['96', '97', '98', '99']
ELR = Elemental_API(enc_ip, enc_user, enc_key, enc_event)
ELR.postTest('start')
time.sleep(10)
ELR.getTest('status', 'json')
# ELR.postTest_add_playlist_network('inputs', "https://stream1.ktict.co.kr:8083/livekbsd1/9968/chunks.m3u8?")

# while True:
#     for i in enc_input_id:
#         ELR.postTest_activate_input('activate_input', i)
#         time.sleep(10)