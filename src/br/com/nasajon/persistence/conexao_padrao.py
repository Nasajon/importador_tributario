# !/usr/bin/env python
# -*- coding: cp1252 -*-
from abc import ABC, abstractmethod
from typing import List


class ConexaoPadrao(ABC):
    """
    Classe abstrata para encapsular a conex�o ao banco de dados, permitindo que sejam utilizadas diferentes
    estrat�gias de persist�ncias (ex: m�ltiplos bancos de dados)
    """

    @abstractmethod
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
        raise NotImplementedError()

    @abstractmethod
    def executarBulk(
            self,
            sql: str,
            parametros: list,
            manterTransacao=False,
            template: str = None
    ) -> None:
        """
        Executa uma instru��o sql em lote, sem retorno

        :param sql: Texto do Comando SQL a ser executado. Caso haja \
        par�metros, os mesmos devem ser passados no argumento parametros
        :param parametros: lista de listas no formato: \
        Registros[Campos[],Campos[],...,Campos[]]
        :param manterTransacao: Par�metro booleano para indicar se h� um controle\
        externo de transa��o ou n�o.
        :param template: Utilizado para a realiza��o de BulkInsert, deve conter \
        o formato de substitui��o dos campos no SQL
        """
        raise NotImplementedError()

    @abstractmethod
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
        raise NotImplementedError()

    # @abstractmethod
    # def executarCopy(
    #     self,
    #     stream: StringIO,
    #     campos: str,
    #     manterTransacao = False
    # ):
    #     """
    #     Executa uma instru��o sql copiando o stream para a tabela
    #
    #     Note:
    #         Se n�o for passada uma conex�o, ser� obtida a primeira dispon�vel no\
    #     Pool.
    #
    #     Args:
    #         stream: Objeto do tipo io.StringIO que cont�m os dados a serem\
    #     copiados
    #         tabela: Tabela para onde os dados devem ser copiados
    #         campos: Campos da tabela que est�o no stream
    #         manterTransacao:    Indica se h� controle transacional ou se a \
    #     transa��o � impl�cita
    #     """
    #     raise NotImplementedError

    @abstractmethod
    def disponivel(self) -> bool:
        """
        Retorna True quando a conex�o est� dispon�vel para uso
        :return: Dispon�vel? Sim ou N�o
        """
        raise NotImplementedError()

    @abstractmethod
    def fechar(self) -> None:
        """
        Fecha a conex�o ao banco de dados
        """
        raise NotImplementedError()

    @abstractmethod
    def startTransaction(self) -> None:
        """
        Inicia uma transa��o
        """
        raise NotImplementedError()

    @abstractmethod
    def commit(self) -> None:
        """
        Confirma uma transa��o
        """
        raise NotImplementedError()

    @abstractmethod
    def rollback(self):
        """
        Cancela uma transa��o
        """
        raise NotImplementedError()

    @abstractmethod
    def obterExclusividade(self):
        """
        Marca a conex�o como "ocupada" por um objeto
        """
        raise NotImplementedError()

    @abstractmethod
    def liberarExclusividade(self):
        """
        Desmarca a conex�o como "ocupada" por um objeto
        """
        raise NotImplementedError()

    @abstractmethod
    def forcarLiberacao(self):
        """
        Retira a exclusividade da conexao, quando poss�vel
        """
        raise NotImplementedError()
