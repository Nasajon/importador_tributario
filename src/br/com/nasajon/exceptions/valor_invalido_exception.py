#!/usr/bin/env python
# -*- coding: cp1252 -*-
class ValorInvalidoException(Exception):
    """
    Classe de Exce��o Personalizada para as Valida��es de Valor dos Objetos
    """
    def __init__(self, valor: str):
        """
        Construtor da classe ValorInvalidoException
        Args:
            valor:  Valor que provocou o erro na tentativa de atribui��o
        """
        self.__mensagemPadrao = "Valor Inv�lido"
        super().__init__(
            self.__mensagemPadrao
            if valor == None
            else self.__mensagemPadrao + ": " + str(valor)
        )