import os
import datetime
from pathlib import Path

def backup_folder(folder_path: str, save_path: str) -> None:
    """
    备份指定文件夹及其子文件夹中的所有文件名到文本文件中。

    Args:
        folder_path (str): 要备份的文件夹路径。
        save_path (str): 要保存的文件夹路径。

    Raises:
        FileNotFoundError: 如果要备份的文件夹不存在，抛出此错误。
        PermissionError: 如果没有足够权限访问要保存的文件夹，抛出此错误。
        OSError: 如果保存文件时出现其他错误，抛出此错误。
    """

    # 检查要备份的文件夹是否存在
    if not Path(folder_path).exists():
        raise FileNotFoundError(f"{folder_path} 文件夹不存在！")

    # 获取当前日期时间字符串
    now = datetime.datetime.now()
    date_time_str = now.strftime("%Y%m%d%H%M%S")

    # 检查要保存的文件夹是否存在，不存在则创建
    save_dir = Path(save_path)
    if not save_dir.exists():
        save_dir.mkdir(parents=True, exist_ok=True)

    # 指定要备份的文本文件路径
    file_path = save_dir / (date_time_str + ".txt")

    try:
        # 打开文本文件，使用with语句进行上下文管理
        with open(file_path, "w", encoding="utf-8") as f:

            # 遍历文件夹及其子文件夹所有信息，并写入文本文件
            for dirpath, dirnames, filenames in os.walk(folder_path):
                level = dirpath.replace(folder_path, "").count(os.sep)
                indent = " " * 4 * level
                f.write("{}{}\\\n".format(indent, os.path.basename(dirpath)))
                subindent = " " * 4 * (level + 1)
                for filename in filenames:
                    f.write("{}{}\n".format(subindent, filename))

    except FileNotFoundError as e:
        raise FileNotFoundError(f"无法打开文件：{file_path}\n{e}")

    except PermissionError as e:
        raise PermissionError(f"没有足够的权限访问文件夹：{save_path}\n{e}")

    except OSError as e:
        raise OSError(f"保存文件时发生错误：{file_path}\n{e}")
