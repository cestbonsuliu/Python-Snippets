from PIL import Image
import os

# 将图片合并为PDF
def convert_image_to_pdf(image_dir, output_path):
    try:
        # 检查输入目录是否存在
        if not os.path.exists(image_dir):
            raise FileNotFoundError(f"Directory {image_dir} not found.")

        # 获取所有图片文件
        image_files = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('png', 'jpg'))])

        # 打开第一张图片
        with Image.open(image_files[0]) as img:
            # 保存成PDF文件
            img.save(output_path, "pdf", save_all=True, append_images=[Image.open(f).convert("RGB") for f in image_files[1:]])
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # 调用函数进行测试
    image_dir = "input"
    output_path = "output.pdf"
    convert_image_to_pdf(image_dir, output_path)
