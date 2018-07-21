from dataBaseConnections.DataBaseEngine import DataBaseEngine
from configparser import ConfigParser

class DataBaseConfiguration():
    def __init__(self, engine, host, database, user, password):
        self.engine = engine
        self.host = host
        self.database = database
        self.user = user
        self.password = password 

class DataBaseConfigurationBuilder():
    engine = DataBaseEngine.SQLite
    host = "localhost"
    database = "py_logger"
    user = "root"
    password = ""

    def withEngine(self, engine):
        self.engine = engine
        return self

    def fromHost(self, host):
        self.host = host
        return self

    def onDataBase(self, database):
        self.database = database
        return self

    def auth(self, user, password):
        return self.withUser(user).withPassword(password)

    def withUser(self, user):
        self.user = user
        return self

    def withPassword(self, password):
        self.password = password
        return self

    def fromConfigurationFile(self, filename=None):
        filename = filename or "database.ini"
        filepath = "../conf/{0}".format(filename)

        config = ConfigParser()
        config.read(filepath)

        databaseSection = config["database"]
        if "engine" in databaseSection:
            engine = DataBaseEngine[databaseSection["engine"]]
            self.withEngine(engine)
        if "host" in databaseSection:
            self.fromHost(databaseSection["host"])
        if "database" in databaseSection:
            self.onDataBase(databaseSection["database"])
        if "user" in databaseSection:
            self.withUser(databaseSection["user"])
        if "password" in databaseSection:
            self.withUser(databaseSection["password"])

        return self

    def build(self):
        dataBaseConfiguration = DataBaseConfiguration(self.engine, self.host, self.database, self.user, self.password)
        return dataBaseConfiguration
