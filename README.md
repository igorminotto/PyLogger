# PyLogger
Projeto final da disciplina "Padrões de Projeto e Framework" da pós-graduação em Engenharia de Software da PUC-SP.

## Definição do problema

- Precisa ser fácil usar;
- Precisa ter valores padrão de configuração, porque se eu sair usando sem configurar nada a biblioteca deveria funcionar com algum comportamento padrão;
- Precisa ter um manual basico de como usar;
- Precisa de manual de como configurar os diferentes destinos dos logs:
  - Quero poder mandar os logs para um servidor HTTP, usando POST. Eu preciso conseguir configurar isso se escolher usar o http como destino;
  - Quero poder mandar os logs para o console;
  - Quero poder mandar os logs para banco de dados;
  - Quero poder mandar os logs para um arquivo;
- Quero poder definir o pattern da string da entrada de log. Por exemplo: 
  - TIMESTAMP - LEVEL - MESSAGE
  - LEVEL : TIMESTAMP : DESTINATION: MESSAGE
  - [LEVEL] : TIMESTAMP: LOGGER_NAME : DESTINATION : MESSAGE
