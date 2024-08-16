from peewee import *
import json5

useDatabase = False

db = SqliteDatabase('./data/data.db')

class Data(Model):
    name = CharField()
    birthday = CharField()

    class Meta:
        database = db # This model uses the "data.db" database.
        db_table = 'names' # this will change the table name

def startDB():
    global db
    if (useDatabase == True):
        db.connect()
        db.create_tables([Data])
    
"""

def createTable(props):
    js_obj = json5.loads(props)
    
    print(js_obj)
    
    class ClassName(Model):


        class Meta:
            database = db
            db_table = "namesss"


"""

    
def AddData():
    if (useDatabase == True):
        uncle_bob = Data(name='Bob', birthday='May')
        uncle_bob.save()


def CanUseDatabase():
    global useDatabase
    useDatabase = True