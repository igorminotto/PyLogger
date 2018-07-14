from Logger import Logger
from LogLevel import LogLevel
from logDestinations.ConsoleDestination import ConsoleDestination
from logDestinations.FileDestination import FileDestination
from logDestinations.HttpDestination import HttpDestination

if __name__=="__main__":
    logger = Logger("Exemplo-Console", ConsoleDestination())
    logger.logDebug("Isto será impresso no console.")

    logger = Logger("Exemplo-Arquivo", FileDestination('../temp/test.log'))
    logger.logInfo("Isto será impresso em um arquivo.")

    logger = Logger("Exemplo-HTTP", HttpDestination('http://localhost:8000/saveLog'))
    #logger.logWarning("Isto será enviado como parâmetro de uma requisição HTTP.")

    
