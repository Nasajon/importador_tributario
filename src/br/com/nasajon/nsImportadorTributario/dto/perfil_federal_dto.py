# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class PerfilFederalDTO:

    def __init__(self):
        self.__pl_pis_cst = ""
        self.__pl_pis_aliquota = ""
        self.__pl_cofins_cst = ""
        self.__pl_cofins_aliquota = ""
        self.__pl_ipi_cst = ""
        self.__pl_ipi_aliquota = ""

    @property
    def pl_pis_cst(self) -> str:
        return self.__pl_pis_cst

    @pl_pis_cst.setter
    def pl_pis_cst(self, value: str):
        self.__pl_pis_cst = value

    @property
    def pl_pis_aliquota(self) -> str:
        return self.__pl_pis_aliquota

    @pl_pis_aliquota.setter
    def pl_pis_aliquota(self, value: str):
        self.__pl_pis_aliquota = value

    @property
    def pl_cofins_cst(self) -> str:
        return self.__pl_cofins_cst

    @pl_cofins_cst.setter
    def pl_cofins_cst(self, value: str):
        self.__pl_cofins_cst = value

    @property
    def pl_cofins_aliquota(self) -> str:
        return self.__pl_cofins_aliquota

    @pl_cofins_aliquota.setter
    def pl_cofins_aliquota(self, value: str):
        self.__pl_cofins_aliquota = value

    @property
    def pl_ipi_cst(self) -> str:
        return self.__pl_ipi_cst

    @pl_ipi_cst.setter
    def pl_ipi_cst(self, value: str):
        self.__pl_ipi_cst = value

    @property
    def pl_ipi_aliquota(self) -> str:
        return self.__pl_ipi_aliquota

    @pl_ipi_aliquota.setter
    def pl_ipi_aliquota(self, value: str):
        self.__pl_ipi_aliquota = value