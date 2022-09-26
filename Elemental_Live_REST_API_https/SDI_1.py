# SDI1 -> Event ID = 24, Input1 ID = 35, Input2 ID = 54

from Elemental_Live_REST_API import Elemental_API
import urllib3

urllib3.disable_warnings() # https 인증서 관련 경고문 제거

enc_ip = '10.20.22.139' #Elemental Live: IP
enc_user = 'encoder' #Elemental Live: USER ID
enc_key = 'y5jYbKPpsnpt1bjs_MVp' #Elemental Live: Authentication Key

enc_img_path_right = '/data/ftpuser/image/right_top_logo2.png' # 우상단_리플레이.png, right_top_logo.png, right_top_logo2.png
enc_img_path_left = '/data/ftpuser/image/image_null.png'        # image_null.png
enc_img_layer_0 = '<layer>0</layer>'

enc_event = '24'                 #Elemental Live Event ID
enc_input_id = '35'                   #Elemental INPUT ID
enc_input_id_2 = '54'                   #Elemental INPUT ID

ELR = Elemental_API(enc_ip, enc_user, enc_key, enc_event)

ELR.getTest('status', 'json')
ELR.postTest_input_image_inserter('image_inserter', enc_img_path_left, enc_img_layer_0, enc_input_id)  # 4.좌상로고 삽입
ELR.postTest_global_image_inserter('image_inserter', enc_img_path_right, enc_img_layer_0)              # 5.우상로고 삽입
ELR.postTest_adjust_audio_gain('adjust_audio_gain', '10')                                              # 6.오디오 출력 조정 (보통은 10dB정도 올림) 

# 하단자막 올리기
caption = "/data/ftpuser/image/image_null.png" # caption.png, image_null.png
ELR.postTest_output_image_inserter('image_inserter', caption, enc_img_layer_0, '180')

# # 썸네일로 덮어버리기
# ssum = '/data/ftpuser/image/ssum.png'
# ELR.postTest_input_image_inserter('image_inserter', ssum, enc_img_layer_0, '35')
# ELR.postTest_adjust_audio_gain('adjust_audio_gain', '-60')  

# ELR.postTest_activate_input('activate_input', enc_input_id_2) # enc_input_id, enc_input_id_2         # Input switching
# ELR.postTest_input_image_inserter('image_inserter', enc_img_path_left, enc_img_layer_0, enc_input_id2)  # 4.좌상로고 삽입