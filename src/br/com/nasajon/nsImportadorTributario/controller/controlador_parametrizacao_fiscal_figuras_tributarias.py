#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
from src.br.com.nasajon.resources.fabrica_de_conexoes import FabricaDeConexoes

from src.br.com.nasajon.nsImportadorTributario.dao.importar_parametrizacao_fiscal_figuras_tributarias_dao import ParametrizacaoFiscalFigurasTributariasDAO
from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_dto import FiguraTributariaDTO
from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_template_dto import FiguraTributariaTemplateDTO

class ControladorParametrizacaoFiscalFigurasTributarias():

    def excluirColunaTbFiguraId(self):
        ParametrizacaoFiscalFigurasTributariasDAO().excluirColunaTbFiguraId()

    def addColunaTbFiguraId(self):
        ParametrizacaoFiscalFigurasTributariasDAO().addColunaTbFiguraId()

    def selecionarNCMs(self) -> List[FiguraTributariaDTO]:
        return ParametrizacaoFiscalFigurasTributariasDAO().selecionarNCMs()

    def selecionarFigurasTributarias(self, ncm) -> List[FiguraTributariaDTO]:
        return ParametrizacaoFiscalFigurasTributariasDAO().selecionarFigurasTributarias(ncm)

    def selecionarFigurasTributariasTemplates(self, tb_operacao_id, tb_perfil_est_id, tb_perfil_fed_id, primeira, lista_figuras) -> List[FiguraTributariaTemplateDTO]:
        return ParametrizacaoFiscalFigurasTributariasDAO().selecionarFigurasTributariasTemplates(tb_operacao_id, tb_perfil_est_id, tb_perfil_fed_id, primeira, lista_figuras)

    def inserirFiguraTributaria(self, count) -> str:
        return ParametrizacaoFiscalFigurasTributariasDAO().inserirFiguraTributaria(count)

    def inserirFiguraTributariaTemplate(self, figuratributaria, ncm):
        ParametrizacaoFiscalFigurasTributariasDAO().inserirFiguraTributariaTemplate(figuratributaria, ncm)

    def inserirFiguraTributariaNCM(self, figuratributaria, ncm):
        ParametrizacaoFiscalFigurasTributariasDAO().inserirFiguraTributariaNCM(figuratributaria, ncm)

    def atualizarFiguraTributaria(self, figuratributaria, ncm):
        ParametrizacaoFiscalFigurasTributariasDAO().atualizarFiguraTributaria(figuratributaria, ncm)