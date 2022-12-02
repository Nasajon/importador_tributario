#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes

from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_perfis_federais_dao import ParametrizacaoFiscalPerfisFederaisDAO
from src.br.com.nasajon.nsImportadorTributario.dto.perfil_federal_dto import PerfilFederalDTO

class ControladorParametrizacaoFiscalPerfisFederais():

    def excluirColunaTbPerfilFedId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().excluirColunaTbPerfilFedId()

    def excluirColunaTbPerfilFedValidadeId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().excluirColunaTbPerfilFedValidadeId()

    def excluirColunaTbPerfilFedValidadeImpostosId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().excluirColunaTbPerfilFedValidadeImpostosId()

    def addColunaTbPerfilFedId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().addColunaTbPerfilFedId()

    def addColunaTbPerfilFedValidadeId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().addColunaTbPerfilFedValidadeId()

    def addColunaTbPerfilFedValidadeImpostosId(self):
        ParametrizacaoFiscalPerfisFederaisDAO().addColunaTbPerfilFedValidadeImpostosId()

    def selecionarPerfisFederais(self) -> List[PerfilFederalDTO]:
        return ParametrizacaoFiscalPerfisFederaisDAO().selecionarPerfisFederais()

    def inserirPerfilTributarioFederal(self, codigo, descricao) -> str:
        return ParametrizacaoFiscalPerfisFederaisDAO().inserirPerfilTributarioFederal(codigo, descricao)

    def inserirPerfilTributarioFederalValidades(self, perfiltrib_fed, data) -> str:
        return ParametrizacaoFiscalPerfisFederaisDAO().inserirPerfilTributarioFederalValidades(perfiltrib_fed, data)

    def inserirPerfilTributarioFederalValidadesImpostos(
            self,
            perfiltrib_fed_validade,
            ipi_cst_entrada,
            pl_ipi_aliquota,
            ipi_cst,
            pis_cst,
            pl_pis_aliquota,
            cofins_cst,
            pl_cofins_aliquota
    ) -> str:
        return ParametrizacaoFiscalPerfisFederaisDAO().inserirPerfilTributarioFederalValidadesImpostos(
            perfiltrib_fed_validade,
            ipi_cst_entrada,
            pl_ipi_aliquota,
            ipi_cst,
            pis_cst,
            pl_pis_aliquota,
            cofins_cst,
            pl_cofins_aliquota)

    def atualizarPerfilFederal(
            self,
            perfiltrib_fed,
            perfiltrib_fed_validade,
            perfiltrib_fed_validade_imposto,
            pl_pis_cst,
            pl_pis_aliquota,
            pl_cofins_cst,
            pl_cofins_aliquota,
            pl_ipi_cst,
            pl_ipi_aliquota
    ):
        ParametrizacaoFiscalPerfisFederaisDAO().atualizarPerfilFederal(
            perfiltrib_fed,
            perfiltrib_fed_validade,
            perfiltrib_fed_validade_imposto,
            pl_pis_cst,
            pl_pis_aliquota,
            pl_cofins_cst,
            pl_cofins_aliquota,
            pl_ipi_cst,
            pl_ipi_aliquota)