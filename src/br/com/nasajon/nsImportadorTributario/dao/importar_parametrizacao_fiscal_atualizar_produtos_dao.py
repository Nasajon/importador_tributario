#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

class ParametrizacaoFiscalAtualizarProdutosDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def atualizarProdutos(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAtualizarProdutos(),
            [],
            False,
            False)

    @staticmethod
    def obterSQLAtualizarProdutos() -> str:
        return "\
            UPDATE\
                estoque.produtos a\
            SET\
                figuratributaria = b.tb_figura_id\
            FROM\
                tmp_imp_tributacao b\
            WHERE\
                replace(b.pl_ncm, '.', '') = a.tipi\
        "