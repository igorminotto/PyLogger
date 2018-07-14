from abc import ABC, abstractmethod

class LogDestination(ABC):
    '''
    This class is abstract (Abstract Base Class) and define a generic destination for logging.
    '''

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def writeLog(self, log):
        pass
