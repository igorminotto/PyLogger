from LogLevel import LogLevel
from logDestinations.ConsoleDestination import ConsoleDestination
from datetime import datetime

class Logger():
    def __init__(self, name=None, destination=None, pattern=None):
        self.__name = name or "Logger"
        self.__destination = destination or ConsoleDestination()
        self.__pattern = Logger.translatePattern(pattern or "[%T] %N at %D with level %L: %M")

    @staticmethod
    def translatePattern(pattern):
        translations = {
            "%D": "DESTINATION",
            "%T": "TIMESTAMP",
            "%L": "LEVEL",
            "%N": "LOGGER_NAME",
            "%M": "MESSAGE"
        }
        for old, new in translations.items():
            pattern = pattern.replace(old, "{{{0}}}".format(new))
        return pattern

    def __getTimestamp(self):
        return str(datetime.now())

    def __createLog(self, level, message):
        return self.__pattern.format(
            TIMESTAMP=self.__getTimestamp(), 
            LEVEL=level.name, 
            LOGGER_NAME=self.__name, 
            DESTINATION=self.__destination.getName(), 
            MESSAGE=message
        )

    def __writeLog(self, level, message):
        log = self.__createLog(level, message)
        self.__destination.writeLog(log)


    def logDebug(self, message):
        self.__writeLog(LogLevel.DEBUG, message)

    def logInfo(self, message):
        self.__writeLog(LogLevel.INFO, message)
    
    def logWarning(self, message):
        self.__writeLog(LogLevel.WARNING, message)
    
    def logError(self, message):
        self.__writeLog(LogLevel.ERROR, message)