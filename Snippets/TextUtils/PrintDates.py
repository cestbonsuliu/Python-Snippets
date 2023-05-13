from datetime import datetime, timedelta

def print_dates_with_weekday(start_date_str, end_date_str):
    """
    打印起始日期和终止日期之间的每一天的日期和星期
    :param start_date_str: 起始日期字符串，格式为"YYYY-MM-DD"
    :param end_date_str: 终止日期字符串，格式为"YYYY-MM-DD"
    """
    weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    try:
        # 将输入的日期字符串转换为日期对象
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        print("日期格式不正确，请重新输入")
        return

    # 计算日期之间的天数
    days = (end_date - start_date).days

    # 依次打印每一天的日期和星期
    for i in range(days + 1):
        date = start_date + timedelta(i)
        weekday = weekdays[date.weekday()]
        print(date.strftime("%Y年%m月%d日"), weekday)