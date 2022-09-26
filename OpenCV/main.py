from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from stream_cv import getCameraStream

# FastAPI를 실행하기 위해서는 터미널에 uvicorn main:app --reload 을 입력한다.
app = FastAPI()

@app.get("/")
async def root():
    return {"Hello" : "PNP"}

@app.get("/test")
async def test(userName):
    return {"Hello" : f"{userName}"}

@app.get("/video")
def video():
    # Mjpeg 포맷으로 스트리밍
    return StreamingResponse(getCameraStream(),
    media_type= "multipart/x-mixed-replace; boundary=PNPframe")