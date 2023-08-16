import os
import subprocess

# To generate video for the original frames
frame_rate = 10

# Use the `-framerate` option to specify the frame rate
# PSNR
# subprocess.run(['ffmpeg', '-i', 'Original_video.mp4','-i', 'Pro_video.mp4'  ,'-filter_complex' ,"psnr" ,'-f','null' ,'-'])
# SSIM
subprocess.run(['ffmpeg', '-i', 'Original_video.mp4','-i', 'Pro_video.mp4'  ,'-lavfi' ,"ssim" ,'-f','null' ,'-'])