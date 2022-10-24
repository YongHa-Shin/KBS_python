from Elemental_Live_REST_API import Elemental_API
import urllib3

urllib3.disable_warnings() # https 인증서 관련 경고문 제거

enc_ip = '10.20.22.139' #Elemental Live: IP
enc_user = 'encoder' #Elemental Live: USER ID
enc_key = 'x3QojFkUjvkkojybswS7' #Elemental Live: Authentication Key

enc_img_path_right = '/data/ftpuser/image/right_top_logo2.png' # 우상단_리플레이.png, right_top logo.png
enc_img_path_left = '/data/ftpuser/image/좌상.png'
enc_img_layer_0 = '<layer>0</layer>'
enc_file_path = '/data/ftpuser/archive/BGM.mp4'
enc_file_path2 = '/data/ftpuser/archive/test2.mp4'
enc_nework_input = 'udp://localhost:5002?interface=lo'
enc_sdi_num = '4' # SDI Number, 1 or 2 or 3 or 4 중에 선택하세요
enc_network_address = 'udp://localhost:5002?interface=lo'

#---------------- 꼭 수정하면서 사용하도록 ---------------#
enc_event = '38'                 #Elemental Live Event ID
enc_input_id = '46'                   #Elemental INPUT ID
enc_output_id = '199'
#-------------------------------------------------------#

ELR = Elemental_API(enc_ip, enc_user, enc_key, enc_event)

ELR.getTest('status', 'json')
ELR.postTest_output_image_inserter('image_inserter', enc_img_path_right, enc_img_layer_0, enc_output_id)
# ELR.postTest_add_playlist_file('inputs', enc_file_path)
# ELR.postTest_add_playlist_sdi('inputs', enc_sdi_num)
# ELR.postTest_replace_playlist_file('playlist', enc_file_path2)
# ELR.postTest_replace_playlist_sdi('playlist', enc_sdi_num)
# ELR.postTest_replace_playlist_network('playlist', enc_network_address)

#------------------------------------------------- Elemental live Streaming 순서 -------------------------------------------------#

#                                                                                                        # 1.Event ID, INPUT ID 꼭 수정한다    
# ELR.getTest('status', 'json')                                                                  # 2.이벤트 status 확인 (만약 Complete이면, ELR.postTest('reset') 먼저 실행)                                                                                       
# ELR.postTest('start')                                                                                  # 3.이벤트 시작                                                                                                                                                                                                
# ELR.postTest_input_image_inserter('image_inserter', enc_img_path_left, enc_img_layer_0, enc_input_id)  # 4.좌상로고 삽입
# ELR.postTest_global_image_inserter('image_inserter', enc_img_path_right, enc_img_layer_0)              # 5.우상로고 삽입
# ELR.postTest_adjust_audio_gain('adjust_audio_gain', '10')                                              # 6.오디오 출력 조정 (보통은 10dB정도 올림) 
# ELR.postTest_activate_input('activate_input', enc_input_id)                                            # 7.Input Swiching

#------------------------------------------------- 유튜브 이벤트 종료 후 시점 ------------------------------------------------------#  

# ELR.postTest('stop') # 1.이벤트 종료
# ELR.postTest('reset') # 2.이벤트 리셋 11
                  
#---------------------------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------ Test 중인 함수 ------------------------------------------------------------#

# ELR.postTest_input_image_inserter('image_inserter', '/data/ftpuser/image/ssum.png', enc_img_layer_0, enc_input_id)
# ELR.postTest_replace_playlist_file('playlist', enc_file_path2) #'/data/ftpuser/image/ssum.jpg'
# ELR.postTest_add_playlist_file('inputs', enc_file_path)
# ELR.postTest_activate_input('activate_input', enc_input_id)
# ELR.postTest_global_image_inserter('image_inserter', enc_img_path_right, enc_img_layer_0)
# ELR.postTest_input_image_inserter('image_inserter', enc_img_path_left, enc_img_layer_0, enc_input_id)
# ELR.postTest_output_image_inserter('image_inserter', enc_img_path_right, enc_img_layer_1)
# ELR.postTest_adjust_audio_gain('adjust_audio_gain', '0')
# ELR.postTest_motion_image_inserter('motion_image_inserter', enc_img_path_left, enc_img_layer_0) -------> 라이센스 있어만 함
# ELR.postTest_add_playlist_sdi('inputs', enc_sdi_num)
# ELR.postTest_add_playlist_network('inputs', enc_network_address)

# ELR.getTest('status', 'json')
# ELR.getTest('outputs', 'json')
# ELR.postTest('start')
# ELR.postTest('stop')
# ELR.postTest('reset')

#result = getTest(enc_ip, enc_event, enc_user, enc_key, 'status', 'xml')
#result = getTest(enc_ip, enc_event, enc_user, enc_key, 'inputs', 'json')
#result = getTest(enc_ip, enc_event, enc_user, enc_key, 'inputs', 'xml')
#result = getTest(enc_ip, enc_event, enc_user, enc_key, 'outputs', 'json')
#result = getTest(enc_ip, enc_event, enc_user, enc_key, 'outputs', 'xml')
#result = postTest(enc_ip, enc_event, enc_user, enc_key, 'start', '')
#result = postTest(enc_ip, enc_event, enc_user, enc_key, 'stop', '')
#result = postTest(enc_ip, enc_event, enc_user, enc_key, 'reset', '')
#result = postTest(enc_ip, enc_event, enc_user, enc_key, 'activate_input', '인풋번호') #running 상태일 때
