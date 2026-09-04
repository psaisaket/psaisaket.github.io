from PIL import Image
import numpy as np
import sys

def convert_to_bin(image_path, output_bin, size=(128, 128)):
    # 1. Open the image and convert to Grayscale (1 byte per pixel)
    img = Image.open(image_path).convert('L')
    
    # 2. Resize it so we know the exact dimensions for the receiver
    img = img.resize(size)
    
    # 3. Convert to a numpy array of 8-bit unsigned integers (0-255)
    pixel_data = np.array(img, dtype=np.uint8)
    
    # 4. Save the raw bytes directly to a .bin file
    pixel_data.tofile(output_bin)
    
    print(f"Success! {image_path} converted to {output_bin}")
    print(f"Dimensions: {size[0]}x{size[1]}")
    print(f"Total Bytes to transmit: {len(pixel_data.tobytes())}")

if __name__ == "__main__":
    # Usage: python3 make_bin.py my_photo.jpg test_image.bin
    if len(sys.argv) < 3:
        print("Usage: python3 make_bin.py <input_image> <output.bin>")
    else:
        convert_to_bin(sys.argv[1], sys.argv[2])