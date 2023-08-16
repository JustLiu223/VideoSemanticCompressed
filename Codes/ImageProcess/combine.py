import os
import skimage.io as io
import cv2

# The folders of the original frames
img_IA_folder = 'data/video/IA'  # Update this with the correct path
img_BA_folder = 'data/video/BA'  # Update this with the correct path

# Get the number of images in the folders
num_images = len([name for name in os.listdir(img_IA_folder) if os.path.isfile(os.path.join(img_IA_folder, name))])

# To get the original name
start_frame = 0
end_frame = num_images - 1  # Subtract 1 to get the correct end_frame

# Output folder for combined images
output_folder = 'data/Afterimage'
os.makedirs(output_folder, exist_ok=True)

for i in range(start_frame, end_frame + 1):
    file_name = "{:03d}.png".format(i)
    path_IA = os.path.join(img_IA_folder, file_name).replace("\\", "/")  # Replace backslashes with forward slashes
    path_BA = os.path.join(img_BA_folder, file_name).replace("\\", "/")  # Replace backslashes with forward slashes
    
    img_IA = cv2.imread(path_IA)
    img_BA = cv2.imread(path_BA)
    
    if img_IA is not None and img_BA is not None:
        # To combine the frames
        img_combined1 = cv2.addWeighted(img_BA, 0.5, img_IA, 0.5, 0)

        # To save the frames with the correct naming
        B, G, R = cv2.split(img_combined1)
        img_combined = cv2.merge([R, G, B])
        io.imsave(os.path.join(output_folder, '{:03d}.png'.format(i)), img_combined)
        print("Saved the image {:03d}.".format(i))
    else:
        print(f"Error: Unable to read one or both images for frame {i}.")

print("All images saved ----- rename !!!")
