from logDestinations.LogDestination import LogDestination
from dataBase.LogRepository import LogRepository

class DataBaseDestination(LogDestination):
    def __init__(self, configuration=None):
        self.logRepository = LogRepository(configuration)

    def getName(self):
        return self.logRepository.connection.configuration.database
        
    def writeLog(self, log):
        self.logRepository.createLog(log)