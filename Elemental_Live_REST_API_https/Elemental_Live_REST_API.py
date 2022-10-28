# git 테스트

import time
import hashlib
import requests

class Elemental_API:

    def __init__(self, IP, USER, KEY, EVENT_ID):
        self.IP = IP               # IP = '10.20.22.139' #Elemental Live: IP
        self.USER = USER           # USER = 'encoder' #Elemental Live: USER ID
        self.KEY = KEY             # KEY = 'y5jYbKPpsnpt1bjs_MVp' #Elemental Live: Authentication Key
        self.EVENT_ID = EVENT_ID   # EVENT ID = '17' #Elemental Live Event
        self.INPUT_ID = None       # Input ID
        self.OUTPUT_ID = None      # Output ID
        self.ACT = None            # start, stop, reset, status..... etc 
        self.TYPE = None           # json or xml
        self.Image_file_path = None
        self.Image_layer = None
        self.GAIN = None
        self.FILE = None

    # REST API를 사용하기 위한 권한 함수
    def encAuth(self, ACT):
        try:
            xtime = str(int(time.time())+30)
            joint = ('/live_events/{}/{}'.format(self.EVENT_ID, ACT)+self.USER+self.KEY+xtime)
            pri_enc = hashlib.md5()
            sec_enc = hashlib.md5()
            sec_enc.update((joint).encode('UTF-8'))
            sec_text = sec_enc.hexdigest()
            pri_enc.update((self.KEY+sec_text).encode('UTF-8'))
            enc_text = pri_enc.hexdigest()
            headers = {'X-Auth-User': self.USER, 'X-Auth-Expires': xtime, 'X-Auth-Key': enc_text,
                    'Accept': 'application/xml', 'Content-type': 'application/xml',}
        except Exception as e: print('API authentication error: {}'.format(e))
        return headers

    # staus를 확인
    def getTest(self, ACT, TYPE):
        if TYPE == 'json':        
            try:
                headers = self.encAuth('{}.json'.format(ACT))
                response = requests.get('http://{}/api/live_events/{}/{}.json'.format(self.IP, self.EVENT_ID, ACT), headers=headers, verify = False).json()
                status = response
            except Exception as e:
                print(e)
        elif TYPE == 'xml':
            try:
                headers = self.encAuth(ACT)
                response = requests.get('http://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, verify = False)
                status = response.text
            except Exception as e:
                print(e)
        else:
            print("Type error Type is selected json or xml")
            return
        return print(status)

    # Event start, stop, reset 동작 제어 
    def postTest(self, ACT):
        try:
            headers = self.encAuth(ACT)
            datas = '<{0}></{0}>'.format(ACT)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("postTest", result)

    # Input source swiching
    def postTest_activate_input(self, ACT, INPUT_ID):
        try:
            headers = self.encAuth(ACT)
            datas = '<input_id>{0}</input_id>'.format(INPUT_ID)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("activate_input", result)

    # 전역 이미지 인서터
    def postTest_global_image_inserter(self, ACT, IMAGE_PATH, IMAGE_LAYER):
        try:
            headers = self.encAuth(ACT)
            datas = ("<{0}>{1}<image_x>0</image_x><image_y>0</image_y><opacity>100</opacity><image_inserter_input><uri>{2}</uri></image_inserter_input></{0}>"
            .format(ACT, IMAGE_LAYER, IMAGE_PATH)).encode('utf-8')
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("global_image_inserter", result)

    # 인풋 소스 이미지 인서터
    def postTest_input_image_inserter(self, ACT, IMAGE_PATH, IMAGE_LAYER, INPUT_ID):
        try:
            headers = self.encAuth(ACT + '/input/'+ INPUT_ID)
            datas = ("<{0}>{1}<image_x>0</image_x><image_y>0</image_y><opacity>100</opacity><image_inserter_input>"
            "<uri>{2}</uri></image_inserter_input></{0}>"
            .format(ACT, IMAGE_LAYER, IMAGE_PATH)).encode('utf-8')
            response = requests.post('https://{}/api/live_events/{}/{}/input/{}'.format(self.IP, self.EVENT_ID, ACT, INPUT_ID), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("input_image_inserter", result)

    # 아웃풋 소스 이미지 인서터
    def postTest_output_image_inserter(self, ACT, IMAGE_PATH, IMAGE_LAYER, OUTPUT_ID):
        try:
            headers = self.encAuth(ACT + '/output/'+ OUTPUT_ID)
            datas = ("<{0}>{1}<image_x>0</image_x><image_y>0</image_y><opacity>100</opacity><image_inserter_input>"
            "<uri>{2}</uri></image_inserter_input></{0}>"
            .format(ACT, IMAGE_LAYER, IMAGE_PATH)).encode('utf-8')
            response = requests.post('https://{}/api/live_events/{}/{}/output/{}'.format(self.IP, self.EVENT_ID, ACT, OUTPUT_ID), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("output_image_inserter", result)

    # Motion graphic image inserter는 motion graphics license가 포함 되어야만 가능함. (현재 사용을 못함)
    def postTest_motion_image_inserter(self, ACT, Image_file_path, Image_layer):
        try:
            headers = self.encAuth(ACT)
            datas = "<{0}>{1}<opacity>100</opacity><active>true</active><enable_rest>true</enable_rest><full_frame>false</full_frame><loop_input>true</loop_input><insertion_mode>mov</insertion_mode><motion_image_inserter_input><uri>{2}</uri></motion_image_inserter_input></{0}>".format(ACT, Image_layer, Image_file_path)
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("motion_image_inserter", result)

    # 오디오 레벨 조정.
    def postTest_adjust_audio_gain(self, ACT, GAIN):
        try:
            headers = self.encAuth(ACT)
            datas = '<gain>{0}</gain>'.format(GAIN)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("adjust_audio_gain", result)

    # Input Source File replace ----> 기존에 대기하던 인풋이 모두 사라지고 새로운 파일을 추가 (현재 동작중인 인풋은 제외)
    def postTest_replace_playlist_file(self, ACT, File_path):
        try:
            headers = self.encAuth(ACT)
            datas = ('<inputs><input><loop_source>true</loop_source><file_input><uri>{}</uri></file_input></input></inputs>'
            .format(File_path)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("replace_playlist_file", result)

#TEST    # Input Source SDI replace ----> 기존에 대기하던 인풋이 모두 사라지고 새로운 SDI를 추가 (현재 동작중인 인풋은 제외)
    def postTest_replace_playlist_sdi(self, ACT, SDI_NUM):
        try:
            headers = self.encAuth(ACT)
            datas = ('<inputs><input><loop_source>true</loop_source><file_input><channel>{}</channel><channel_type>3G-SDI</channel_type></file_input></input></inputs>'
            .format(SDI_NUM)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("replace_playlist_sdi", result)

#TEST    # Input Source Network replace ----> 기존에 대기하던 인풋이 모두 사라지고 새로운 Network Source를 추가 (현재 동작중인 인풋은 제외)
    def postTest_replace_playlist_network(self, ACT, Network_address):
        try:
            headers = self.encAuth(ACT)
            datas = ('<inputs><input><network_input><uri>{}</uri></network_input></input></inputs>'
            .format(Network_address)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("replace_playlist_network", result)

    # Input Source File Add ----> 새로운 파일을 추가
    def postTest_add_playlist_file(self, ACT, File_path):
        try:
            headers = self.encAuth(ACT)
            datas = ('<input><loop_source>true</loop_source><file_input><uri>{0}</uri></file_input></input>'
            .format(File_path)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("add_playlist_file", result)

    # Input Source SDI input Add ----> 새로운 SDI를 추가
    def postTest_add_playlist_sdi(self, ACT, SDI_NUM):
        try:
            headers = self.encAuth(ACT)
            datas = ('<input><device_input><channel>{}</channel><channel_type>3G-SDI</channel_type></device_input></input>'
            .format(SDI_NUM)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("add_playlist_sdi", result)

    # Input Source Network input Add ----> 새로운 Network를 추가
    def postTest_add_playlist_network(self, ACT, Network_address):
        try:
            headers = self.encAuth(ACT)
            datas = ('<input><network_input><uri>{}</uri></network_input></input>'
            .format(Network_address)).encode('utf-8')
            print(datas)
            response = requests.post('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT), headers=headers, data=datas, verify = False)
            print('https://{}/api/live_events/{}/{}'.format(self.IP, self.EVENT_ID, ACT))
            result = (response, response.status_code)
        except Exception as e:
            print('Failed to stop recording file :', e)
        return print("add_playlist_network", result)