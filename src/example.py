from logger.Logger import Logger
from logger.LogLevel import LogLevel
from logDestinations.ConsoleDestination import ConsoleDestination
from logDestinations.FileDestination import FileDestination
from logDestinations.HttpDestination import HttpDestination
from logDestinations.DataBaseDestination import DataBaseDestination
from dataBaseConnections.DataBaseConfiguration import DataBaseConfigurationBuilder

if __name__=="__main__":
    logger = Logger("Exemplo-Console", ConsoleDestination())
    logger.logDebug("Isto será impresso no console.")

    logger = Logger("Exemplo-Arquivo", FileDestination('../temp/test.log'))
    logger.logInfo("Isto será impresso em um arquivo.")

    logger = Logger("Exemplo-HTTP", HttpDestination('http://www.mocky.io/v2/5b535c8e2f0000d6163bb70e'))
    logger.logWarning("Isto será enviado como parâmetro de uma requisição HTTP.")

    logger = Logger("Exemplo-DB", DataBaseDestination())
    logger.logError("Isto será inserido no banco de dados default")

    configuration = DataBaseConfigurationBuilder().onDataBase('exemplo')
    logger = Logger("Exemplo-DB", DataBaseDestination(configuration))
    logger.logError("Isto será inserido no banco de dados")