import os
import fitz


def decrypt_pdf(pdf_path, password):
    """
    将指定的 PDF 文件解密
    :param pdf_path: str，PDF 文件路径
    :param password: str，PDF 文件密码
    :return: bool，True 表示解密成功，False 表示解密失败
    """
    # 检查 PDF 文件是否存在
    if not os.path.exists(pdf_path):
        print(f"PDF 文件 {pdf_path} 不存在！")
        return False

    try:
        # 打开 PDF 文件
        with fitz.open(pdf_path) as pdf:
            # 验证 PDF 文件密码是否正确
            if not pdf.is_locked:
                print(f"PDF 文件 {pdf_path} 未加密，无需解密！")
                return False

            if not pdf.authenticate(password):
                print(f"PDF 文件 {pdf_path} 密码错误，解密失败！")
                return False

            # 保存解密后的 PDF 文件
            pdf.save(pdf_path)
            pdf.close()

            if os.path.exists(pdf_path):
                return True
            else:
                return False

    except Exception as e:
        print(f"解密 PDF 文件 {pdf_path} 失败：{e}")
        return False
