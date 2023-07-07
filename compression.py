import base64
import gzip
import os
from tkinter import Tk, filedialog
from PIL import Image

def compress_image(image_path, compressed_file):
    # Encode the image as Base64
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    encoded_data = base64.b64encode(image_data)

    # Compress the Base64 encoded data
    with open(compressed_file, "wb") as compressed_image:
        compressed_image.write(encoded_data)

def decompress_image(compressed_file, output_path):
    # Decompress the compressed file
    with open(compressed_file, "rb") as compressed_image:
        encoded_data = compressed_image.read()

    # Decode the Base64 encoded data and save as an image
    decoded_data = base64.b64decode(encoded_data)
    with open(output_path, "wb") as output_file:
        output_file.write(decoded_data)

# Select file for compression or decompression
root = Tk()
root.withdraw()

choice = input("Choose an option:\n1. Compress\n2. Decompress\n")

if choice == "1":
    # Compress
    input_file = filedialog.askopenfilename()
    output_file = input("Enter the name of the compressed file: ")

    # Check if the selected file is an image or a normal text file
    is_image = False
    try:
        Image.open(input_file)
        is_image = True
    except IOError:
        pass

    if is_image:
        # Compress the image file
        compress_image(input_file, output_file)
        print("Compression completed!")
    else:
        # Compress the normal text file
        with open(input_file, "rb") as file:
            data = file.read()
        with open(output_file, "wb") as compressed_file:
            compressed_file.write(data)
        print("Compression completed!")

elif choice == "2":
    # Decompress
    input_file = filedialog.askopenfilename()
    output_file = input("Enter the name of the decompressed file: ")

    # Check if the selected file is a compressed image or a normal compressed file
    is_image = False
    try:
        with open(input_file, "rb") as file:
            encoded_data = file.read()
        base64.b64decode(encoded_data)
        is_image = True
    except (ValueError, TypeError):
        pass

    if is_image:
        # Decompress the compressed image file
        decompress_image(input_file, output_file)
        print("Decompression completed!")
    else:
        # Decompress the normal compressed file
        with open(input_file, "rb") as compressed_file:
            data = compressed_file.read()
        with open(output_file, "wb") as file:
            file.write(data)
        print("Decompression completed!")

else:
    print("Invalid choice!")
