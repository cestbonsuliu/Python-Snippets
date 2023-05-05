import re

def replace_img_tag(string):
    """
    将字符串中的<img>标签替换成Markdown格式的图片链接。
    :param string: 待处理的字符串。
    :return: 处理后的字符串。
    """
    pattern = r'<img.*?src="(.*?)".*?>'
    matches = re.findall(pattern, string)
    for match in matches:
        replaced_string = '![]({})'.format(match)


    return replaced_string



if __name__ == "__main__":

    string = r"""
<img width="962" height="296" src=":/96ff0891e1dd4453b3a1a3e48c772738" class="jop-noMdConv">
    
    """



    print(replace_img_tag(string))

