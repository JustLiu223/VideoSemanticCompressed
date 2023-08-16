import os
import subprocess

# The folders of the original frames
img_folder = 'data/Afterimage'
# To generate video for the original frames
frame_rate = 10

# Use the `-framerate` option to specify the frame rate
subprocess.run(['ffmpeg', '-framerate', str(frame_rate), '-i', os.path.join(img_folder, '%03d.png'), '-vcodec', 'libx264', '-r', '25','Pro_video.mp4'])