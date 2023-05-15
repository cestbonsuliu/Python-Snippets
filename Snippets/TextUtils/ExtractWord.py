import re


def extract_word_pos(raw_str):
    # 按行分割原始字符串
    single = raw_str.split(sep="\n")

    end = ""

    for i in single:
        # 如果该行非空且不包含 "【名】"，则进行处理
        if i and i.find("【名】") == -1:
            # 提取单词词性
            cixing = re.findall(r'\w+\.\s', i)
            # 如果找不到单词词性则跳过该行
            if not cixing:
                continue
            # 去除单词词性后提取中文意思
            re_i = i.replace(cixing[0], "")
            cns = re_i.split("；")
            # 将单词和中文意思拼接后添加到结果字符串中
            for cn in cns:
                end = end + cixing[0] + cn + "\n\n"

    return end


if __name__ == "__main__":
    # 测试代码
    raw_str = """
    n. 码（长度单位，等于 3 英尺或 0.91 米）；（尤指沙等建筑材料的）平方码，立方码；（某种用途的）区域，场地；（小屋的）后院，院子；<北美> 庭院花园；<西印度> 包括房子的庭院；<南非> 出租庭院；城市小区；帆桁；<美，非正式> 100美元，百元钞票；<英，非正式> 苏格兰场（the Yard）；（尤指牙买加侨民之间所指的）祖国，牙买加（Yard）；<美> 庭院花园

    v. <美> 把（木材）堆放（或运至）场内；把（家畜）驱入圈栏；（麋鹿）冬令集居

    【名】 （Yard）（英）亚德（人名）
    """

    new_str = extract_word_pos(raw_str)
    print(new_str)
