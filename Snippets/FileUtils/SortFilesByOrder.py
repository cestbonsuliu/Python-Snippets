import os


def sort_files_by_order(dir_path, order):
    """
    dir_path: 目录路径
    order: 排序顺序，取值可以是 'asc' 或 'desc'
    return: 排序后的文件列表
    """
    # 获取目录下的所有文件名
    files = os.listdir(dir_path)

    # 排序文件列表
    if order == 'asc':
        sorted_files = sorted(files)
    elif order == 'desc':
        sorted_files = sorted(files, reverse=True)
    else:
        raise ValueError("排序顺序只能是 'asc' 或 'desc'")

    return sorted_files
