# !/usr/bin/env python
# -*- coding: cp1252 -*-
from io import StringIO
from typing import List

import psycopg2
import psycopg2.extensions
import psycopg2.extras

from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao


class ConexaoPostgresAdapter(ConexaoPadrao):
    """
    Classe respons�vel por encapsular as opera��es com banco de dados Postgres.
    � uma extens�o da classe ConexaoPadrao.
    """

    def __init__(self, conexao):
        self.__conexao = conexao
        self.__cursor = conexao.cursor()
        self.__ocupada = False
        self.__alocada = False

    @property
    def conexao(self):
        """
        Conex�o ao Banco de Dados Postgres
        """
        return self.__conexao

    @property
    def cursor(self):
        """
        Cursor conectado ao Banco de Dados Postgres
        """
        return self.__cursor

    def executarComando(
            self,
            sql: str,
            parametros: dict,
            manterTransacao=False
    ) -> None:
        """
        Executa uma instru��o sql sem retorno
        :param sql: Texto do Comando SQL a ser executado. Caso haja \
        par�metros, os mesmos devem ser passados no argumento parametros
        :param parametros: Dicion�rio contendo os par�metros a serem aplicados\
        no comando sql, no formato <Nome, Valor>
        :param manterTransacao: Par�metro booleano para indicar se h� um controle\
        externo de transa��o ou n�o.
        """
        try:
            self.__ocupada = True
            self.cursor.execute(sql, parametros)
            if (not manterTransacao):
                self.__conexao.commit()
        finally:
            self.__ocupada = False

    def executarBulk(
            self,
            sql: str,
            parametros: list,
            manterTransacao=False,
            template: str = None
    ) -> None:
        """
        Executa uma instru��o sql em lote, sem retorno

        Args:
            sql:        Texto do Comando SQL a ser executado. Caso haja \
        par�metros, os mesmos devem ser passados no argumento parametros
            parametros: lista de listas no formato: \
        Registros[Campos[],Campos[],...,Campos[]]
            manterTransacao: Par�metro booleano para indicar se h� um controle\
        externo de transa��o ou n�o.
            template:   Utilizado para a realiza��o de BulkInsert, deve conter \
        o formato de substitui��o dos campos no SQL
        """
        self.__ocupada = True
        try:
            psycopg2.extras.execute_values(
                self.cursor,
                sql,
                parametros,
                template,
                10000
            )
            if (not manterTransacao):
                self.__conexao.commit()
        except:
            if (not manterTransacao):
                self.__conexao.rollback()
            raise
        finally:
            self.__ocupada = False

    def executarConsulta(
            self,
            sql: str,
            parametros: dict,
            manterTransacao=False
    ) -> List[dict]:
        """
       Executa uma instru��o sql retornando uma lista de dicion�rio \
       (nome_campo:Valor)

       :param sql: Texto do Comando SQL a ser executado. Caso haja \
       par�metros, os mesmos devem ser passados no argumento parametros
       :param parametros: Dicion�rio contendo os par�metros a serem aplicados\
       no comando sql, no formato <Nome, Valor>
       :param manterTransacao: Par�metro booleano para indicar se h� um controle\
       externo de transa��o ou n�o.
       :return: List[dict]
       """
        self.__ocupada = True
        try:
            self.cursor.execute(sql, parametros)
            resultado = self.cursor.fetchall()
            retorno = [
                {
                    campo.name: registro[self.cursor.description.index(campo)]
                    for campo in self.cursor.description
                }
                for registro in resultado
            ]
            if (not manterTransacao):
                self.__conexao.commit()
        except:
            if (not manterTransacao):
                self.__conexao.rollback()
            raise
        finally:
            self.__ocupada = False
        return retorno

    def disponivel(self) -> bool:
        """
        Retorna True quando a conex�o est� dispon�vel para uso
        :return: Dispon�vel? Sim ou N�o
        """
        return not (self.__ocupada or self.__alocada)

    def fechar(self) -> None:
        """
        Fecha a conex�o ao banco de dados
        """
        try:
            self.cursor.close()
        except:
            pass  # abafar exce��o
        try:
            self.conexao.close()
        except:
            pass  # abafar exce��o

    def startTransaction(self) -> None:
        """
        Inicia uma transa��o
        """
        self.commit()

    def commit(self) -> None:
        """
        Confirma uma transa��o
        """
        self.conexao.commit()

    def rollback(self) -> None:
        """
        Cancela uma transa��o
        """
        self.conexao.rollback()

    def obterExclusividade(self) -> None:
        """
        Marca a conex�o como "ocupada" por um objeto
        """
        self.__alocada = True

    def liberarExclusividade(self) -> None:
        """
        Desmarca a conex�o como "ocupada" por um objeto
        """
        self.__alocada = False
        self.__ocupada = False

    def forcarLiberacao(self) -> None:
        """
        Retira a exclusividade da conexao, quando poss�vel
        """
        if self.conexao.status != psycopg2.extensions.STATUS_IN_TRANSACTION:
            self.liberarExclusividade()
