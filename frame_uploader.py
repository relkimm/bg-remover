import cv2

async def upload_frame(dir: str, index: int, frame: any):
  path = f"{dir}/{index}.png"
  cv2.imwrite(path, frame)
  return path
