# !/usr/bin/env python
# -*- coding: cp1252 -*-
from enum import Enum


class EnumParametros(Enum):
    """
    Enumerado para guardar os Par�metros suportados pelo sistema
    """
    SGBD = "BANCO_DE_DADOS.banco"
    SERVIDOR = "BANCO_DE_DADOS.servidor"
    NOME_BD = "BANCO_DE_DADOS.nome_banco"
    USUARIO = "BANCO_DE_DADOS.usuario"
    SENHA = "BANCO_DE_DADOS.senha"
    PORTA = "BANCO_DE_DADOS.porta"
    ARQUIVO_DADOS = "GERAL.arquivo_dados"
    PASTA_XML = "GERAL.pasta_xml"
    PASTA_SAIDA = "GERAL.pasta_saida"
    SOBREPOR_DOCUMENTOS = "GERAL.sobrepor_documentos"
    ESTABELECIMENTOS = "GERAL.estabelecimentos"
    ANOS_FISCAIS = "GERAL.anos_fiscais"
    ICMS_DESONERADO_DESCONTO = "GERAL.icms_desonerado_como_desconto"
    ATUALIZAR_PRODUTOS = "GERAL.atualizar_produtos"
    MODO_SERVICO = "GERAL.modo_servico"
    IMPORTAR_SEM_PROTOCOLO = "GERAL.importar_sem_protocolo_autorizacao"
    EMAIL_LOG = "GERAL.email_log"
    IDENTIFICAR_ENCODING = "GERAL.identificar_encoding"
    DESABILITAR_LOG = "GERAL.desabilitar_log"
    TIPO_DOCUMENTO = "GERAL.tipo_documento"
    AJUSTA_CHAVE_ACESSO = "GERAL.ajusta_chave_acesso"


