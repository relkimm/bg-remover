from fastapi import FastAPI, UploadFile
from video_uploader import upload_video

app = FastAPI()

@app.get("/")
def index():
  return { "hello": "world" }

@app.post("/video")
def video(file: UploadFile):
  upload_video(f"static/video/{file.filename}", file.file)
  return { "video": "uploaded" }