# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class OperacaoDTO:

    def __init__(self):
        self.__pl_tipo = ""
        self.__pl_natureza = ""
        self.__pl_operacao_codigo = ""
        self.__pl_operacao_descricao = ""

    @property
    def pl_tipo(self) -> str:
        return self.__pl_tipo

    @pl_tipo.setter
    def pl_tipo(self, value: str):
        self.__pl_tipo = value

    @property
    def pl_natureza(self) -> str:
        return self.__pl_natureza

    @pl_natureza.setter
    def pl_natureza(self, value: str):
        self.__pl_natureza = value

    @property
    def pl_operacao_codigo(self) -> str:
        return self.__pl_operacao_codigo

    @pl_operacao_codigo.setter
    def pl_operacao_codigo(self, value: str):
        self.__pl_operacao_codigo = value

    @property
    def pl_operacao_descricao(self) -> str:
        return self.__pl_operacao_descricao

    @pl_operacao_descricao.setter
    def pl_operacao_descricao(self, value: str):
        self.__pl_operacao_descricao = value