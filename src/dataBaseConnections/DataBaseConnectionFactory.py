from dataBaseConnections.DataBaseEngine import DataBaseEngine

class DataBaseConnectionFactory()
    def createConnectionFor(self, configuration):
        if configuration.engine == DataBaseEngine.SQLite:
            return self.createSQLiteConnectionFor(configuration)
        raise InvalidDataBaseConfiguration("Engine not found or not implemented yet.")

    def createSQLiteConnectionFor(self, configuration):
        yield

class InvalidDataBaseConfiguration(Exception):
    pass