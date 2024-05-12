import asyncio
from fastapi import FastAPI, UploadFile
from video_uploader import upload_video
from frame_extractor import extract_frames
from bg_remover import remove_bg
from frame_uploader import upload_frame

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
  frames = await asyncio.gather(*remove_bg_tasks)
  upload_frame_tasks = [upload_frame("static/frame", index, frame) for index, frame in enumerate(frames)]
  frame_paths = await asyncio.gather(*upload_frame_tasks)
  return { "video": "uploaded" }