from logDestinations.LogDestination import LogDestination

class DataBaseDestination(LogDestination):
    def __init__(self):
        pass

    def getName(self):
        return "Console"
        
    def writeLog(self, log):
        print(log)