import os

def clear_files(path, ext=None):
    """
    清空指定文件夹中指定类型的文件。
    :param path: 文件夹路径。
    :param ext: 文件扩展名（不包括点号），默认为None，表示清空所有类型的文件。
    """
    # 检查输入参数的合法性
    if not isinstance(path, str) or not os.path.exists(path):
        print(f"Path not found: {path}")
        return
    if ext is not None and not isinstance(ext, str):
        print(f"Invalid file extension: {ext}")
        return

    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and (ext is None or filename.endswith(f".{ext}")):
                # 检查文件是否可以被删除
                if not os.access(file_path, os.W_OK):
                    print(f"Permission denied: {file_path}")
                    continue
                os.remove(file_path)
    except Exception as e:
        print(f"Error occurred: {e}")
