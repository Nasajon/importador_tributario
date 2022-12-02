#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid

from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametros import ControladorParametros
from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

from src.br.com.nasajon.nsImportadorTributario.dto.operacao_dto import OperacaoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.grupo_de_operacoes_dto import GrupoDeOperacoesDTO

class ParametrizacaoFiscalOperacoesDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def criarCampoOperacaoID(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLCriarCampoOperacaoID(),
            [],
            False,
            False)

    def selecionarOperacoes(self) -> List[OperacaoDTO]:
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSqlOperacoes(),
                [],
                OperacaoDTO
            )

    def selecionarGrupoDeOperacoes(self, operacao_natureza) -> List[GrupoDeOperacoesDTO]:
        parametros = [
            str(operacao_natureza)
        ]
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSqlGrupoDeOperacoes(),
                parametros,
                GrupoDeOperacoesDTO
            )

    def inserirGrupoDeOperacoes(self, operacao_natureza, pl_natureza) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            str(guid),
            str(operacao_natureza),
            str(operacao_natureza)
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirGrupoDeOperacoes(),
            parametros,
            False)
        return guid

    def inserirOperacao(self, operacao_codigo, pl_operacao_descricao, operacao_sinal, operacao_grupo) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            str(guid),
            str(operacao_codigo),
            str(pl_operacao_descricao),
            str(operacao_sinal),
            str(operacao_grupo)
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirOperacao(),
            parametros,
            False)
        return guid

    def atualizarOperacaoId(self, operacao_id, pl_tipo, pl_natureza, pl_operacao_codigo, pl_operacao_descricao):
        parametros = [
            operacao_id,
            pl_tipo,
            pl_natureza,
            pl_operacao_codigo,
            pl_operacao_descricao
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAtualizarOperacaoId(),
            parametros,
            False,
            False)

    @staticmethod
    def obterSQLCriarCampoOperacaoID() -> str:
        return """ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_operacao_id UUID"""

    @staticmethod
    def obterSqlOperacoes() -> str:
        return "\
            SELECT\
                pl_tipo,\
                pl_natureza,\
                pl_operacao_codigo,\
                pl_operacao_descricao\
            FROM\
                tmp_imp_tributacao\
            GROUP BY\
                1, 2, 3, 4"

    @staticmethod
    def obterSqlGrupoDeOperacoes() -> str:
        return "\
            SELECT\
                grupodeoperacao\
            FROM\
                estoque.gruposdeoperacoes\
            WHERE\
                codigo = %s\
            LIMIT\
                1"

    @staticmethod
    def obterSQLInserirGrupoDeOperacoes() -> str:
        return "INSERT INTO estoque.gruposdeoperacoes(grupodeoperacao, codigo, descricao) VALUES(%s, %s, %s)"

    @staticmethod
    def obterSQLInserirOperacao() -> str:
        return "\
            INSERT INTO estoque.operacoes(\
                operacao,\
                codigo,\
                descricao,\
                sinal,\
			    grupodeoperacao,\
                finalidade,\
                ativa,\
                tipooperacao,\
                requisicao,\
                modalidadefrete,\
                objetivodaoperacao,\
                comportamentooperacao\
            )\
            VALUES (\
                %s ,\
                %s ,\
                %s ,\
                %s ,\
                %s ,\
                '1' ,\
                'true' ,\
                '23' ,\
                'false' ,\
                '0' ,\
                '1' ,\
                '0'\
            )"

    @staticmethod
    def obterSQLAtualizarOperacaoId() -> str:
        return "\
            UPDATE \
                tmp_imp_tributacao \
            SET\
                tb_operacao_id = %s\
            WHERE\
                pl_tipo = %s AND\
                pl_natureza = %s AND\
                pl_operacao_codigo = %s AND\
                pl_operacao_descricao = %s\
        "