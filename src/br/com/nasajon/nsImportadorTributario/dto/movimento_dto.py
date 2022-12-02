# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class MovimentoDTO:

    def __init__(self):
        self.__tb_operacao_id = ""
        self.__pl_cfop = ""
        self.__pl_mov_fiscal = ""
        self.__pl_mov_prop_em_terc = ""
        self.__pl_mov_terc_em_meu_poder = ""
        self.__pl_tipo = ""

    @property
    def tb_operacao_id(self) -> str:
        return self.__tb_operacao_id

    @tb_operacao_id.setter
    def tb_operacao_id(self, value: str):
        self.__tb_operacao_id = value

    @property
    def pl_cfop(self) -> str:
        return self.__pl_cfop

    @pl_cfop.setter
    def pl_cfop(self, value: str):
        self.__pl_cfop = value

    @property
    def pl_mov_fiscal(self) -> str:
        return self.__pl_mov_fiscal

    @pl_mov_fiscal.setter
    def pl_mov_fiscal(self, value: str):
        self.__pl_mov_fiscal = value

    @property
    def pl_mov_prop_em_terc(self) -> str:
        return self.__pl_mov_prop_em_terc

    @pl_mov_prop_em_terc.setter
    def pl_mov_prop_em_terc(self, value: str):
        self.__pl_mov_prop_em_terc = value

    @property
    def pl_mov_terc_em_meu_poder(self) -> str:
        return self.__pl_mov_terc_em_meu_poder

    @pl_mov_terc_em_meu_poder.setter
    def pl_mov_terc_em_meu_poder(self, value: str):
        self.__pl_mov_terc_em_meu_poder = value

    @property
    def pl_tipo(self) -> str:
        return self.__pl_tipo

    @pl_tipo.setter
    def pl_tipo(self, value: str):
        self.__pl_tipo = value

