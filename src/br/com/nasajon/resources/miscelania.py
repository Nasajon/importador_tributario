# !/usr/bin/env python
# -*- coding: cp1252 -*-
import os
import sys
import traceback
from datetime import datetime
from typing import List


class Miscel:
    """
    Classe que contém a Miscelânia de utilidades
    """

    @staticmethod
    def elementoMaisComunNaLista(lista: List) -> object:
        """
        Retorna o elemento que mais se repete na lista
        :param lista: lista a ser analisada
        :return: o elemento mais comum
        """
        if not lista:
            return None
        return max(set(lista), key=lista.count)

    @staticmethod
    def preencherAtributo(objeto, nomeAtributo, valor) -> object:
        """
        Preenche o atributo desejado no objeto e devolve o objeto preenchido
        :param objeto: objeto a ser preenchido
        :param nomeAtributo: nome do atributo a ser preenchido
        :param valor: valor a ser atribuído ao atributo do objeto
        :return: objeto com o valor atribuído
        """
        if hasattr(objeto, nomeAtributo):
            setattr(objeto, nomeAtributo, valor)
        return objeto

    @staticmethod
    def preencherObjeto(registro: dict, classeRetorno, propagarExcecoes: bool = True) -> object:
        """
        Preenche um objeto a partir de um dict retornado de uma query

        :param registro: dict(nome_campo: valor) com os dados retornados\
        pela consulta
        :param classeRetorno: Classe dos objetos Dto que serão retornados na\
        lista
        :param propagarExcecoes: Se as exceções devem ser porpagadas ou abafadas
        :return: objeto preenchido
        """
        try:
            objeto = classeRetorno()
            for chave, valor in registro.items():
                Miscel.preencherAtributo(objeto, chave, valor)
            return objeto
        except Exception as e:
            tb = traceback.format_exc()
            if propagarExcecoes:
                raise e
            else:
                print('Erro ao preencher objeto', tb)
                return None

    @staticmethod
    def dataHoraAtual() -> str:
        """
        Retorna Data e Hora atuais no formato 'YYYY-mm-DD HH:MM:SS'
        :return: Data e Hora atuais
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def dataAtual() -> str:
        """
        Retorna a Data atual no formato 'YYYY-mm-DD'
        :return: Data atual
        """
        return datetime.now().strftime("%Y-%m-%d")

    @staticmethod
    def horaAtual() -> str:
        """
        Retorna a hora atual no formato 'HH:MM:SS'
        :return: Hora atual
        """
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def formatarDataHora(dataHora: datetime) -> str:
        """
        Retorna Data e Hora informados no formato 'YYYY-mm-DD HH:MM:SS'
        :param dataHora: Data e Hora a serem formatados
        :return: Data e Hora formatados
        """
        return dataHora.now().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def formatarData(data: datetime) -> str:
        """
        Retorna a Data informada no formato 'YYYY-mm-DD'
        :param data: data a ser formatada
        :return: Data formatada
        """
        return data.now().strftime("%Y-%m-%d")

    @staticmethod
    def formatarHora(dataHora: datetime) -> str:
        """
        Retorna a Hora informada no formato 'HH:MM:SS'
        :param dataHora: hora a formatar
        :return: Hora formatada
        """
        return dataHora.now().strftime("%H:%M:%S")

    @staticmethod
    def formatarErro(identificador: str, e: Exception, stackTrace: str) -> str:
        """
        Retorna mensagens de erro tratadas
        :param identificador: Identificação (Tipo) do erro
        :param e: Exceção levantada
        :param stackTrace: Stack Trace
        :return: Texto de erro formatado
        """
        if identificador is None:
            identificador = "desconhecido"
        return ';{};Erro:;"{}";"{}";"{}"'.format(Miscel.dataHoraAtual(), identificador, str(e), stackTrace)

    @staticmethod
    def formatarAviso(identificador: str, mensagem: str, stackTrace: str) -> str:
        """
        Retorna mensagens de advertência (warning) tratadas
        :param identificador: Identificação (Tipo) do aviso
        :param mensagem: Mensagem ao usuário
        :param stackTrace: Stack Trace
        :return: Mensagem de advertência formatada
        """
        if identificador is None:
            identificador = "desconhecido"

        aviso = f';{Miscel.dataHoraAtual()};Aviso:;"{identificador}";"{mensagem}"'

        if stackTrace == "":
            aviso = aviso + f';{stackTrace}'
        return aviso

    @staticmethod
    def retornarPastaDaAplicacao() -> str:
        """
        Retorna em qual pasta a aplicação está sendo executada
        :return: pasta da aplicação
        """
        # Verifica se é um executável (Frozen) ou um script
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        elif __file__:
            caminhoDaAplicacao = os.path.dirname(__file__)
            return os.path.abspath(os.path.join(caminhoDaAplicacao, os.pardir))

    @staticmethod
    def heartBeat():
        """ Retorna quantos segundos a aplicação deverá aguardar após concluir uma importação.
        Destina-se a evitar processamento desnecessário """
        return 5