from logDestinations.LogDestination import LogDestination

class ConsoleDestination(LogDestination):
    def getName(self):
        return "Console"
        
    def writeLog(self, log):
        print(log)