# !/usr/bin/env python
# -*- coding: cp1252 -*-


class Singleton(type):
    """
    Classe de Apoio para criação de Singletons
    !Copiei da internet!
    """
    
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
