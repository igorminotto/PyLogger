from logDestinations.LogDestination import LogDestination
from os import path, makedirs

class FileDestination(LogDestination):
    def __init__(self, filepath):
        self.__filepath = path.basename(filepath)
        self.__file = FileDestination.getFile(filepath)

    @staticmethod
    def getFile(filepath):
        dirpath = path.dirname(filepath)
        if not path.exists(dirpath):
            try:
                makedirs(dirpath)
            except OSError:
                raise FileDestinationCannotBeCreatedError("The directories for {file} can't be created.".format(file=filepath))
        try:
            file = open(filepath, 'a+')
        except FileNotFoundError:
            raise FileDestinationCannotBeCreatedError("The file {file} can't be created.".format(file=filepath))
        return file

    def getName(self):
        return self.__filepath
        
    def writeLog(self, log):
        self.__file.write(log + "\n")

class FileDestinationCannotBeCreatedError(Exception):
    pass