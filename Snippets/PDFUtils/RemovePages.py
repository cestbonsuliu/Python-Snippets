import PyPDF2

def remove_pages(input_file_path, output_file_path, start_page=None, end_page=None):
    # 打开 PDF 文件
    with open(input_file_path, 'rb') as input_pdf, open(output_file_path, 'wb') as output_pdf:
        # 读取 PDF 文件
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        # 删除指定页数范围内的页
        if start_page is not None and end_page is not None:
            delete_pages(pdf_reader, start_page, end_page)

        # 创建一个 PDF 写入器
        pdf_writer = PyPDF2.PdfWriter()

        # 将 PDF 文件的每一页添加到 PDF 写入器
        for page_num in range(len(pdf_reader.pages)):
            # 添加页面
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # 将 PDF 文件写入输出文件
        pdf_writer.write(output_pdf)

def delete_pages(pdf_reader, start_page, end_page):
    for i in range(start_page - 1, end_page):
        pdf_reader.pages[i].mediabox.upper_right = (0, 0)
        pdf_reader.pages[i].mediabox.lower_left = (0, 0)
        pdf_reader.pages[i].cropbox.upper_right = (0, 0)
        pdf_reader.pages[i].cropbox.lower_left = (0, 0)

