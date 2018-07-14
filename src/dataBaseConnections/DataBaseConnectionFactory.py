from dataBaseConnections.DataBaseEngine import DataBaseEngine

class DataBaseConnectionFactory()
    def createConnectionFor(self, configuration):
        if configuration.engine == DataBaseEngine.SQLite:
            return self.createSQLiteConnectionFor(configuration)
        raise InvalidDataBaseConfiguration("Engine not found or not implemented yet.")

    def createSQLiteConnectionFor(self, configuration):
        # http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
        # https://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python
        yield

class InvalidDataBaseConfiguration(Exception):
    pass