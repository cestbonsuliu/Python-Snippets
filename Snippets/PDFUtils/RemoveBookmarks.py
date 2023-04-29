import PyPDF2

def remove_bookmarks(input_file_path, output_file_path):
    # 打开 PDF 文件
    with open(input_file_path, 'rb') as input_pdf:
        # 读取 PDF 文件
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        try:
            # 检查 PDF 是否有书签
            if '/Outlines' in pdf_reader.trailer['/Root']:
                # 删除书签
                pdf_reader.trailer['/Root'].pop('/Outlines')

            # 创建一个 PDF 写入器
            pdf_writer = PyPDF2.PdfWriter()

            # 将原始 PDF 文件的每一页添加到 PDF 写入器
            for page_num in range(len(pdf_reader.pages)):
                # 添加页面
                pdf_writer.add_page(pdf_reader.pages[page_num])

            # 将 PDF 文件写入输出文件
            with open(output_file_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

        except KeyError:
            print('PDF 文件没有书签！')