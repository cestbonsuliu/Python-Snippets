def split_string(long_str:str, str1:str, str2:str) -> tuple:
    # 参数类型检查
    if not isinstance(long_str, str) or not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("输入参数为字符串类型")

    # 字符串长度检测
    if len(long_str) == 0 or len(str1) == 0 or len(str2) == 0:
        raise ValueError("字符串为空")

    # 找到str1和str2在long_str中的位置
    idx1 = long_str.find(str1)
    idx2 = long_str.find(str2)

    # 如果没有找到，返回None
    if idx1 == -1 or idx2 == -1:
        return None

    # 确保idx1 < idx2
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1

    # 切分字符串并返回
    part1 = long_str[:idx1+len(str1)]
    part2 = long_str[idx1+len(str1):idx2]
    part3 = long_str[idx2:]

    return (part1, part2, part3)
