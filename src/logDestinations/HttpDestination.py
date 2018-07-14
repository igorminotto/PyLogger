import requests
from logDestinations.LogDestination import LogDestination

class HttpDestination(LogDestination):
    def __init__(self, url):
        self.__url = url

    def getName(self):
        return self.__url
        
    def writeLog(self, log):
        try:
            requests.post(self.__url, params={log: log})
        except:
            raise HttpDestinationCannotBeReachedError("The URL {url} could not be reached.".format(url=self.__url))

class HttpDestinationCannotBeReachedError(Exception):
    pass