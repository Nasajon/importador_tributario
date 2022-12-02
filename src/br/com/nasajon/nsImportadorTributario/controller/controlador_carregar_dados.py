#!/usr/bin/env python
# -*- coding: cp1252 -*-
from typing import List

from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes
from src.br.com.nasajon.nsImportadorTributario.dao.tabela_temporaria_dao import TabelaTemporariaDAO
from src.br.com.nasajon.nsImportadorTributario.dao.carregar_dados_dao import CarregarDadosDAO


class ControladorCarregarDados():

    def carregarDados(self):
        CarregarDadosDAO().carregarDados()