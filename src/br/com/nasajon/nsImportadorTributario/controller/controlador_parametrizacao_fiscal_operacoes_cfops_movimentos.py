#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes

from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_operacoes_cfops_movimentos_dao import ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO
from src.br.com.nasajon.nsImportadorTributario.dto.movimento_dto import MovimentoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.cfop_dto import CfopDTO

class ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos():

    def selecionarMovimentos(self) -> List[MovimentoDTO]:
        return ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO().selecionarMovimentos()

    def selecionarCFOP(self, cfop) -> List[CfopDTO]:
        return ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO().selecionarCFOP(cfop)

    def inserirOperacoesCFOP(self, tb_operacao_id, cfop_id) -> str:
        return ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO().inserirOperacoesCFOP(tb_operacao_id, cfop_id)

    def inserirOperacoesCFOPsSlots(self, tb_operacao_id, operacaocfop, slot, entrada):
        ParametrizacaoFiscalOperacoesCFOPsMovimentosDAO().inserirOperacoesCFOPsSlots(tb_operacao_id, operacaocfop, slot, entrada)