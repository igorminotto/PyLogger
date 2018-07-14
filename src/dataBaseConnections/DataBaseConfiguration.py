from dataBaseConnections.DataBaseEngine import DataBaseEngine

class DataBaseConfiguration():
    def __init__(self, engine=None, host=None, database=None, user=None, password=None):
        self.engine = engine or DataBaseEngine.SQLite
        self.host = "localhost"
        self.database = "py_logger"
        self.user = "root"
        self.password = ""

