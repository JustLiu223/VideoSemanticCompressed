import os
import skimage.io as io
import cv2
import numpy as np
import time

def get_array_inverse(arr1):
    arr = np.array(arr1)
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            if arr1[i][j] == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    return arr


class ImgSplit():
    @staticmethod
    def get_array_im(arr1):
        arr2 = np.array(arr1)
        row = arr2.shape[0]
        col = arr2.shape[1]
        for i in range(0, row):
            for j in range(0, col):
                if arr1[i][j] == 0:
                    arr2[i][j] = 1
                else:
                    arr2[i][j] = 0
        return arr2

    @staticmethod
    def seg_mask_im_macro(arr2):
        arr1 = np.array(arr2)
        row = arr1.shape[0]
        col = arr1.shape[1]
        nrow = int(row / 16)
        ncol = int(col / 16)
        for i in range(nrow):
            for j in range(ncol):
                slice1 = arr1[16 * i:16 * (i + 1), 16 * j:16 * (j + 1)]
                for i1 in range(16):
                    for j1 in range(16):
                        if slice1[i1][j1] == 1:
                            arr1[16 * i:16 * (i + 1), 16 * j:16 * (j + 1)] = 1
                            break
                        break
        return arr1


def color_adjust(img):
    B, G, R = cv2.split(img)
    img = cv2.merge([R, G, B])
    return img


def get_img(img_seg, img_gt):
    arr_im = ImgSplit.get_array_im(img_seg)
    seg_mask_im_macro_old = ImgSplit.seg_mask_im_macro(arr_im)
    im = np.array(seg_mask_im_macro_old)
    seg_mask_im_macro = np.expand_dims(im, 2).repeat(3, axis=2)
    im_images = seg_mask_im_macro * img_gt
    uim = get_array_inverse(im)
    seg_mask_uim_macro = np.expand_dims(uim, 2).repeat(3, axis=2)
    uim_images = seg_mask_uim_macro * img_gt
    return im_images, uim_images


def uim_to_local_img(img, step):
    io.imsave(f'./data/U_im/BA{step:06d}.png', img)


def im_to_local_img(img, step):
    io.imsave(f'./data/im/IA{step:06d}.png', img)


img_gt_folder = 'data/originalImage'
img_seg_folder = 'data/segMasks'
# Get the number of image frames in the 'data/originalImage' directory
image_files = os.listdir(img_gt_folder)
num_frame = len([f for f in image_files if f.endswith('.png')])

if not os.path.exists('./data/U_im'):
    os.makedirs('./data/U_im')

if not os.path.exists('./data/im'):
    os.makedirs('./data/im')

time_start = time.time()

for i in range(num_frame):
    gt_name = f"{i:06d}.png"
    seg_name = f"{i:06d}.png"
    path_gt = os.path.join(img_gt_folder, gt_name)
    path_seg = os.path.join(img_seg_folder, seg_name)

    img_gt = cv2.imread(path_gt, 1)
    img_seg = cv2.imread(path_seg, 0)

    img_im, img_uim = get_img(img_seg, img_gt)
    img_im = color_adjust(img_im)
    img_uim = color_adjust(img_uim)

    im_to_local_img(img_im, i)
    uim_to_local_img(img_uim, i)

time_end = time.time()
time_cost = time_end - time_start

print('Average time cost per frame:', time_cost / num_frame)
