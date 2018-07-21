# PyLogger

## Introdução

Um logger simples para a linguagem Python.

_Este é o projeto final da disciplina "Padrões de Projeto e Framework" da pós-graduação em Engenharia de Software da PUC-SP, do ano de 2018._

## Istalação

Baixe esse projeto utilizando o git:

```bash 
$ git clone https://github.com/igorminotto/PyLogger.git
```

Após isso, acesse o diretório PyLogger. 
Esse projeto depende do [pipenv](https://github.com/pypa/pipenv), um alternativa mais simples ao pip.
Após instalar o pipenv, execute o comando na raiz do projeto:

```bash 
$ pipenv install
```

## Modo de usar

### Comportamento padrão

O comportamento padrão do logger é imprimir a saída no console. Veja o exemplo:

```python
from logger.Logger import Logger

logger = Logger()

logger.logDebug("Isto será impresso no console.")
# [2018-07-21 14:29:45.415818] Logger at Console with level DEBUG: Isto será impresso no console.

logger.logInfo("Isto é uma informação qualquer.")
logger.logWarning("Isto é um alerta.")
logger.logError("Isto é um erro.")
```

### Saída no console

```python
from logger.Logger import Logger
from logDestinations.ConsoleDestination import ConsoleDestination

logger = Logger(name="Exemplo-Console", destination=ConsoleDestination())
logger.logInfo("Isto será impresso no console.")
```

### Saída em um arquivo

```python
from logger.Logger import Logger
from logDestinations.FileDestination import FileDestination

logger = Logger(destination=FileDestination('../temp/test.log'))
logger.logInfo("Isto será impresso no arquivo test.log.")
```

### Saída em um banco de dados

No momento, apenas o conector do SQLite foi implementado.

```python
from logger.Logger import Logger
from logDestinations.DataBaseDestination import DataBaseDestination
from dataBaseConnections.DataBaseConfiguration import DataBaseConfigurationBuilder

configuration = DataBaseConfigurationBuilder().onDataBase('exemplo')
logger = Logger(destination=DataBaseDestination(configuration))
logger.logInfo("Isto será inserido no banco de dados.")
```
### Saída através de uma requisição HTTP

Será feita uma requisição POST para a URL definida, passando o parâmetro "log" com a mensagem formatada.

```python
from logger.Logger import Logger
from logDestinations.HttpDestination import HttpDestination

logger = Logger("Exemplo-HTTP", HttpDestination('http://www.mocky.io/v2/5b535c8e2f0000d6163bb70e'))
logger.logInfo("Isto será enviado como parâmetro de uma requisição HTTP.")
```

### Definindo a formatação

A formatação aceita uma string com 5 marcadores:
- %T para o timestamp
- %N para o nome do logger
- %D para o destino
- %L para o level do log
- %M para a mensagem

```python
logger = Logger(pattern="[%T] %N at %D with level %L: %M")
# Ex.: [2018-07-21 14:29:45.415818] Logger at Console with level DEBUG: Esta é a mensagem.

logger = Logger(pattern="[%L] : %T : %N : %D: %M")
# Ex.: [DEBUG] : 2018-07-21 14:29:45.415818 : Logger : Console : Esta é a mensagem.
```
