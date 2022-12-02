#!/usr/bin/env python
# -*- coding: cp1252 -*-
import configparser
import os
import sys

from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.resources.miscelania import Miscel
from src.br.com.nasajon.resources.singleton import Singleton


class ControladorParametros(metaclass=Singleton):
    """
    Singleton respons�vel por obter e retornar os valores parametrizados\
    do sistema
    """
    def __init__(self):
        self.parametros = dict()
        self.__JobManager = True if os.getenv('jobmanager') == 'True' else False


    def obterParametro(self, parametro: EnumParametros) -> str:
        """
        Retornar o valor do par�metro desejado
        Args:
            parametro: src.br.com.nasajon.resources.enum_parametros
        """

        self.carregarParametros()
        return (
            self.parametros[parametro.value]
            if (parametro.value in self.parametros)
            else None
        )

    def carregarParametros(self):
        """
        Carrega os par�metros a partir do arquivo de configura��o '.ini'
        """

        if self.__JobManager:
            parametros = [
                ['BANCO_DE_DADOS.banco', 'PostgreSQL'],
                ['BANCO_DE_DADOS.servidor', os.getenv('bd_host')],
                ['BANCO_DE_DADOS.nome_banco', os.getenv('bd_nome')],
                ['BANCO_DE_DADOS.usuario', os.getenv('bd_user')],
                ['BANCO_DE_DADOS.senha', os.getenv('bd_senha')],
                ['BANCO_DE_DADOS.porta', os.getenv('bd_porta')],
            ]

            args_gerais = ('pasta_xml', 'pasta_saida', 'pasta_log', 'sobrepor_documentos',
                           'estabelecimentos', 'anos_fiscais', 'pasta_xml_importados',
                           'pasta_xml_nao_suportados', 'icms_desonerado_como_desconto',
                           'atualizar_produtos', 'importar_sem_protocolo_autorizacao', 'identificar_encoding',
                           'desabilitar_log', 'tipo_documento'
                           )

            for item in args_gerais:
                args_env = os.getenv(item)
                parametros.append(['GERAL.' + item, args_env])

            parametrosIni = {(arg[0]): arg[1] for arg in parametros}
        
        else:

            if (len(self.parametros) > 0):
                return

            if (len(sys.argv) > 1):
                self.parametros = {
                    str(arg).split("=")[0]:arg.split("=")[1]
                    for arg in sys.argv
                    if ((str(arg).rfind(".py") < 0) and (str(arg).rfind("=") > 1))
                }

            caminhoDoArquivo = os.path.join(
                Miscel.retornarPastaDaAplicacao(),
                'nsImportadorTributario.ini'
            )
            arquivoConfiguracao = configparser.ConfigParser()
            arquivoConfiguracao.read(caminhoDoArquivo)
            parametrosIni = {
                (sessao + "." + chave_parametro):valor_parametro
                for sessao in arquivoConfiguracao.sections()
                for chave_parametro, valor_parametro in arquivoConfiguracao.items(sessao)
            }

        for parametro in parametrosIni.keys():
            if(not(parametro in self.parametros)):
                self.parametros[parametro] = parametrosIni[parametro]