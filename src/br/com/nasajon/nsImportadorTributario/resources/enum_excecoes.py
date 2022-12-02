# !/usr/bin/env python
# -*- coding: cp1252 -*-
from enum import Enum


class EnumExcecoes(Enum):
    """
    Enumerado para exceções encontradas na importação de NFCes.
    Em todos os casos o arquivo XML será movido da pasta de importações.
    """
    # Inconsistências na formatação do arquivo XML, seja de TAG, caracter inválido, etc...
    FORMATACAO_INVALIDA = "XML mal formatado."

    # CFOP desconhecido, inexistente ou fora do patrão aceitável
    CFOP_DESCONHECIDO = "CFOP inválido ou inconsistente."

    # Chave acesso inválida para uma NFCe
    CHAVE_INVALIDA = "Chave de Acesso inválida."
    
    # Tipo não suportado
    TIPO_INVALIDO = "Tipo do documento não suportado."

    # Estabelecimento não encontrado no banco de dados selecionado
    EMITENTE_DESCONHECIDO = "Emitente (Estabelecimento) não encontrado."

    # Estabelecimento não encontrado no banco de dados selecionado
    ESTABELECIMENTO_DESCONHECIDO = "Estabelecimento não encontrado."

    # Inconsistências genéricas não categorizadas
    DOCUMENTO_DUPLICADO = "Documento duplicado na pasta de XMLs. Movendo arquivo para importadas."

    # Inconsistências genéricas não categorizadas
    DESCONHECIDO = "Erro Desconhecido."

    # Formato do arquivo segue modelo 65 porém não trata-se de uma NFCe. Exemplo: XML de ciência da operação.
    XML_INCOMPATIVEL = 'Não foi possível interpretar a estrutura do XML. Verifique se o arquivo contém erros em tags ou possui conteúdo válido.'

    # Fora do período informado no .ini
    PERIODO_INVALIDO = "Fora do período selecionado"

