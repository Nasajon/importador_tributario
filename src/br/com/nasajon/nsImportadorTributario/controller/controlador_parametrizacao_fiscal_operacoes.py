#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List

from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes
from src.br.com.nasajon.nsImportadorTributario.dao.tabela_temporaria_dao import TabelaTemporariaDAO
from src.br.com.nasajon.nsImportadorTributario.dao.carregar_dados_dao import CarregarDadosDAO
from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_operacoes_dao import ParametrizacaoFiscalOperacoesDAO

from src.br.com.nasajon.nsImportadorTributario.dto.operacao_dto import OperacaoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.grupo_de_operacoes_dto import GrupoDeOperacoesDTO

class ControladorParametrizacaoFiscalOperacoes():

    def criarCampoOperacaoID(self):
        ParametrizacaoFiscalOperacoesDAO().criarCampoOperacaoID()

    def selecionarOperacoes(self) -> List[OperacaoDTO]:
        return ParametrizacaoFiscalOperacoesDAO().selecionarOperacoes()

    def selecionarGrupoDeOperacoes(self, operacao_natureza) -> List[GrupoDeOperacoesDTO]:
        return ParametrizacaoFiscalOperacoesDAO().selecionarGrupoDeOperacoes(operacao_natureza)

    def inserirGrupoDeOperacoes(self, operacao_natureza, pl_natureza) -> str:
        return ParametrizacaoFiscalOperacoesDAO().inserirGrupoDeOperacoes(operacao_natureza, pl_natureza)

    def inserirOperacao(self, operacao_codigo, pl_operacao_descricao, operacao_sinal, operacao_grupo) -> str:
        return ParametrizacaoFiscalOperacoesDAO().inserirOperacao(operacao_codigo, pl_operacao_descricao, operacao_sinal, operacao_grupo)

    def atualizarOperacaoId(self, operacao_id, pl_tipo, pl_natureza, pl_operacao_codigo, pl_operacao_descricao):
        ParametrizacaoFiscalOperacoesDAO().atualizarOperacaoId(operacao_id, pl_tipo, pl_natureza, pl_operacao_codigo, pl_operacao_descricao)