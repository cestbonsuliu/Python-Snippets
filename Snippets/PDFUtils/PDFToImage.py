import fitz
import os

# 将PDF转化为图片
def convert_pdf_to_image(pdf_path, output_dir, zoom_x=1.0, zoom_y=1.0, rotation_angle=0):
    try:
        # 检查PDF文件是否存在
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"File {pdf_path} not found.")

        # 创建对应PDF文件的输出目录
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_path = os.path.join(output_dir, pdf_name)
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # 打开PDF文件
        with fitz.open(pdf_path) as doc:
            for page_index in range(doc.page_count):
                page = doc[page_index]
                trans = fitz.Matrix(zoom_x, zoom_y).pre_rotate(rotation_angle)
                pixmap = page.getPixmap(matrix=trans, alpha=False)
                image_path = os.path.join(output_path, f"{page_index}.png")
                pixmap.writePNG(image_path)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    # 调用函数进行测试
    pdf_path = "example.pdf"
    output_dir = "output"
    convert_pdf_to_image(pdf_path, output_dir, zoom_x=2.0, zoom_y=2.0, rotation_angle=90)
