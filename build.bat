@SET PYTHONPATH=%CD%\src
@SET PARAMS=-y --clean^
 --onefile^
 -p %PYTHONPATH%^
 --name "nsImportadorTributario"^
 --icon src\br\com\nasajon\nsImportadorTributario\resources\icon.ico^
 --distpath "%NSBIN%"^
 --workpath "%NSDCU%"

@SET PARAMS64=-y --clean^
 --onefile^
 -p %PYTHONPATH%^
 --name "nsImportadorTributario64"^
 --icon src\br\com\nasajon\nsImportadorTributario\resources\icon.ico^
 --distpath "%NSBIN%"^
 --workpath "%NSDCU%"

@IF DEFINED JENKINS_HOME (
	@SET PARAMS=%PARAMS% --version-file "%WORKSPACE%\output\VersionInfo2"
)

@IF EXIST venv (
  @CALL @%CD%\venv\Scripts\deactivate.bat
)

@IF EXIST venv64 (
  @CALL @%CD%\venv64\Scripts\deactivate.bat
)

@ECHO ##### Criando o ambiente virtual em 32 bits#####

@python -m venv --clear venv

@ECHO ##### Compilando o projeto em 32 bits #####

@CMD "/c @%CD%\venv\Scripts\activate.bat && @pip install -r requirements.txt && @pyinstaller %PARAMS% src\br\com\nasajon\nsImportadorTributario\main.py && @%CD%\venv\Scripts\deactivate.bat"


@ECHO ##### Criando o ambiente virtual em 64 bits#####

@"C:\Users\bruno\AppData\Local\Programs\Python\Python311\python.exe" -m venv --clear venv64

@ECHO ##### Compilando o projeto em 64 bits #####

@CMD "/c @%CD%\venv64\Scripts\activate.bat && @pip install -r requirements.txt && @pyinstaller %PARAMS64% src\br\com\nasajon\nsImportadorTributario\main.py && @%CD%\venv64\Scripts\deactivate.bat"

pause