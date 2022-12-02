#!/usr/bin/env python
# -*- coding: cp1252 -*-
import psycopg2

from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametros import ControladorParametros
from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.persistence.conexao_postgres_adapter import ConexaoPostgresAdapter
from src.br.com.nasajon.resources.enum_sgbd import EnumSGBD
from src.br.com.nasajon.resources.singleton import Singleton


class ConstrutorDeConexoes(metaclass=Singleton):
    def contruirConexao(self) -> ConexaoPadrao:
        """
        M�todo respons�vel por construir conex�es com o banco de dados a \
        partir dos par�metros definidos no arquivo de configura��o padr�o \
        do sistema
        """
        sgbd_str = ControladorParametros().obterParametro(EnumParametros.SGBD)
        return self.__construirConexaoBanco(EnumSGBD(sgbd_str))
    


    def __construirConexaoBanco(self, sgbd: EnumParametros) -> ConexaoPadrao:
        """
        M�todo privado respons�vel por construir as conex�es ao banco de dados
        Args:
            sgbd:   Enumerado respons�vel por identificar o servidor de banco \
        de dados utilizado. EX: PostgreSQL, Oracle, MySQL.
        """
        if (sgbd == EnumSGBD.POSTGRES):
            return self.__obterConexaoPostgres()
    

    
    def __obterConexaoPostgres(self) -> ConexaoPadrao:
        """
        M�todo privado respons�vel por construir as conex�es ao PostgreSQL e \
        retornar no Adapter
        """
        conexaoPostgres = psycopg2.connect(
                    host = ControladorParametros().obterParametro(
                            EnumParametros.SERVIDOR
                        ),
                    database = ControladorParametros().obterParametro(
                            EnumParametros.NOME_BD
                        ),
                    user = ControladorParametros().obterParametro(
                            EnumParametros.USUARIO
                        ),
                    password = ControladorParametros().obterParametro(
                            EnumParametros.SENHA
                        ), 
                    port = int(ControladorParametros().obterParametro(
                            EnumParametros.PORTA
                        )
                ),
                client_encoding = "utf8",
                application_name = "Importador Tributário"
            )
        return ConexaoPostgresAdapter(conexaoPostgres)