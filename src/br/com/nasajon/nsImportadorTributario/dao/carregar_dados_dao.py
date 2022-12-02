#!/usr/bin/env python
# -*- coding: cp1252 -*-
from typing import List
import uuid

from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametros import ControladorParametros
from src.br.com.nasajon.nsImportadorTributario.resources.enum_parametros import EnumParametros
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco


class CarregarDadosDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def carregarDados(self):
        parametros = [
            ControladorParametros().obterParametro(EnumParametros.ARQUIVO_DADOS).upper()
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLCarregarDados(),
            parametros,
            False,
            False)

    @staticmethod
    def obterSQLConfigurarEncoding() -> str:
        return "SET CLIENT_ENCODING TO 'utf8'"

    @staticmethod
    def obterSQLCarregarDados() -> str:
        return "COPY tmp_imp_tributacao FROM %s DELIMITER ',' csv header"

    def criarTabelaTemporaria(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLApagarTabelaTemporariaCasoExista(),
            [],
            False,
            False)

        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLCriaTabelaTemporaria(),
            [],
            False,
            False)

    @staticmethod
    def obterSQLApagarTabelaTemporariaCasoExista() -> str:
        return "DROP TABLE IF EXISTS tmp_imp_tributacao"

    @staticmethod
    def obterSQLCriaTabelaTemporaria() -> str:
        return "CREATE TABLE tmp_imp_tributacao (pl_estabelecimento varchar, pl_tipo varchar, pl_natureza varchar,\
            pl_operacao_codigo varchar, pl_operacao_descricao varchar, pl_cfop varchar, pl_ncm varchar,\
            pl_mov_fiscal varchar, pl_mov_prop_em_terc varchar, pl_mov_terc_em_meu_poder varchar,\
            pl_execao_produto varchar, pl_execao_regime_tributario varchar, pl_execao_participante varchar,\
            pl_pis_cst varchar, pl_pis_aliquota varchar, pl_cofins_cst varchar, pl_cofins_aliquota varchar,\
            pl_ipi_cst varchar, pl_ipi_aliquota varchar, pl_icms_uf_destino varchar,\
            pl_icms_cst_contribuinte_icms varchar, pl_icms_cst_nao_contribuinte_icms varchar,\
            pl_icms_modalidade_base_calculo varchar, pl_icms_aliquota_interna varchar, pl_icms_aliquota_fecp varchar,\
            pl_icms_percentual_diferimento varchar, pl_icms_percentual_reducao varchar,\
            pl_icms_st_aliquota_fecp varchar, pl_icms_st_percentual_mva varchar, pl_icms_st_percentual_reducao varchar,\
            pl_icms_st_modalidade_base_calculo varchar, pl_icms_st_forma_cobranca_st varchar)"