import db.db as db, db.dbModels as dbModel
from config import msgs


# Здесь будем прописывать логику маломальскую, 
# данный файл называют ещё core.py
# Как я понял у тебя он назывался логик

def firstMSG(userId)-> str:
    '''Проверка наличия пользователя, ежи нет добавляем'''
    if not db.user_exists(userId):
        db.auth_user(userId)
        return msgs['neofit']
    else:
        return msgs['firstMSG']


def db_conn()->None:
    dbModel.db.connect()
    dbModel.db.create_tables([dbModel.Result, dbModel.TypeExercise])
    dbModel.db.close()


