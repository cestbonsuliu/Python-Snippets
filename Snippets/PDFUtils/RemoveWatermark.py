import fitz
from PIL import Image


def remove_watermark(pdf_file: str, new_pdf_file: str):
    """
    去除 PDF 文件中的水印
    :param pdf_file: 待处理的 PDF 文件路径
    :param new_pdf_file: 处理完成后生成的新的 PDF 文件路径
    """
    with fitz.open(pdf_file) as doc:
        for i in range(doc.page_count):
            page = doc[i]
            images = page.get_image_list()
            for image in images:
                img_pil = Image.frombytes("RGB", [image[2], image[3]], image[10])
                # 检查图片是否符合水印特征，如颜色区别不大，像素点密集等
                if 'watermark' in image[7] and check_img(img_pil):
                    page.remove_image(image[0])
        doc.save(new_pdf_file)


def check_img(img_pil):
    # TODO: 根据需要自定义检查方式，比如像素点、颜色区别等
    return True
