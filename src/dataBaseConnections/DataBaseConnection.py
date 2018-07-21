from abc import ABC, abstractmethod

class DataBaseConnection(ABC):
    def __init__(self, configuration):
        self.configuration = configuration
        self.connect()

    def __del__(self):
        self.disconnect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query, parameters=None):
        pass