#!/usr/bin/env python
# -*- coding: cp1252 -*-

from src.br.com.nasajon.nsImportadorTributario.resources.enum_excecoes import EnumExcecoes
from src.br.com.nasajon.exceptions.nao_suportado import Nao_Suportado, Excecao
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_move_arquivos import ControladorMoveArquivos
from src.br.com.nasajon.resources.utilidades_log import ModuloLog
from src.br.com.nasajon.domain.nfce import NFCE

class ControladorExcecoes:
    """
    Controlador com o objetivo de formatar mensagens de exce��o al�m de mover arquivos que estejam dentro
    desses par�metros para pastas corretas.
    """
    def formatarExcecao(self, excecao: EnumExcecoes, arquivo: str, *detalhes):
        mensagem_excecao = excecao.value

        if detalhes != ():
            ModuloLog.excecao(mensagem_excecao, arquivo, detalhes[0])
        else:
            ModuloLog.excecao(mensagem_excecao, arquivo)
            try:
                if mensagem_excecao != EnumExcecoes.XML_INCOMPATIVEL:
                    raise Excecao(arquivo, mensagem_excecao)
                else:
                    raise Nao_Suportado(arquivo, mensagem_excecao)
            except:
                pass


    def notificarNotaDuplicada(self, nota: NFCE):
        ModuloLog.excecao(EnumExcecoes.DOCUMENTO_DUPLICADO.value,nota.codigo_emitente,nota.identificador)
        ControladorMoveArquivos.notificaImportado(nota)
