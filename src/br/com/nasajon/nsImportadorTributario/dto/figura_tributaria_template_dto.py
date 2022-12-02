# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class FiguraTributariaTemplateDTO:

    def __init__(self):
        self.__figuratributaria = ''

    @property
    def figuratributaria(self) -> str:
        return self.__figuratributaria

    @figuratributaria.setter
    def figuratributaria(self, value: str):
        self.__figuratributaria = value