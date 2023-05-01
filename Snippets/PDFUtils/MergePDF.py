import os
import fitz


def merge_pdfs(input_dir, output_path):
    """
    将指定目录下所有的 PDF 文件合并为一个文件
    :param input_dir: str，包含待合并 PDF 文件的目录
    :param output_path: str，合并后的输出文件路径
    :return: bool，True 表示合并成功，False 表示合并失败
    """
    # 检查输入目录是否存在
    if not os.path.exists(input_dir):
        print(f"输入目录 {input_dir} 不存在！")
        return False

    # 获取目录下所有的 PDF 文件路径
    pdf_paths = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if f.endswith(".pdf")]

    # 如果没有找到 PDF 文件，则返回 False
    if not pdf_paths:
        print(f"目录 {input_dir} 下没有找到 PDF 文件！")
        return False

    # 排序 PDF 文件的列表
    pdf_paths.sort()

    try:
        # 创建输出 PDF 文件对象
        pdf_out = fitz.open()

        # 将所有 PDF 文件添加到输出文件中
        for path in pdf_paths:
            with fitz.open(path) as pdf:
                pdf_out.insert_pdf(pdf)

        # 保存输出 PDF 文件
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdf_out.save(output_path)
        pdf_out.close()

        if os.path.exists(output_path):
            return True
        else:
            return False

    except Exception as e:
        print(f"合并 PDF 文件失败：{e}")
        return False
