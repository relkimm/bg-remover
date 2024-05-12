import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks.python import BaseOptions, vision

base_options = BaseOptions(model_asset_path="selfie_segmenter.tflite")
options = vision.ImageSegmenterOptions(
  base_options=base_options,
  output_category_mask=True,
)
segmenter = vision.ImageSegmenter.create_from_options(options)

async def remove_bg(img: any):
  rmg_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  mp_img = mp.Image(data=rmg_img, image_format=mp.ImageFormat.SRGB)
  segmented = segmenter.segment(mp_img)
  category_mask = segmented.category_mask.numpy_view()
  mask = category_mask < 0.2
  alpha_channel = mask.astype(np.uint8) * 255
  result_img = np.dstack((rmg_img, alpha_channel))
  return cv2.cvtColor(result_img, cv2.COLOR_RGBA2BGRA)
