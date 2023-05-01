import os
import fitz


def encrypt_pdf(pdf_path, password):
    """
    将指定的 PDF 文件加密
    :param pdf_path: str，PDF 文件路径
    :param password: str，PDF 文件密码
    :return: bool，True 表示加密成功，False 表示加密失败
    """
    # 检查 PDF 文件是否存在
    if not os.path.exists(pdf_path):
        print(f"PDF 文件 {pdf_path} 不存在！")
        return False

    try:
        # 打开 PDF 文件
        with fitz.open(pdf_path) as pdf:
            # 遍历每个页面，将其加密
            for i in range(pdf.page_count):
                pdf.authenticate(password)
                pdf.update_page(i)

            # 保存加密后的 PDF 文件
            pdf.save(pdf_path)
            pdf.close()

            if os.path.exists(pdf_path):
                return True
            else:
                return False

    except Exception as e:
        print(f"加密 PDF 文件 {pdf_path} 失败：{e}")
        return False
