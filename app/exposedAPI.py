import database as fb



class Api():
    
    def log(self, value):
        print(value)
        fb.startDB()
        fb.AddData()

    """
    def StartAndAddData(self, props):
        fb.startDB()
        fb.AddData()
        fb.createTable(props)
    """
    
    def createTableData(self, dbname, data ):
        """
        Enum
        """
        fb.createTable(dbname, data)