#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_dto import FiguraTributariaDTO
from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_template_dto import FiguraTributariaTemplateDTO

class ParametrizacaoFiscalFigurasTributariasDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def excluirColunaTbFiguraId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbFiguraId(),
            [],
            False,
            False)

    def addColunaTbFiguraId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbFiguraId(),
            [],
            False,
            False)

    def selecionarNCMs(self) -> List[FiguraTributariaDTO]:
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSQLSelecionarNCMs(),
                [],
                FiguraTributariaDTO
            )

    def selecionarFigurasTributarias(self, ncm) -> List[FiguraTributariaDTO]:
        parametros = [
            ncm
        ]
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSQLSelecionarFigurasTributarias(),
                parametros,
                FiguraTributariaDTO
            )

    def selecionarFigurasTributariasTemplates(self, tb_operacao_id, tb_perfil_est_id, tb_perfil_fed_id, primeira, lista_figuras) -> List[FiguraTributariaTemplateDTO]:
        parametros = [
            tb_operacao_id,
            tb_perfil_est_id,
            tb_perfil_fed_id,
            primeira,
            lista_figuras
        ]
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSQLSelecionarFigurasTributariasTemplates(),
                parametros,
                FiguraTributariaTemplateDTO
            )

    def inserirFiguraTributaria(self, count) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            count,
            count
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirFiguraTributaria(),
            parametros,
            False,
            False)
        return guid

    def inserirFiguraTributariaTemplate(self, figuratributaria, ncm):
        parametros = [
            figuratributaria,
            ncm
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirFiguraTributariaTemplate(),
            parametros,
            False,
            False)

    def inserirFiguraTributariaNCM(self, figuratributaria, ncm):
        parametros = [
            figuratributaria,
            ncm
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirFiguraTributariaNCM(),
            parametros,
            False,
            False)

    def atualizarFiguraTributaria(self, figuratributaria, ncm):
        parametros = [
            figuratributaria,
            ncm
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAtualizarFiguraTributaria(),
            parametros,
            False,
            False)

    @staticmethod
    def obterSQLExcluirColunaTbFiguraId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_figura_id"

    @staticmethod
    def obterSQLAddColunaTbFiguraId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_figura_id UUID"

    @staticmethod
    def obterSQLSelecionarNCMs() -> str:
        return "\
            SELECT\
                DISTINCT replace(pl_ncm, '.', '') as ncm,\
                b.id, \
                a.pl_ncm\
            FROM\
                tmp_imp_tributacao a\
                LEFT JOIN  ns.tipi b ON  replace(pl_ncm, '.', '') = b.ncm\
        "

    @staticmethod
    def obterSQLSelecionarFigurasTributarias() -> str:
        return "\
            SELECT\
                tb_operacao_id,\
                tb_perfil_est_id,\
                tb_perfil_fed_id\
            FROM\
                tmp_imp_tributacao\
            WHERE\
                replace(pl_ncm, '.', '') = %s\
        "

    @staticmethod
    def obterSQLSelecionarFigurasTributariasTemplates() -> str:
        return "\
            SELECT\
                figuratributaria\
            FROM\
                estoque.figurastributariastemplates\
            WHERE\
                operacao = %s AND\
                perfiltributario_estadual = %s AND\
                perfiltributario_federal = %s AND\
                CASE\
                    WHEN %s THEN(1 = 1)\
                    ELSE figuratributaria = ANY(%s)\
                END\
        "

    @staticmethod
    def obterSQLInserirFiguraTributaria() -> str:
        return "\
            INSERT INTO estoque.figurastributarias(figuratributaria, codigo, descricao) VALUES (\
                %s,\
                'FT' || LPAD(%s::VARCHAR, 4, '0'),\
                'Figura Tributária ' || LPAD(%s::VARCHAR, 4, '0')\
			)\
        "

    @staticmethod
    def obterSQLInserirFiguraTributariaTemplate() -> str:
        return "\
            INSERT INTO estoque.figurastributariastemplates(\
                figuratributaria, estabelecimento, operacao, perfiltributario_estadual, perfiltributario_federal\
            )\
            SELECT\
                %s,\
                b.estabelecimento,\
                a.tb_operacao_id,\
                a.tb_perfil_est_id,\
                a.tb_perfil_fed_id\
            FROM\
                tmp_imp_tributacao a\
                    INNER JOIN ns.estabelecimentos b ON a.pl_estabelecimento =  b.raizcnpj || b.ordemcnpj\
            WHERE\
                replace(pl_ncm, '.', '') = %s\
        "

    @staticmethod
    def obterSQLInserirFiguraTributariaNCM() -> str:
        return "INSERT INTO estoque.figurastributarias_ncm(figuratributaria, tipi) VALUES (%s, %s)"

    @staticmethod
    def obterSQLAtualizarFiguraTributaria() -> str:
        return "UPDATE tmp_imp_tributacao SET tb_figura_id = %s WHERE replace(pl_ncm, '.', '') = %s"