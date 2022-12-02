# !/usr/bin/env python
# -*- coding: cp1252 -*-
from uuid import UUID

class CfopDTO:

    def __init__(self):
        self.__id = ""

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value