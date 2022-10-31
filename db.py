import sqlite3

#connect = sqlite3.connect("accounttant.db", check_same_thread=False)
conn = sqlite3.connect("Sport.db", check_same_thread=False)
cursor = conn.cursor()

def auth_user(user_id):
    if user_exists(user_id):
        cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        conn.commit()
        return "True"
    else return "False"

def user_exists(user_id):
    """Проверяем, есть ли юзер в базе"""
    result = cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id))
    return bool(len(result.fetchall()))

def close():
    """Закрываем соединение с БД"""
    conn.close()