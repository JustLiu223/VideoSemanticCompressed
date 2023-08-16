import os
import shutil
from PIL import Image

# 原始图像文件夹路径
raw_image_folder = "dataset/rawImage"
# 目标文件夹路径
target_folder = "data/originalImage"
# 开始索引
start_index = 0

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 获取原始图像文件列表并排序
file_list = os.listdir(raw_image_folder)
file_list.sort()

# 用于重命名的索引计数器
index = start_index

# 遍历原始图像文件并重命名并保存到目标文件夹
for file_name in file_list:
    src_path = os.path.join(raw_image_folder, file_name)
    if os.path.isfile(src_path):
        # 检查文件是否为图像文件
        try:
            image = Image.open(src_path)
            # 生成新的文件名
            new_file_name = '{:06d}.png'.format(index)
            dest_path = os.path.join(target_folder, new_file_name)
            
            # 转换为PNG格式并保存到目标文件夹
            image.save(dest_path)
            print(f"Converted and saved {file_name} as {new_file_name}")
            
            # 更新索引计数器
            index += 1
        except (IOError, SyntaxError):
            print(f"Skipped {file_name} as it is not a valid image file.")

print("重命名和保存完成。")
