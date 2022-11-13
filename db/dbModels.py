from peewee import *


# SQLite database using WAL journal mode and 64MB cache.
db = SqliteDatabase('db/Sport.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class BaseModel(Model):
    class Meta:
        database = db


class TypeExercise(BaseModel):
    name = CharField(max_length=50)


class Result(BaseModel):
    user_id = IntegerField()
    number_pullups = IntegerField(default=0)
    number_approaches = IntegerField(default=0)
    datetime_add = DateField(formats='%Y-%m-%d')
    type_exercise_id = ForeignKeyField(TypeExercise, backref='results', null=True)

    class Meta:
        # проверка чтобы в одно записи количество раз и подходов были в разумной пределе
        constraints = [Check('number_pullups between 0 and 100'), Check('number_approaches between 0 and 100')]
