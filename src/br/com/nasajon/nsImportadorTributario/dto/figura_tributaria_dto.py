# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class FiguraTributariaDTO:

    def __init__(self):
        self.__ncm = ""
        self.__id = ""
        self.__pl_ncm = ""
        self.__tb_operacao_id = ""
        self.__tb_perfil_est_id = ""
        self.__tb_perfil_fed_id = ""

    @property
    def ncm(self) -> str:
        return self.__ncm

    @ncm.setter
    def ncm(self, value: str):
        self.__ncm = value

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def pl_ncm(self) -> str:
        return self.__pl_ncm

    @pl_ncm.setter
    def pl_ncm(self, value: str):
        self.__pl_ncm = value

    @property
    def tb_operacao_id(self) -> str:
        return self.__tb_operacao_id

    @tb_operacao_id.setter
    def tb_operacao_id(self, value: str):
        self.__tb_operacao_id = value

    @property
    def tb_perfil_est_id(self) -> str:
        return self.__tb_perfil_est_id

    @tb_perfil_est_id.setter
    def tb_perfil_est_id(self, value: str):
        self.__tb_perfil_est_id = value

    @property
    def tb_perfil_fed_id(self) -> str:
        return self.__tb_perfil_fed_id

    @tb_perfil_fed_id.setter
    def tb_perfil_fed_id(self, value: str):
        self.__tb_perfil_fed_id = value
