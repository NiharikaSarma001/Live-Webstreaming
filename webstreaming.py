import cv2
import urllib.request
import numpy as np
from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
app = FastAPI()
#url = "https://5e35-2406-7400-61-5d2e-ad57-10fb-b51b-5dc5.in.ngrok.io/video"
url = "http:192.168.0.123:8080/video"
cap = cv2.VideoCapture(url)
@app.get("/")
async def read_root():
    return {"hello": "world"}

@app.get("/video")
async def video_feed(response: Response):
    # while True:
    #     img_resp = urllib.request.urlopen(url)
    #     print(img_resp)
        
    #     img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    #     frame = cv2.imdecode(img_arr, -1)
    #     ret, jpeg = cv2.imencode('.jpg', frame)
    #     response.headers["content-type"] = "image/jpeg"
    #     await response.send(jpeg.tobytes())
    return StreamingResponse(generator(), media_type="multipart/x-mixed-replace; boundary=frame")
def generator():
    while True:
        #img_resp = urllib.request.urlopen(url)
        #print(img_resp)
        res, frame = cap.read()
        #img_arr = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        #frame = cv2.imdecode(img_arr, -1)
        ret, jpeg = cv2.imencode('.jpg', frame)
        #response.headers["content-type"] = "image/jpeg"
        yield (b"--frame\r\n" 
               b"Content-Type: image/jpeg\r\n\r\n" + bytearray(jpeg) + b"\r\n")
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
