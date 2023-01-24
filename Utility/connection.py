import sys
sys.path.insert(1,'C://Users//Dani Jurma//Desktop//project_newVersion//Utility')
import adminCredentials as admin
import pymysql

class connection:
    def __init__(self):
        self.host = admin.host
        self.user = admin.user
        self.password = admin.password
        self.database = admin.database

    def connectToMySQL(self):
        connectionObject = connection()
        newConnection = pymysql.connect(
            host=connectionObject.host,
            user=connectionObject.user,
            password=connectionObject.password,
            database=connectionObject.database
        )
        return newConnection
    
