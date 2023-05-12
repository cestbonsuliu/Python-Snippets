import pymysql
from typing import Dict

def update_word_field(word: str, field: str, value: str, mysql_info: Dict[str, str]):
    # 从参数中获取 MySQL 数据库连接信息
    host = mysql_info['host']
    user = mysql_info['user']
    password = mysql_info['password']
    database = mysql_info['database']
    charset = mysql_info['charset']

    # 连接 MySQL 数据库
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        charset=charset
    )

    # 获取数据库操作游标
    cursor = connection.cursor()

    # 根据单词名称查询数据
    sql = "SELECT * FROM words WHERE word=%s"
    cursor.execute(sql, (word,))
    result = cursor.fetchone()

    # 如果找到对应的数据，更新指定字段
    if result:
        id = result[0]
        fields = ["word", "EN_definition", "CN_definition", "phonetic", "audio"]
        if field in fields:
            # 更新数据表中的记录
            sql = f"UPDATE words SET {field}=%s, updated_at=NOW() WHERE id=%s"

            # 使用参数化查询，并将新的值和 ID 作为参数传入
            cursor.execute(sql, (value, id))
            connection.commit()

            print(f"成功更新单词为 {word} 的 {field}")
        else:
            print(f"{field} 字段不存在")
    else:
        print(f"找不到单词为 {word} 的数据")

    # 关闭数据库连接
    connection.close()
