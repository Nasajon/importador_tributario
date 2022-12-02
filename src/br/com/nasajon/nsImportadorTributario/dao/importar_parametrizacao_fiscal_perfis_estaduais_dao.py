#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

from src.br.com.nasajon.nsImportadorTributario.dto.perfil_estadual_dto import PerfilEstadualDTO

class ParametrizacaoFiscalPerfisEstaduaisDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def excluirColunaTbPerfilEstId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbPerfilEstId(),
            [],
            False,
            False)

    def excluirColunaTbPerfilEstValidadeId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbPerfilEstValidadeId(),
            [],
            False,
            False)

    def addColunaTbPerfilEstId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbPerfilEstId(),
            [],
            False,
            False)

    def addColunaTbPerfilEstValidadeId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbPerfilEstValidadeId(),
            [],
            False,
            False)

    def selecionarPerfisEstaduais(self) -> List[PerfilEstadualDTO]:
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSQLSelecionarPerfisEstaduais(),
                [],
                PerfilEstadualDTO
            )

    def inserirPerfilTributarioEstadual(self, codigo, descricao, uf_referencia, pl_icms_aliquota_interna) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            codigo,
            descricao,
            uf_referencia,
            pl_icms_aliquota_interna
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioEstadual(),
            parametros,
            False,
            False)
        return guid

    def inserirPerfilTributarioEstadualValidades(self, perfiltrib_est, data) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            perfiltrib_est,
            data
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioEstadualValidades(),
            parametros,
            False,
            False)
        return guid

    def inserirPerfilTributarioEstadualValidadesImpostos(
        self,
        perfiltrib_est_validade,
        pl_icms_uf_destino,
        icms_cst,
        pl_icms_percentual_reducao,
        pl_icms_st_percentual_mva,
        pl_icms_st_percentual_reducao,
        icms_st_for_cob,
        entrada,
        saida,
        pl_icms_aliquota_fecp,
        pl_icms_percentual_diferimento,
        icms_st_mod,
        icms_mod,
        icms_cst_nao_contr,
        pl_icms_st_aliquota_fecp
    ):
        parametros = [
            perfiltrib_est_validade,
            pl_icms_uf_destino,
            icms_cst,
            pl_icms_percentual_reducao, #
            pl_icms_st_percentual_mva, #
            pl_icms_st_percentual_reducao, #
            icms_st_for_cob,
            entrada,
            saida,
            pl_icms_aliquota_fecp, #
            pl_icms_percentual_diferimento, #
            icms_st_mod,
            icms_mod,
            icms_cst_nao_contr,
            pl_icms_st_aliquota_fecp #
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioEstadualValidadesImpostos(),
            parametros,
            False,
            False)

    def atualizarPerfilEstadual(
        self,
        perfiltrib_est,
        perfiltrib_est_validade,
        pl_estabelecimento,
        pl_icms_aliquota_interna,
        pl_icms_cst_contribuinte_icms,
        pl_icms_cst_nao_contribuinte_icms,
        pl_icms_modalidade_base_calculo,
        pl_icms_aliquota_fecp,
        pl_icms_percentual_diferimento,
        pl_icms_percentual_reducao,
        pl_icms_st_aliquota_fecp,
        pl_icms_st_percentual_mva,
        pl_icms_st_percentual_reducao,
        pl_icms_st_modalidade_base_calculo,
        pl_icms_st_forma_cobranca_st,
        pl_icms_uf_destino
    ):
        parametros = [
            perfiltrib_est,
            perfiltrib_est_validade,
            pl_estabelecimento,
            pl_icms_aliquota_interna,
            pl_icms_cst_contribuinte_icms,
            pl_icms_cst_nao_contribuinte_icms,
            pl_icms_modalidade_base_calculo,
            pl_icms_aliquota_fecp,
            pl_icms_percentual_diferimento,
            pl_icms_percentual_reducao,
            pl_icms_st_aliquota_fecp,
            pl_icms_st_percentual_mva,
            pl_icms_st_percentual_reducao,
            pl_icms_st_modalidade_base_calculo,
            pl_icms_st_forma_cobranca_st,
            pl_icms_uf_destino
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAtualizarPerfilEstadual(),
            parametros,
            False,
            False)

    @staticmethod
    def obterSQLExcluirColunaTbPerfilEstId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_perfil_est_id"

    @staticmethod
    def obterSQLExcluirColunaTbPerfilEstValidadeId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_perfil_est_validade_id"

    @staticmethod
    def obterSQLAddColunaTbPerfilEstId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_perfil_est_id UUID"

    @staticmethod
    def obterSQLAddColunaTbPerfilEstValidadeId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_perfil_est_validade_id UUID"

    @staticmethod
    def obterSQLSelecionarPerfisEstaduais() -> str:
        return "\
            SELECT\
                c.uf as uf_referencia,\
                a.pl_estabelecimento,\
                a.pl_icms_aliquota_interna,\
                a.pl_icms_cst_contribuinte_icms,\
                a.pl_icms_cst_nao_contribuinte_icms,\
                a.pl_icms_modalidade_base_calculo,\
                a.pl_icms_aliquota_fecp,\
                a.pl_icms_percentual_diferimento,\
                a.pl_icms_percentual_reducao,\
                a.pl_icms_st_aliquota_fecp,\
                a.pl_icms_st_percentual_mva,\
                a.pl_icms_st_percentual_reducao,\
                a.pl_icms_st_modalidade_base_calculo,\
                a.pl_icms_st_forma_cobranca_st,\
                a.pl_icms_uf_destino,\
                d.entrada,\
                d.saida\
            FROM\
                tmp_imp_tributacao a\
                    INNER JOIN ns.estabelecimentos b ON a.pl_estabelecimento = b.raizcnpj || b.ordemcnpj\
                    INNER JOIN ns.municipios c ON c.ibge = b.ibge\
                    INNER JOIN scritta.tabicms d ON d.uflocal = c.UF and d.uf = a.pl_icms_uf_destino\
            GROUP BY\
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17\
        "

    @staticmethod
    def obterSQLInserirPerfilTributarioEstadual() -> str:
        return "\
            INSERT INTO estoque.perfiltrib_est\
                (perfiltrib_est, codigo, descricao, uf_origem, icms_aliquotainterna, situacao)\
            VALUES \
                (%s, %s, %s, %s,  (replace(%s, ',','.'))::numeric, 1)\
        "

    @staticmethod
    def obterSQLInserirPerfilTributarioEstadualValidades() -> str:
        return "INSERT INTO estoque.perfiltrib_est_validades(perfiltrib_est_validade, perfiltrib_est, data) VALUES(%s, %s, %s)"

    @staticmethod
    def obterSQLInserirPerfilTributarioEstadualValidadesImpostos() -> str:
        return "\
            INSERT INTO estoque.perfiltrib_est_validades_impostos(\
                perfiltrib_est_validade,\
                uf_destino,\
                icms_cst,\
                icms_reducao,\
                mva,\
                icms_reducao_st,\
                icms_formadecobranca_st,\
                icms_entrada,\
                icms_saida,\
                fcp,\
                diferimento,\
                modalidade_bc_icmsst,\
                modalidade_bc_icms,\
                icms_cst_contribuinte,\
                fcp_st\
            )\
            VALUES(\
                %s,\
                %s,\
                %s,\
                (replace(%s, ',', '.'))::numeric,\
                (replace(%s, ',', '.'))::numeric,\
                (replace(%s, ',', '.'))::numeric,\
                %s,\
                %s,\
                %s,\
                (replace(%s, ',', '.'))::numeric,\
                (replace(%s, ',', '.'))::numeric,\
                %s,\
                %s,\
                %s,\
                (replace(%s, ',', '.'))::numeric\
            )\
        "

    @staticmethod
    def obterSQLAtualizarPerfilEstadual() -> str:
        return "\
            UPDATE\
                tmp_imp_tributacao\
            SET\
                tb_perfil_est_id = %s,\
                tb_perfil_est_validade_id = %s\
            WHERE\
                coalesce(pl_estabelecimento, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_aliquota_interna, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_cst_contribuinte_icms, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_cst_nao_contribuinte_icms, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_modalidade_base_calculo, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_aliquota_fecp, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_percentual_diferimento, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_percentual_reducao, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_st_aliquota_fecp, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_st_percentual_mva, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_st_percentual_reducao, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_st_modalidade_base_calculo, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_st_forma_cobranca_st, '') = coalesce(%s, '') AND\
                coalesce(pl_icms_uf_destino, '') = coalesce(%s, '')\
            "