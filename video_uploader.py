def upload_video(path: str, video: any):
  with open(path, "wb") as buffer:
    buffer.write(video.read())
  return path
