# !/usr/bin/env python
# -*- coding: cp1252 -*-
from enum import Enum


class EnumExcecoes(Enum):
    """
    Enumerado para exce��es encontradas na importa��o de NFCes.
    Em todos os casos o arquivo XML ser� movido da pasta de importa��es.
    """
    # Inconsist�ncias na formata��o do arquivo XML, seja de TAG, caracter inv�lido, etc...
    FORMATACAO_INVALIDA = "XML mal formatado."

    # CFOP desconhecido, inexistente ou fora do patr�o aceit�vel
    CFOP_DESCONHECIDO = "CFOP inv�lido ou inconsistente."

    # Chave acesso inv�lida para uma NFCe
    CHAVE_INVALIDA = "Chave de Acesso inv�lida."
    
    # Tipo n�o suportado
    TIPO_INVALIDO = "Tipo do documento n�o suportado."

    # Estabelecimento n�o encontrado no banco de dados selecionado
    EMITENTE_DESCONHECIDO = "Emitente (Estabelecimento) n�o encontrado."

    # Estabelecimento n�o encontrado no banco de dados selecionado
    ESTABELECIMENTO_DESCONHECIDO = "Estabelecimento n�o encontrado."

    # Inconsist�ncias gen�ricas n�o categorizadas
    DOCUMENTO_DUPLICADO = "Documento duplicado na pasta de XMLs. Movendo arquivo para importadas."

    # Inconsist�ncias gen�ricas n�o categorizadas
    DESCONHECIDO = "Erro Desconhecido."

    # Formato do arquivo segue modelo 65 por�m n�o trata-se de uma NFCe. Exemplo: XML de ci�ncia da opera��o.
    XML_INCOMPATIVEL = 'N�o foi poss�vel interpretar a estrutura do XML. Verifique se o arquivo cont�m erros em tags ou possui conte�do v�lido.'

    # Fora do per�odo informado no .ini
    PERIODO_INVALIDO = "Fora do per�odo selecionado"

