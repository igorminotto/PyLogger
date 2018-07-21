from dataBaseConnections.DataBaseEngine import DataBaseEngine
from dataBaseConnections.SQLiteConnection import SQLiteConnection
from dataBaseConnections.DataBaseConfiguration import DataBaseConfigurationBuilder

class DataBaseConnectionFactory():
    def createConnection(self):
        configuration = DataBaseConfigurationBuilder().fromConfigurationFile().build()
        return self.createConnectionFor(configuration)

    def createConnectionFor(self, configuration):
        if configuration.engine == DataBaseEngine.SQLite:
            dataBaseConnection = SQLiteConnection(configuration)
        else:
            raise InvalidDataBaseConfiguration("Engine {engine} not found or not implemented yet.".format(engine=configuration.engine))
        self.__prepareDataBase(dataBaseConnection)
        return dataBaseConnection

    def __prepareDataBase(self, dataBaseConnection):
        dataBaseConnection.execute("""
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL
            )
        """)

class InvalidDataBaseConfiguration(Exception):
    pass