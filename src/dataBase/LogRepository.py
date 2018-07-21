from dataBaseConnections.DataBaseConnectionFactory import DataBaseConnectionFactory

class LogRepository():
    def __init__(self, configuration=None):
        if configuration:
            self.connection = DataBaseConnectionFactory().createConnectionFor(configuration)
        else:
            self.connection = DataBaseConnectionFactory().createConnection()
    
    def createLog(self, log):
        query = """
            INSERT INTO logs (message) VALUES (:log)
        """
        self.connection.execute(query, parameters = {"log": log})