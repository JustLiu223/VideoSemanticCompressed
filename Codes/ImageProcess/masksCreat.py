import cv2
import numpy as np
import os
from ultralytics import YOLO

def masks_to_png(masks, image_size, save_path_folder, file_name):
    # Create an empty black image with the given size
    png_image = np.zeros((image_size[0], image_size[1]), dtype=np.uint8)

    # Draw each segment on the image
    for segment in masks.xy:
        if len(segment) >= 3:  # A segment needs at least 3 points (x, y)
            points = np.array(segment, dtype=np.int32).reshape((-1, 2))
            cv2.fillPoly(png_image, [points], 255)  # Fill segment with white (255)

    # Create the folder if it doesn't exist
    os.makedirs(save_path_folder, exist_ok=True)

    # Save the PNG image inside the folder
    save_path = os.path.join(save_path_folder, file_name)
    cv2.imwrite(save_path, png_image)

model = YOLO('yolov8x-seg.pt')  # pretrained YOLOv8n model

# Define path to the image file directory
image_dir = 'data/originalImage'
save_path_folder = 'data/segMasks'

# Get a list of all image files in the directory
image_files = os.listdir(image_dir)
image_files.sort()  # Ensure proper ordering if the filenames are not sorted

# Process each image and its corresponding masks
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file).replace('\\', '/')

    # Load the image to obtain its size
    image = cv2.imread(image_path)
    image_size = (image.shape[0], image.shape[1])

    # Run inference on the image to get the masks
    results = model(image_path, save=True)
    masks = results[0].masks

    # Save the masks as PNG images
    file_name = os.path.splitext(image_file)[0] + '.png'  # Use the same name as the image but with .png extension
    masks_to_png(masks, image_size, save_path_folder, file_name)
