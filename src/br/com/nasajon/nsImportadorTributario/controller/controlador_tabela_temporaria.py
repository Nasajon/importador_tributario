#!/usr/bin/env python
# -*- coding: cp1252 -*-
from typing import List

from src.br.com.nasajon.nsImportadorTributario.dao.tabela_temporaria_dao import TabelaTemporariaDAO
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes


class ControladorTabelaTemporaria():

    def criarTabelaTemporaria(self):
        conexao = FabricaDeConexoes().obterConexaoExclusiva()
        try:
            conexao.startTransaction()
            TabelaTemporariaDAO(conexao).criarTabelaTemporaria()
            conexao.commit()
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            conexao.liberarExclusividade()