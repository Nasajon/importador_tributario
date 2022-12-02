# !/usr/bin/env python
# -*- coding: cp1252 -*-
from enum import Enum


class EnumTipoDocumento(Enum):
    """
    Enumerado para guardar os tipos de documentos suportados
    """
    NFCE = "NFCE"
    CTE = "CTE"
    NFSE = "NFSE"
    CONTROLLER = "CONTROLLER"


