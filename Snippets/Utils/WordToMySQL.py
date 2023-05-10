import pymysql
from typing import Dict


def insert_word_to_mysql(word_info: Dict[str, str], mysql_info: Dict[str, str]) -> bool:
    """
    向MySQL数据库中插入一条单词记录

    Args:
        word_info: 包含单词信息的字典，需要包括note_id, word, pronunciation, etymology, difficulty_ranking,
            EN_definition, CN_definition, image_url, word_family, homonyms, synonyms, antonyms, discriminate,
            phrase, example_sentence, forgotten, remembered
        mysql_info: 包含MySQL数据库连接信息的字典，需要包括host, user, password, database

    Returns:
        True表示插入成功，False表示插入失败
    """

    # 检查单词信息是否完整
    required_fields = ["note_id", "word", "pronunciation", "etymology", "difficulty_ranking",
                       "EN_definition", "CN_definition", "image_url", "word_family", "homonyms", "synonyms",
                       "antonyms", "discriminate", "phrase", "example_sentence", "forgotten", "remembered"]
    for field in required_fields:
        if field not in word_info:
            print(f"Error: Missing required field '{field}' in word_info.")
            return False

    # 检查MySQL连接信息是否完整
    required_fields = ["host", "user", "password", "database"]
    for field in required_fields:
        if field not in mysql_info:
            print(f"Error: Missing required field '{field}' in mysql_info.")
            return False

    # 尝试连接MySQL数据库
    try:
        conn = pymysql.connect(
            host=mysql_info["host"],
            user=mysql_info["user"],
            password=mysql_info["password"],
            database=mysql_info["database"],
            charset="utf8"
        )
    except Exception as e:
        print(f"Error: Failed to connect to MySQL database. {e}")
        return False

    # 获取游标
    cursor = conn.cursor()

    # 定义插入单词的SQL语句
    sql = """
        INSERT INTO words (note_id, word, pronunciation, etymology, difficulty_ranking, EN_definition,
        CN_definition, image_url, word_family, homonyms, synonyms, antonyms, discriminate, phrase, example_sentence,
        forgotten, remembered, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """

    # 执行插入操作
    try:
        cursor.execute(sql, (word_info["note_id"], word_info["word"], word_info["pronunciation"], word_info["etymology"],
                             word_info["difficulty_ranking"], word_info["EN_definition"], word_info["CN_definition"],
                             word_info["image_url"], word_info["word_family"], word_info["homonyms"], word_info["synonyms"],
                             word_info["antonyms"], word_info["discriminate"], word_info["phrase"], word_info["example_sentence"],
                             word_info["forgotten"], word_info["remembered"]))
    except Exception as e:
        print(f"Error: Failed to insert word to MySQL database. {e}")
        return False

    # 提交事务
    conn.commit()

    # 关闭游标和连接
    cursor.close()
    conn.close()

    return True
