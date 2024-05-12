import cv2

def extract_frames(dir: str, video_path: str) -> list[str]:
  video = cv2.VideoCapture(video_path)
  frames = []
  while video.isOpened():
    success, frame = video.read()
    if not success:
      break
    frames.append(frame)
  video.release()
  return frames
