from PIL import Image

def generate_webp(path: str, img_paths: str):
  imgs = [Image.open(img_path) for img_path in img_paths]
  imgs[0].save(
    path, 
    format="webp",
    save_all=True, 
    append_images=imgs[1:], 
    loop=0, 
    duration=33,
    quality=80, 
  )
  return path