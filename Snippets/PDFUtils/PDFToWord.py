import fitz
import os


def pdf_to_word(pdf_path, word_path):
    """
    将 PDF 文件转为 word 文件
    :param pdf_path: str，PDF 文件路径
    :param word_path: str，word 文件路径
    :return: bool，True 表示转换成功，False 表示转换失败
    """
    if not os.path.exists(pdf_path):
        print(f"{pdf_path} 文件不存在！")
        return False

    # 检查输出路径是否已经存在，如果是，则删除原文件或目录
    if os.path.exists(word_path):
        if os.path.isfile(word_path):
            os.remove(word_path)
        elif os.path.isdir(word_path):
            os.rmdir(word_path)

    try:
        # 打开 PDF 文件
        with fitz.open(pdf_path) as pdf:
            # 创建 word 文档对象
            doc = fitz.open()
            # 遍历 PDF 中的每一页
            for page in pdf:
                # 将当前页转为图像
                pix = page.get_pixmap()
                # 将图像添加到 word 文档中
                img = fitz.Image(fitz.csRGB, pix)
                rect = img.rect
                pdfbytes = img.tobytes()
                img_width, img_height = rect.width, rect.height
                img_matrix = fitz.Matrix(1, 1).preScale(img_width / img.width, img_height / img.height)
                img_clip = fitz.Pixmap(fitz.csRGB, img_matrix, pdfbytes)
                doc.insert_image(rect, pixmap=img_clip)

            # 保存 word 文档
            if not os.path.exists(os.path.dirname(word_path)):
                os.makedirs(os.path.dirname(word_path), exist_ok=True)
            doc.save(word_path)
            doc.close()

            if os.path.exists(word_path):
                return True
            else:
                return False

    except Exception as e:
        print(f"转换失败：{e}")
        return False
