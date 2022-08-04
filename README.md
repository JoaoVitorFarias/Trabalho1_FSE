# FSE: Trabalho 1

Trabalho 1 da disciplina de Fundamentos de Sistemas Embarcados (2022/1)

## Descrição

Este trabalho tem por objetivo a criação de um sistema distribuído para o controle e monitoramento de um grupo de sinais de trânsito. O sistema deve ser desenvolvido para funcionar em um conjunto de placas Raspberry Pi com um servidor central responsável pelo controle e interface com o usuário e servidores distribuídos para o controle local e monitoramento dos sinais do cruzamento junto aos respectivos sensores que monitoram as vias. Dentre os dispositivos envolvidos estão o controle de temporizaçãio e acionamento dos sinais de trânsito, o acionmento de botões de passagens de pedestres, o monitoramento de sensores de passagem de carros bem como a velocidade da via e o avanço de sinal vermelho.

[Enunciado do trabalho](https://gitlab.com/fse_fga/trabalhos-2022_1/trabalho-1-2022-1)

## Execução do Projeto

Primeiramente, clone o repositório:

``` git clone https://github.com/JoaoVitorFarias/Trabalho1_FSE.git ```

Para que o projeto seja executado corretamente é preciso rodar o servidor central primeiro, em seguida o servidor distribuído.


### Servidor Central

Para executar o servidor central deve-se navegar até a pasta onde se encontra o código:

``` cd Trabalho1/servidor_central ``` 

Na pasta é necessário executar o arquivo **main.py**, além de informar o IP do host e as portas para cada cruzamento:

``` python main.py <HOST> <PORTA_CRUZAMENTO1> <PORTA_CRUZAMENTO2> <PORTA_CRUZAMENTO3> <PORTA_CRUZAMENTO4> ``` 

exemplo: ``` python main.py 164.41.98.26 10241 10242 10243 10244 ``` 

### Servidor Distribuído

Para executar o servidor distribuído é preciso navegar até a pasta onde se encontra o código:

``` cd Trabalho1/servidor_distribuido ``` 

Na pasta é necessário executar o arquivo **main.py**, além de informar o IP do host e as portas para cada um dos dois cruzamentos:

``` python msin.py <HOST> <PORTA_PRIMEIRO_CRUZAMENTO> <PORTA_SEGUNDO_CRUZAMENTO> ``` 

exemplo: ``` python main.py 164.41.98.26 10243 10244 ``` 

Obs.: Por conta dos 4 cruzamentos estarem divididos em duas placas, cada instância do servidor distribuído só recebe duas portas por parâmetro


