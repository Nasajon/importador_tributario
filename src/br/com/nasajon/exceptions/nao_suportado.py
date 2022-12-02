#!/usr/bin/env python
# -*- coding: cp1252 -*-



class Nao_Suportado(Exception):
    """
    Classe de exce��o para XML de modelo ou caracter�stica n�o suportada
    """

    def __init__(self, arquivo : str, valor: str):
        from br.com.nasajon.nsImportadorTributario.controller.nsImportadorTributario import ControladorMoveArquivos
        self.__mensagemPadrao = "XML n�o suportado"
        super().__init__(
            self.__mensagemPadrao
            if valor == None
            else self.__mensagemPadrao + ": " + str(valor)
        )
        ControladorMoveArquivos.notificaNaoSuportada(arquivo)

class Excecao(Exception):
    """
    Classe de exce��o para XML de modelo ou caracter�stica n�o suportada
    """

    def __init__(self, arquivo : str, valor: str):
        from br.com.nasajon.nsImportadorTributario.controller.nsImportadorTributario import ControladorMoveArquivos
        self.__mensagemPadrao = "Exce��o"
        super().__init__(
            self.__mensagemPadrao
            if valor == None
            else self.__mensagemPadrao + ": " + str(valor)
        )
        ControladorMoveArquivos.notificaNaoImportado(arquivo)