import cv2

# video_source = {
#     "마라도" : "https://stream1.ktict.co.kr:8083/livekbsd1/9982/chunks.m3u8?",
#     "세병교" : "https://stream1.ktict.co.kr:8083/livekbsd1/9967/chunks.m3u8?",
#     "수영만" : "https://stream1.ktict.co.kr:8083/livekbsd1/9991/chunks.m3u8?"
#     }

def getCameraStream():
    camOjb = cv2.VideoCapture("https://stream1.ktict.co.kr:8083/livekbsd1/9982/chunks.m3u8?")
    while True:
        # 예외처리
        retVal, mat = camOjb.read()
        if not retVal:
            break
        
        # openCV 이미지를 jpeg 포맷으로 변환
        retVal, jpgImg = cv2.imencode('.jpg', mat)

        # 스트리밍을 위한 jpeg 포맷을 바이너리 형태로 변환
        jpgBin = bytearray(jpgImg.tobytes())

        # 비동기 처리 대기
        yield (b'--PNPframe\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpgBin + b'\r\n')