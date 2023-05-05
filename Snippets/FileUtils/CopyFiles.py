import os
import shutil

def copy_files_by_type(src_folder, dest_folder, file_type):
    try:
        # 遍历源文件夹及其子文件夹下所有文件
        for root, dirs, files in os.walk(src_folder):
            for file in files:
                # 判断文件是否为需要复制的类型
                if file.endswith(file_type):
                    # 拼接源文件路径和目标文件路径
                    src_file_path = os.path.join(root, file)
                    dest_file_path = os.path.join(dest_folder, file)
                    # 复制文件到目标文件夹下
                    shutil.copy(src_file_path, dest_file_path)
    except Exception as e:
        print(f"复制文件出现异常：{e}")
