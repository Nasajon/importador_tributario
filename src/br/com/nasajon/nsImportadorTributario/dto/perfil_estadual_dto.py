# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class PerfilEstadualDTO:

    def __init__(self):
        self.__uf_referencia = ""
        self.__pl_estabelecimento = ""
        self.__pl_icms_aliquota_interna = ""
        self.__pl_icms_cst_contribuinte_icms = ""
        self.__pl_icms_cst_nao_contribuinte_icms = ""
        self.__pl_icms_modalidade_base_calculo = ""
        self.__pl_icms_aliquota_fecp = ""
        self.__pl_icms_percentual_diferimento = ""
        self.__pl_icms_percentual_reducao = ""
        self.__pl_icms_st_aliquota_fecp = ""
        self.__pl_icms_st_percentual_mva = ""
        self.__pl_icms_st_percentual_reducao = ""
        self.__pl_icms_st_modalidade_base_calculo = ""
        self.__pl_icms_st_forma_cobranca_st = ""
        self.__pl_icms_uf_destino = ""
        self.__entrada = ""
        self.__saida = ""

    @property
    def uf_referencia(self) -> str:
        return self.__uf_referencia

    @uf_referencia.setter
    def uf_referencia(self, value: str):
        self.__uf_referencia = value

    @property
    def pl_estabelecimento(self) -> str:
        return self.__pl_estabelecimento

    @pl_estabelecimento.setter
    def pl_estabelecimento(self, value: str):
        self.__pl_estabelecimento = value

    @property
    def pl_icms_aliquota_interna(self) -> str:
        return self.__pl_icms_aliquota_interna

    @pl_icms_aliquota_interna.setter
    def pl_icms_aliquota_interna(self, value: str):
        self.__pl_icms_aliquota_interna = value

    @property
    def pl_icms_cst_contribuinte_icms(self) -> str:
        return self.__pl_icms_cst_contribuinte_icms

    @pl_icms_cst_contribuinte_icms.setter
    def pl_icms_cst_contribuinte_icms(self, value: str):
        self.__pl_icms_cst_contribuinte_icms = value

    @property
    def pl_icms_cst_nao_contribuinte_icms(self) -> str:
        return self.__pl_icms_cst_nao_contribuinte_icms

    @pl_icms_cst_nao_contribuinte_icms.setter
    def pl_icms_cst_nao_contribuinte_icms(self, value: str):
        self.__pl_icms_cst_nao_contribuinte_icms = value

    @property
    def pl_icms_modalidade_base_calculo(self) -> str:
        return self.__pl_icms_modalidade_base_calculo

    @pl_icms_modalidade_base_calculo.setter
    def pl_icms_modalidade_base_calculo(self, value: str):
        self.__pl_icms_modalidade_base_calculo = value

    @property
    def pl_icms_aliquota_fecp(self) -> str:
        return self.__pl_icms_aliquota_fecp

    @pl_icms_aliquota_fecp.setter
    def pl_icms_aliquota_fecp(self, value: str):
        self.__pl_icms_aliquota_fecp = value

    @property
    def pl_icms_percentual_diferimento(self) -> str:
        return self.__pl_icms_percentual_diferimento

    @pl_icms_percentual_diferimento.setter
    def pl_icms_percentual_diferimento(self, value: str):
        self.__pl_icms_percentual_diferimento = value

    @property
    def pl_icms_percentual_reducao(self) -> str:
        return self.__pl_icms_percentual_reducao

    @pl_icms_percentual_reducao.setter
    def pl_icms_percentual_reducao(self, value: str):
        self.__pl_icms_percentual_reducao = value

    @property
    def pl_icms_st_aliquota_fecp(self) -> str:
        return self.__pl_icms_st_aliquota_fecp

    @pl_icms_st_aliquota_fecp.setter
    def pl_icms_st_aliquota_fecp(self, value: str):
        self.__pl_icms_st_aliquota_fecp = value

    @property
    def pl_icms_st_percentual_mva(self) -> str:
        return self.__pl_icms_st_percentual_mva

    @pl_icms_st_percentual_mva.setter
    def pl_icms_st_percentual_mva(self, value: str):
        self.__pl_icms_st_percentual_mva = value

    @property
    def pl_icms_st_percentual_reducao(self) -> str:
        return self.__pl_icms_st_percentual_reducao

    @pl_icms_st_percentual_reducao.setter
    def pl_icms_st_percentual_reducao(self, value: str):
        self.__pl_icms_st_percentual_reducao = value

    @property
    def pl_icms_st_modalidade_base_calculo(self) -> str:
        return self.__pl_icms_st_modalidade_base_calculo

    @pl_icms_st_modalidade_base_calculo.setter
    def pl_icms_st_modalidade_base_calculo(self, value: str):
        self.__pl_icms_st_modalidade_base_calculo = value

    @property
    def pl_icms_st_forma_cobranca_st(self) -> str:
        return self.__pl_icms_st_forma_cobranca_st

    @pl_icms_st_forma_cobranca_st.setter
    def pl_icms_st_forma_cobranca_st(self, value: str):
        self.__pl_icms_st_forma_cobranca_st = value

    @property
    def pl_icms_uf_destino(self) -> str:
        return self.__pl_icms_uf_destino

    @pl_icms_uf_destino.setter
    def pl_icms_uf_destino(self, value: str):
        self.__pl_icms_uf_destino = value

    @property
    def entrada(self) -> str:
        return self.__entrada

    @entrada.setter
    def entrada(self, value: str):
        self.__entrada = value

    @property
    def saida(self) -> str:
        return self.__saida

    @saida.setter
    def saida(self, value: str):
        self.__saida = value