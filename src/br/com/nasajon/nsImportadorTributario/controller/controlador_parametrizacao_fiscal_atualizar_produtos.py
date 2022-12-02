#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes

from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_atualizar_produtos_dao import ParametrizacaoFiscalAtualizarProdutosDAO

class ControladorParametrizacaoFiscalAtualizarProdutos():

    def atualizarProdutos(self):
        ParametrizacaoFiscalAtualizarProdutosDAO().atualizarProdutos()