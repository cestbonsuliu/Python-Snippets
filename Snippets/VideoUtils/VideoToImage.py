import cv2
import os
import argparse
import logging

def save_image(image, addr, num):
    address = os.path.join(addr, f"image_{num}.jpg")
    cv2.imwrite(address, image)

def process_video(video_path, output_dir, interval):
    # 如果输出目录不存在，则创建该目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取视频文件
    video = cv2.VideoCapture(video_path)

    # 遍历帧并将选定的帧保存为图像
    i = 0   # 帧计数器
    j = 0   # 图片计数器
    while True:
        success, frame = video.read()
        if not success:
            break

        i += 1
        if i % interval == 0:
            j += 1
            save_image(frame, output_dir, j)
            logging.info(f"已保存第{j}张图片，对应帧数{i}")

    video.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将视频转换为一系列图像")
    parser.add_argument("video_path", help="输入视频文件的路径")
    parser.add_argument("--output_dir", "-o", default="./result", help="保存输出图像的目录")
    parser.add_argument("--interval", "-i", type=int, default=24,
                        help="每n帧采集一帧图像（默认值：24）")
    args = parser.parse_args()

    # 设置日志记录格式和级别
    logging.basicConfig(format="[%(asctime)s] %(message)s", level=logging.INFO)

    process_video(args.video_path, args.output_dir, args.interval)
