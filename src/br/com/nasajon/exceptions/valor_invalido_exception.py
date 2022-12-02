#!/usr/bin/env python
# -*- coding: cp1252 -*-
class ValorInvalidoException(Exception):
    """
    Classe de Exceção Personalizada para as Validações de Valor dos Objetos
    """
    def __init__(self, valor: str):
        """
        Construtor da classe ValorInvalidoException
        Args:
            valor:  Valor que provocou o erro na tentativa de atribuição
        """
        self.__mensagemPadrao = "Valor Inválido"
        super().__init__(
            self.__mensagemPadrao
            if valor == None
            else self.__mensagemPadrao + ": " + str(valor)
        )