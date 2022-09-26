import cv2
import time

video_source = {
    "마라도" : "https://stream1.ktict.co.kr:8083/livekbsd1/9982/chunks.m3u8?",
    "세병교" : "https://stream1.ktict.co.kr:8083/livekbsd1/9967/chunks.m3u8?",
    "수영만" : "https://stream1.ktict.co.kr:8083/livekbsd1/9991/chunks.m3u8?"
    }

for key, value in video_source.items() :
    cap = cv2.VideoCapture(value)

    # 프레임을 정수형으로 형 변환
    frameWidth = 1280
    frameHeight = 720
    # frameWidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))	# 원본영상의 넓이(가로) 프레임
    # frameHeight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))	# 원본영상의 높이(세로) 프레임
    
    if frameWidth == 0 and frameHeight == 0:
        continue

    frame_size = (frameWidth, frameHeight)
    print('frame_size={}'.format(frame_size))
    frameRate = 30
    target_time = time.time() + 10

    while time.time() < target_time:
        # 한 장의 이미지(frame)를 가져오기
        # 영상 : 이미지(프레임)의 연속
        # 정상적으로 읽어왔는지 -> retval
        # 읽어온 프레임 -> frame
        retval, frame = cap.read()
        if not(retval):	# 프레임정보를 정상적으로 읽지 못하면
            break  # while문을 빠져나가기
        
        # cv2.imshow('aaa', image)    
        cv2.imshow('frame', frame)	# 프레임 보여주기
        key = cv2.waitKey(frameRate)  # frameRate msec동안 한 프레임을 보여준다
        
        # # 키 입력을 받으면 키값을 key로 저장 -> esc == 27(아스키코드)
        # if key == 27:
        #     break	# while문을 빠져나가기

# print("반복문 탈출!!")   
cap.release()	# 영상 파일(카메라) 사용을 종료
cv2.destroyAllWindows()

