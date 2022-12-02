# !/usr/bin/env python
# -*- coding: cp1252 -*-
import os
import sys
import time
from datetime import datetime
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametros import ControladorParametros
from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.resources.miscelania import Miscel



class ModuloLog:

    var_hora_inicio = None
    var_hora_termino = None
    var_pasta_log = None
    var_notas_encaminhadas = None
    var_notas_processadas = None
    var_duracao_processo = None

    var_total_nao_suportadas = 0
    var_total_importadas = 0
    var_total_excecoes = 0

    @staticmethod
    def gerarNomeArquivoLog() -> str:
        """
        Retorna um nome para um novo arquivo de log
        :return: Nome a ser usado no arquivo de log
        """
        if ModuloLog.log_desabilitado():
            return 

        hora = Miscel.dataHoraAtual()
        data = Miscel.dataAtual()
        
        if (ControladorParametros().obterParametro(EnumParametros.PASTA_SAIDA) == None):
            print('Arquivo de configuração incompleto ou inexistente.')
            print('Preencha o arquivo "nsImportadorTributario.INI.DIST" localizado na pasta raiz do importador e remova a extenção ".DIST" do nome.')
            time.sleep(60)
            sys.exit()
        pasta = ControladorParametros().obterParametro(EnumParametros.PASTA_SAIDA) + "\\" + 'nsImportadorTributario'
        if not os.path.exists(pasta):
            os.mkdir(pasta)
        pasta += "\\" + 'LOG'
        if not os.path.exists(pasta):
                os.mkdir(pasta)
        pasta += "\\" + ControladorParametros().obterParametro(EnumParametros.NOME_BD)
        if not os.path.exists(pasta):
            os.mkdir(pasta)
        pasta += "\\" + data
        if not os.path.exists(pasta):
            os.mkdir(pasta)
        pasta_log = os.path.join(pasta, 'nsImportadorTributario{}.csv'.format(''.join(c for c in hora if c.isdigit())))
        open(pasta_log, "x")
        ModuloLog.var_pasta_log = pasta_log

    @staticmethod
    def iniciarModuloLog():
        if ModuloLog.log_desabilitado():
            return 

        ModuloLog.var_hora_inicio = datetime.now()

        if ModuloLog.var_pasta_log is not None:
            return

        ModuloLog.gerarNomeArquivoLog()
        ModuloLog.info("""### Nasajon Sistemas - nsImportadorTributario ###""")
        ModuloLog.info("Iniciando processamento")

    @staticmethod
    def finalizarModuloLog():
        if ModuloLog.log_desabilitado():
            return 

        ModuloLog.var_hora_termino = datetime.now()
        ModuloLog.var_duracao_processo = (ModuloLog.var_hora_termino - ModuloLog.var_hora_inicio).seconds

        ModuloLog.info("Importação finalizada. Tempo total do processo: " + str(ModuloLog.var_duracao_processo) + " segundos")


    @staticmethod
    def info(mensagem: str):
        """
        Retorna mensagens de erro tratadas
        :param identificador: Identificação (Tipo) do erro
        :param e: Exceção levantada
        :param stackTrace: Stack Trace
        :return: Texto de erro formatado
        """
        if ModuloLog.log_desabilitado():
            return 

        mensagem = 'INFO - {} - {}'.format(Miscel.dataHoraAtual(), mensagem)
        print(mensagem)
        ModuloLog.escreverLog(mensagem)

    @staticmethod
    def aviso(mensagem, razao_social, numero_nota):
        """
        Retorna mensagens de advertência (warning) tratadas
        :param identificador: Identificação (Tipo) do aviso
        :param mensagem: Mensagem ao usuário
        :param stackTrace: Stack Trace
        :return: Mensagem de advertência formatada
        """
        if ModuloLog.log_desabilitado():
            return 

        ModuloLog.escreverLog('AVISO - {} - {} - {} - {}'.format(Miscel.dataHoraAtual(), razao_social, numero_nota, mensagem))

    @staticmethod
    def excecao(mensagem, *args):
        """
        Retorna mensagens de advertência (warning) tratadas
        :param identificador: Identificação (Tipo) do aviso
        :param mensagem: Mensagem ao usuário
        :param stackTrace: Stack Trace
        :return: Mensagem de advertência formatada
        """
        if ModuloLog.log_desabilitado():
            return 

        if len(args) > 0:
            if len(args) == 1:
                ModuloLog.escreverLog('EXCEÇÃO - {} - Diretório do Arquivo: {} - {}'.format(Miscel.dataHoraAtual(), args[0], mensagem))
            elif len(args) == 3:
                ModuloLog.escreverLog('EXCEÇÃO - {} - Diretório do Arquivo: {} - Estabelecimento: {} - Número da Nota: {} - {}'.format(Miscel.dataHoraAtual(), args[0], args[1], args[2], mensagem))
            else:
                ModuloLog.escreverLog('EXCEÇÃO - {} - {}'.format(Miscel.dataHoraAtual(), mensagem))
        else:
            ModuloLog.escreverLog('EXCEÇÃO - {} - {}'.format(Miscel.dataHoraAtual(), mensagem))

    @staticmethod
    def erro(erro, *mensagem):
        """
        Retorna mensagens de advertência (warning) tratadas
        :param identificador: Identificação (Tipo) do aviso
        :param mensagem: Mensagem ao usuário
        :param stackTrace: Stack Trace
        :return: Mensagem de advertência formatada
        """
        if ModuloLog.log_desabilitado():
            return 

        if mensagem != ():
            ModuloLog.escreverLog('ERRO - {} - {} - {}'.format(Miscel.dataHoraAtual(), str(erro), mensagem[0]))
        else:
            ModuloLog.escreverLog('ERRO - {} - {}'.format(Miscel.dataHoraAtual(), str(erro)))

    @staticmethod
    def escreverLog(mensagem):
        if ModuloLog.log_desabilitado():
            return 

        pasta_log = ModuloLog.var_pasta_log
        with open(pasta_log, 'a') as arquivo:
            arquivo.writelines(mensagem + '\n')
        arquivo.close()

    @staticmethod
    def log_desabilitado():
        return ControladorParametros().obterParametro(EnumParametros.DESABILITAR_LOG ) == "True"
          
