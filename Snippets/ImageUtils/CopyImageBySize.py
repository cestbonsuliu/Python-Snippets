import os
import shutil
from PIL import Image


def copy_images_by_size(src_folder, dest_folder, size, format=None):
    """
    将源文件夹中指定尺寸的图片复制到目标文件夹中。

    Args:
        src_folder (str): 源文件夹路径。
        dest_folder (str): 目标文件夹路径。
        size (tuple): 图片的宽度和高度，例如：(800, 600)。
        format (str): 图片格式，例如："JPEG"、"PNG"等。默认为None，表示不限制图片格式。
    """
    for filename in os.listdir(src_folder):
        filepath = os.path.join(src_folder, filename)
        if os.path.isfile(filepath):
            try:
                with Image.open(filepath) as img:
                    if img.size == size and (not format or img.format == format):
                        shutil.copy2(filepath, dest_folder)
            except (IOError, SyntaxError):
                pass
