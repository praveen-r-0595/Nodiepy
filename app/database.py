from peewee import *
import json5
from playhouse.migrate import *

useDatabase = False

db = SqliteDatabase('app/data/data.db') # Database Location from root directory - Nodiepy

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
    

# The below function is to dynamically create a table in sqlite db
def createTable(dbname, props):

    """
    This Code

    """

    global db
    print(props)
    jsObj = json5.loads(props)

    keys = list(jsObj.keys())
    value = list(jsObj.values())

    migrator = SqliteMigrator(db)

    class ClassName(Model):
       
        class Meta:
            database = db
            db_table = dbname

    db.connect()
    db.create_tables([ClassName])
    
    for key, value in jsObj.items():
        
        currentField = findField(value)

        migrate(
            migrator.add_column(dbname, str(key), currentField)
        )


def findField(checkValue):
   
    match checkValue:
            case 'integer':
                field = IntegerField(default = 0)
                return field
            case "text":
                field = CharField(default = "data")
                return field
            case "date":
                field = DateField(default = None)
                return field
            case "boolean":
                field = IntegerField(default = 0)
                return field
            case "largetext":
                field = TextField(default = "desc")
                return field
            case "time": 
                field = TimeField(default = None)
                return field

    
    
def AddData():
    if (useDatabase == True):
        uncle_bob = Data(name='Bob', birthday='May')
        uncle_bob.save()


def CanUseDatabase():
    global useDatabase
    useDatabase = True