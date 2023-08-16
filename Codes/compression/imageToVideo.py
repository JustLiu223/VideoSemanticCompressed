import os
import subprocess

# The folders of the original frames
img_folder = 'data/originalImage'
img_IA_folder = 'data/im'
img_BA_folder = 'data/U_im'

# To generate video for the original frames
frame_rate = 10

# Use the `-framerate` option to specify the frame rate
subprocess.run(['ffmpeg', '-framerate', str(frame_rate), '-i', os.path.join(img_folder, '%06d.png'), '-vcodec', 'libx264', '-r', '25','Original_video.mp4'])

# To generate video for BA images with crf=23
subprocess.run(['ffmpeg', '-framerate', str(frame_rate),'-f', 'image2', '-i', os.path.join(img_BA_folder, 'BA%06d.png'), '-vcodec', 'libx264', '-crf', '12', '-r', '25', 'BA_video.mp4'])

# To generate video for IA images with crf=18
subprocess.run(['ffmpeg', '-framerate', str(frame_rate),'-f', 'image2', '-i', os.path.join(img_IA_folder, 'IA%06d.png'), '-vcodec', 'libx264', '-crf', '45', '-r', '25', 'IA_video.mp4'])
