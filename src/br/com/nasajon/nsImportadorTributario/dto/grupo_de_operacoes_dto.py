# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class GrupoDeOperacoesDTO:

    def __init__(self):
        self.__grupodeoperacao = ""

    @property
    def grupodeoperacao(self) -> str:
        return self.__grupodeoperacao

    @grupodeoperacao.setter
    def grupodeoperacao(self, value: str):
        self.__grupodeoperacao = value