from dataBaseConnections.DataBaseConnection import DataBaseConnection
import sqlite3

class SQLiteConnection(DataBaseConnection):
    connection = None

    def __init__(self, configuration):
        super(SQLiteConnection, self).__init__(configuration)

    def connect(self):
        database = self.configuration.database + ".db"
        databasePath = "../temp/{file}".format(file=database)
        self.connection = sqlite3.connect(databasePath)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute(self, query, parameters=None):
        cursor = self.connection.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)