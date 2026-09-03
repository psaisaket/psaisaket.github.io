import time
from PIL import Image
import os

image_path = "/Users/sagniktripathy/Documents/imageProcessingBBB/received_img.jpeg"

print("Waiting for incoming image stream from HackRF...")
last_size = -1

while True:
    if os.path.exists(image_path):
        current_size = os.path.getsize(image_path)
        # Check if the file size has stabilized (meaning transmission finished)
        if current_size > 0 and current_size == last_size:
            try:
                img = Image.open(image_path)
                img.show()  # Pops up the image on your screen
                print("Image successfully received and rendered!")
                break
            except Exception:
                # File might still be flushing to disk, keep waiting
                pass
        last_size = current_size
    time.sleep(1)