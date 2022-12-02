# !/usr/bin/env python
# -*- coding: cp1252 -*-
from typing import List

from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes
from src.br.com.nasajon.resources.miscelania import Miscel


class UtilidadesBanco:
    """
    Classe utilizada para centralizar as opera��es com o banco de dados.
    Dada uma conex�o, o objeto fornecer� funcionalidades para executar comandos\
    SQL
    """

    @staticmethod
    def executarComando(conexao: ConexaoPadrao, sql: str, parametros, bulk: bool = False,
                        manterTransacao=False, template: str = None) -> None:
        """
        Executa uma instru��o sql sem retorno

        Note:
            Se n�o for passada uma conex�o, ser� obtida a primeira dispon�vel\
        no Pool.

        :param conexao: Objeto do tipo ConexaoPadrao que ser� a conex�o \
        utilizado para interagir com o banco de dados
        :param sql: Texto do Comando SQL a ser executado. Caso haja \
        par�metros, os mesmos devem ser passados no argumento parametros
        :param parametros: Quando (Bulk = False) > Dicion�rio contendo os \
        par�metros a serem aplicados no comando sql, no formato <Nome, Valor> \
        Quando (Bulk = True) > lista de listas no formato \
        Registros[Campos[],Campos[],...,Campos[]]
        :param bulk: Informa se a lista de parametros cont�m 1 (False) ou \
            varios registros (True)
        :param manterTransacao: Indica se h� controle transacional ou se a \
        transa��o � impl�cita
        :param template: Utilizado para a realiza��o de BulkInsert, deve conter \
        o formato de substitui��o dos campos no SQL
        """
        if conexao is None:
            conexao = FabricaDeConexoes().obterConexao()
        if bulk:
            conexao.executarBulk(sql, parametros, manterTransacao, template)
        else:
            conexao.executarComando(sql, parametros, manterTransacao)

    @staticmethod
    def executarConsulta(conexao: ConexaoPadrao, sql: str, parametros: dict,
                         classeRetorno, manterTransacao=False) -> List[object]:
        """
        Executa uma instru��o sql retornando uma lista de DTO

        Note:
            Se n�o for passada uma conex�o, ser� obtida a primeira dispon�vel no\
        Pool.

        :param conexao: Objeto do tipo ConexaoPadrao que ser� a conex�o \
        utilizado para interagir com o banco de dados
        :param sql: Texto do Comando SQL a ser executado. Caso haja \
        par�metros, os mesmos devem ser passados no argumento parametros
        :param parametros: Dicion�rio contendo os par�metros a serem aplicados\
        no comando sql, no formato <Nome, Valor>
        :param classeRetorno: Classe dos objetos Dto que ser�o retornados na lista
        manterTransacao:
        :param manterTransacao: Indica se h� controle transacional ou se a \
        transa��o � impl�cita
        :return: Lista de Objetos populados
        """
        if conexao is None:
            conexao = FabricaDeConexoes().obterConexao()
        listaDeRegistros = conexao.executarConsulta(
            sql,
            parametros,
            manterTransacao
        )
        if classeRetorno is not None:

            return UtilidadesBanco.obterObjetosPreenchidos(
                listaDeRegistros,
                classeRetorno
            )
        else:
            return listaDeRegistros

    # @staticmethod
    # def executarCopy(
    #         conexao: ConexaoPadrao,
    #         stream: StringIO,
    #         tabela: str,
    #         campos: str,
    #         manterTransacao=False
    # ):
    #     """
    #     Executa uma instru��o sql copiando o stream para a tabela
    #
    #     Note:
    #         Se n�o for passada uma conex�o, ser� obtida a primeira dispon�vel no\
    #     Pool.
    #
    #     Args:
    #         conexao: Objeto do tipo ConexaoPadrao que ser� a conex�o \
    #     utilizado para interagir com o banco de dados
    #         stream: Objeto do tipo io.StringIO que cont�m os dados a serem\
    #     copiados
    #         tabela: Tabela para onde os dados devem ser copiados
    #         campos: Campos da tabela que est�o no stream
    #         manterTransacao:    Indica se h� controle transacional ou se a \
    #     transa��o � impl�cita
    #     """
    #     if (conexao == None):
    #         conexao = FabricaDeConexoes().obterConexao()
    #     conexao.executarCopy(stream, tabela, campos, manterTransacao)

    @staticmethod
    def obterObjetosPreenchidos(registros: List[dict], classeRetorno) -> List[object]:
        """
        Preenche uma lista de objetos a partir de um retorno de uma query

        :param registros: Lista de dict com os dados retornados pela consulta
        :param classeRetorno: Classe dos objetos Dto que ser�o retornados na lista
        :return: objetos preenchidos
        """
        return [
            obj
            for obj in [
                Miscel.preencherObjeto(registro, classeRetorno, False)
                for registro in registros
            ]
            if obj is not None
        ]
