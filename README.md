
# Importador Tributário
Módulo de importação de configurações tributárias


## Utilização em ambiente de Produção

1. Configure o arquivo nsImportadorTributario.ini na pasta raiz do sistema, substituindo os valores:
    ```
    [BANCO_DE_DADOS]
    Banco = PostgreSQL
    Servidor = <IP DO SERVIDOR>
    Nome_Banco = <BANCO DE DADOS>
    Usuario = <USUARIO BANCO>
    Senha = <SENHA BANCO>
    Porta = <PORTA BANCO>
    
    [GERAL]
	Arquivo Dados = <CAMINHO DA PLANILHA COM AS CONFIGURAÇÕES DE ENTRADA>
    Pasta_Log = <PASTA PARA LOG DE EXECUÇÃO>
    ``` 
2. Execute o arquivo ..\importador_tributario\src\br\com\nasajon\nsImportadorTributario\importador_tributario.bat


## Configurando o Ambiente de Desenvolvimento
1. Instale o Python 3.7.x na distribuição "Windows x86-64 executable installer".
    1.1 O download pode ser feito por esse link (https://www.python.org/downloads/windows/)
    1.2 Durante a instalação, marque a opção 'Add Python 3.7 to PATH'
    1.3 Reinicie o computador
2. Instale as extensões psycopg2 e PyInstaller via CMD.
	2.1 Psycopg2:
	>Python -m pip install psycopg2
	
	2.2 PyInstaller:
	>Python -m pip install pyinstaller
	
    2.2 Caso o proxy esteja bloqueando a instalação da extensão psycopg2 , abra o CMD na pasta raiz do projeto e execute o comando
    >Python -m pip install psycopg2_binary-2.8.2-cp37-cp37m-win_amd64.whl
          
3. Clone o repositório localmente
4. Instale e configure o VsCode
	4.1 O VsCode pode ser baixado por esse link (https://code.visualstudio.com/download)
	4.2 Com o VsCode aberto, abra a raiz do repositório como raiz do projeto
	4.3 Com o VsCode aberto, vá na aba Extensões (No menu lateral esquerdo), pesquise por Python e instale
	4.4 O script de execução do projeto é /src/br/com/nasajon/nsImportadorTributario/main.py. Basta executar com F5. É possível utilizar breakpoints
5. Faça uma cópia local do arquivo src/br/nasajon/nsImportadorTributario.ini.dist, renomeando para "nsImportadorTributario.ini", e ajuste seu conteúdo conforme o ambiente de sua máquina (parâmetros de banco de dados, Logs)


## Utilização em ambiente de desenvolvimento

### Executando o Importador
Para rodar o importador em seu ambiente de desenvolvimento, após configurar o arquivo .ini conforme citado acima, basta rodar o seguinte comando:

> python <repositorio_dir>/src/br/com/nasajon/nsImportadorTributario/main.py


### Gerando o executável
O Importador Tributário utiliza a extensão PyInstaller para gerar executáveis no Windows. O programa pode ser gerado através do "Build.bat" localizado na pasta raiz do projeto. Caso encontre qualquer inconsistência durante a execução verifique se as instalações do Python e PyInstaller foram feitas corretamente, além do PATH contido nas variáveis de ambiente.