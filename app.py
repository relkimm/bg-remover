import asyncio
from fastapi import FastAPI, UploadFile
from video_uploader import upload_video
from frame_extractor import extract_frames
from bg_remover import remove_bg

app = FastAPI()

@app.get("/")
def index():
  return { "hello": "world" }

@app.post("/video")
async def video(file: UploadFile):
  video_path = upload_video(
    path=f"static/video/{file.filename}", 
    video=file.file,
  )
  frames = extract_frames(
    dir="static/frame",
    video_path=video_path,
  )
  remove_bg_tasks = [remove_bg(frame) for frame in frames]
  await asyncio.gather(*remove_bg_tasks)
  return { "video": "uploaded" }