# import db.db_old as db_old, db.database as dbModel
from config import msgs


# Здесь будем прописывать логику маломальскую, 
# данный файл называют ещё core.py
# Как я понял у тебя он назывался логик

def firstMSG(userId)-> str:
    return msgs['neofit']
    # '''Проверка наличия пользователя, ежи нет добавляем'''
    # if not db_old.user_exists(userId):
    #     db_old.auth_user(userId)
    #     return msgs['neofit']
    # else:
    #     return msgs['firstMSG']



