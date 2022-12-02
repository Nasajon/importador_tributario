#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes

from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_perfis_estaduais_dao import ParametrizacaoFiscalPerfisEstaduaisDAO
from src.br.com.nasajon.nsImportadorTributario.dto.perfil_estadual_dto import PerfilEstadualDTO

class ControladorParametrizacaoFiscalPerfisEstaduais():

    def excluirColunaTbPerfilEstId(self):
        ParametrizacaoFiscalPerfisEstaduaisDAO().excluirColunaTbPerfilEstId()

    def excluirColunaTbPerfilEstValidadeId(self):
        ParametrizacaoFiscalPerfisEstaduaisDAO().excluirColunaTbPerfilEstValidadeId()

    def addColunaTbPerfilEstId(self):
        ParametrizacaoFiscalPerfisEstaduaisDAO().addColunaTbPerfilEstId()

    def addColunaTbPerfilEstValidadeId(self):
        ParametrizacaoFiscalPerfisEstaduaisDAO().addColunaTbPerfilEstValidadeId()

    def selecionarPerfisEstaduais(self) -> List[PerfilEstadualDTO]:
        return ParametrizacaoFiscalPerfisEstaduaisDAO().selecionarPerfisEstaduais()

    def inserirPerfilTributarioEstadual(self, codigo, descricao, uf_referencia, pl_icms_aliquota_interna) -> str:
        return ParametrizacaoFiscalPerfisEstaduaisDAO().inserirPerfilTributarioEstadual(codigo, descricao, uf_referencia, pl_icms_aliquota_interna)

    def inserirPerfilTributarioEstadualValidades(self, perfiltrib_est, data) -> str:
        return ParametrizacaoFiscalPerfisEstaduaisDAO().inserirPerfilTributarioEstadualValidades(perfiltrib_est, data)

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
        ParametrizacaoFiscalPerfisEstaduaisDAO().inserirPerfilTributarioEstadualValidadesImpostos(
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
        )

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
        ParametrizacaoFiscalPerfisEstaduaisDAO().atualizarPerfilEstadual(
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
        )