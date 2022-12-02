# !/usr/bin/env python
# -*- coding: cp1252 -*-
from typing import List

from src.br.com.nasajon.nsImportadorTributario.controller.builder.construtor_de_conexoes import ConstrutorDeConexoes
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.singleton import Singleton


class FabricaDeConexoes(metaclass=Singleton):
    """
    Classe respons�vel por gerir o Pool de conexoes com o banco de dados.
    """

    def __init__(self):
        self.__poolDeConexoes: List[ConexaoPadrao] = set()

    def obterConexao(self) -> ConexaoPadrao:
        """
        Retorna uma conex�o dispon�vel do pool.

        Note:
            Caso n�o haja conex�es dispon�veis, uma nova ser� criada e inclu�da\
        no pool
        :return: uma conex�o ao banco de dados
        """
        for conexao in self.__poolDeConexoes:
            if conexao.disponivel():
                return conexao

        return self.__obterNovaConexao()

    def __del__(self) -> None:
        """
        M�todo destrutor que fecha as conex�es
        """""
        for conexao in self.__poolDeConexoes:
            conexao.fechar()
        super()

    @property
    def poolDeConexoes(self) -> List[ConexaoPadrao]:
        """
        Lista com as conex�es ao banco de dados
        :return: Lista de conex�es no pool
        """
        return self.__poolDeConexoes

    def __obterNovaConexao(self) -> ConexaoPadrao:
        """
        Instancia uma nova conex�o e a adiciona no Pool
        :return: uma nova conex�o
        """
        novaConexao = ConstrutorDeConexoes().contruirConexao()
        self.__adicionarConexaoNoPool(novaConexao)
        return novaConexao

    def __adicionarConexaoNoPool(self, conexao: ConexaoPadrao) -> None:
        """
        Adiciona uma conexao no Pool

        Note:
            Se a conex�o j� estiver no pool, nada ser� feito
            A conex�o dever� ser um objeto de classe que extenda a classe \
        src.br.com.nasajon.nsImportadorTributario.persistencia.conexao_padrao.ConexaoPadrao
        :param conexao: Objeto do tipo ConexaoPadrao que ser� adicionado no pool
        """
        if conexao in self.__poolDeConexoes:
            return
        self.__poolDeConexoes.add(conexao)

    def obterConexaoExclusiva(self) -> ConexaoPadrao:
        """
        Retorna uma conex�o dispon�vel do pool e a torna exclusiva, impedindo\
        que outro objeto a acesse.

        Note:
            Caso n�o haja conex�es dispon�veis, uma nova ser� criada e inclu�da\
        no pool
        """
        conexao = self.obterConexao()
        conexao.obterExclusividade()
        return conexao

    def destruirConexao(self, conexao: ConexaoPadrao) -> None:
        """
        Fecha e remove a conex�o do Pool
        :param conexao: conex�o a ser destru�da
        """
        conexao.obterExclusividade()
        self.__poolDeConexoes.remove(conexao)
        conexao.fechar()
