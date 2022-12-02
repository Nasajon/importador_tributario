#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid

from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametros import ControladorParametros
from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

from src.br.com.nasajon.nsImportadorTributario.dto.movimento_dto import MovimentoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.cfop_dto import CfopDTO

class ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def selecionarMovimentos(self) -> List[MovimentoDTO]:
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSqlMovimentos(),
                [],
                MovimentoDTO
            )

    def selecionarCFOP(self, cfop) -> List[CfopDTO]:
        parametros = [
            str(cfop)
        ]
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSqlCFOP(),
                parametros,
                CfopDTO
            )

    def inserirOperacoesCFOP(self, tb_operacao_id, cfop_id) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            str(guid),
            tb_operacao_id,
            cfop_id
        ]
        UtilidadesBanco.executarComando(
                self.__conexao,
                self.obterSqlInserirOperacoesCFOP(),
                parametros,
                False
            )
        return guid

    def inserirOperacoesCFOPsSlots(self, tb_operacao_id, operacaocfop, slot, entrada):
        parametros = [
            tb_operacao_id,
            operacaocfop,
            slot,
            entrada
        ]
        UtilidadesBanco.executarComando(
                self.__conexao,
                self.obterSqlInserirOperacoesCFOPsSlots(),
                parametros,
                False
            )

    @staticmethod
    def obterSqlMovimentos() -> str:
        return "\
            SELECT\
                tb_operacao_id,\
                pl_cfop,\
                pl_mov_fiscal,\
                pl_mov_prop_em_terc,\
                pl_mov_terc_em_meu_poder,\
                pl_tipo\
            FROM\
                tmp_imp_tributacao\
            GROUP BY\
                1, 2, 3, 4, 5, 6\
        "

    @staticmethod
    def obterSqlCFOP() -> str:
        return "\
            SELECT\
                id\
            FROM\
                ns.cfop\
            WHERE\
                cfop = TRIM(%s)\
            LIMIT\
                1\
        "

    @staticmethod
    def obterSqlInserirOperacoesCFOP() -> str:
        return "INSERT INTO estoque.operacoescfops(operacaocfop, operacao, cfop, ativo) VALUES (%s, %s, %s, 'true')"

    @staticmethod
    def obterSqlInserirOperacoesCFOPsSlots() -> str:
        return "\
            INSERT INTO estoque.operacoescfopsslots(operacao, operacaocfop, slot, entrada)\
            VALUES (%s, %s, %s, %s)"