
import cv2
import argparse
import os


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='Process pic')
    parser.add_argument('--input', help='video to process', dest='input', default=None, type=str)
    parser.add_argument('--output', help='pic to store', dest='output', default=None, type=str)
    # default为间隔多少帧截取一张图片；我这里用10刚刚好！
    parser.add_argument('--skip_frame', dest='skip_frame', help='skip number of video', default=1.5, type=float)
    # input为输入视频的路径 ，output为输出存放图片的路径
    # args = parser.parse_args(['--input', r'E:/internship/LeftCamera.avi', r'--output', 'E:/internship/pin2cyl/'])
    args = parser.parse_args(['--input', r'BA_video.mp4', r'--output', './data/video/IA'])
    return args


def process_video(i_video, o_video, num):
    cap = cv2.VideoCapture(i_video)
    num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    expand_name = '.png'
    sur_name = ''
    if not cap.isOpened():
        print("Please check the path.")
    cnt = 0
    count = 0
    while 1:
        ret, frame = cap.read()
        cnt += 1
 
        if cnt % num == 0:
            count += 1
#            cv2.imwrite(os.path.join(o_video, sur_name + str(count) + expand_name), frame)
            if count < 10:
                cv2.imwrite(os.path.join(o_video, sur_name + str("00") + str(count) + expand_name), frame)
            elif count >= 10 and count < 100:
                cv2.imwrite(os.path.join(o_video, sur_name + str("0") + str(count) + expand_name), frame)
            else:
                cv2.imwrite(os.path.join(o_video, sur_name + str(count) + expand_name), frame)

        if not ret:
            break


if __name__ == '__main__':
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    print('Called with args:')
    print(args)
    process_video(args.input, args.output, args.skip_frame)
