#!/usr/bin/env python
# -*- coding: cp1252 -*-

from typing import List
import uuid
from src.br.com.nasajon.persistence.conexao_padrao import ConexaoPadrao
from src.br.com.nasajon.resources.utilidades_banco import UtilidadesBanco

from src.br.com.nasajon.nsImportadorTributario.dto.perfil_federal_dto import PerfilFederalDTO

class ParametrizacaoFiscalPerfisFederaisDAO:

    def __init__(self, conexao: ConexaoPadrao = None):
        self.__conexao = conexao

    def excluirColunaTbPerfilFedId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbPerfilFedId(),
            [],
            False,
            False)

    def excluirColunaTbPerfilFedValidadeId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbPerfilFedValidadeId(),
            [],
            False,
            False)

    def excluirColunaTbPerfilFedValidadeImpostosId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLExcluirColunaTbPerfilFedValidadeImpostosId(),
            [],
            False,
            False)

    def addColunaTbPerfilFedId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbPerfilFedId(),
            [],
            False,
            False)

    def addColunaTbPerfilFedValidadeId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbPerfilFedValidadeId(),
            [],
            False,
            False)

    def addColunaTbPerfilFedValidadeImpostosId(self):
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAddColunaTbPerfilFedValidadeImpostosId(),
            [],
            False,
            False)

    def selecionarPerfisFederais(self) -> List[PerfilFederalDTO]:
        return UtilidadesBanco.executarConsulta(
                self.__conexao,
                self.obterSQLSelecionarPerfisFederais(),
                [],
                PerfilFederalDTO
            )

    def inserirPerfilTributarioFederal(self, codigo, descricao) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            codigo,
            descricao
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioFederal(),
            parametros,
            False,
            False)
        return guid

    def inserirPerfilTributarioFederalValidades(self, perfiltrib_fed, data) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            perfiltrib_fed,
            data
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioFederalValidades(),
            parametros,
            False,
            False)
        return guid

    def inserirPerfilTributarioFederalValidadesImpostos(
            self,
            perfiltrib_fed_validade,
            ipi_cst_entrada,
            pl_ipi_aliquota,
            ipi_cst,
            pis_cst,
            pl_pis_aliquota,
            cofins_cst,
            pl_cofins_aliquota) -> str:
        guid = str(uuid.uuid4())
        parametros = [
            guid,
            perfiltrib_fed_validade,
            ipi_cst_entrada,
            pl_ipi_aliquota,
            ipi_cst,
            pis_cst,
            pl_pis_aliquota,
            cofins_cst,
            pl_cofins_aliquota
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLInserirPerfilTributarioFederalValidadesImpostos(),
            parametros,
            False,
            False)
        return guid

    def atualizarPerfilFederal(
            self,
            perfiltrib_fed,
            perfiltrib_fed_validade,
            perfiltrib_fed_validade_imposto,
            pl_pis_cst,
            pl_pis_aliquota,
            pl_cofins_cst,
            pl_cofins_aliquota,
            pl_ipi_cst,
            pl_ipi_aliquota):
        parametros = [
            perfiltrib_fed,
            perfiltrib_fed_validade,
            perfiltrib_fed_validade_imposto,
            pl_pis_cst,
            pl_pis_aliquota,
            pl_cofins_cst,
            pl_cofins_aliquota,
            pl_ipi_cst,
            pl_ipi_aliquota
        ]
        UtilidadesBanco.executarComando(
            self.__conexao,
            self.obterSQLAtualizarPerfilFederal(),
            parametros,
            False,
            False)

    @staticmethod
    def obterSQLExcluirColunaTbPerfilFedId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_perfil_fed_id"

    @staticmethod
    def obterSQLExcluirColunaTbPerfilFedValidadeId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_perfil_fed_validade_id"

    @staticmethod
    def obterSQLExcluirColunaTbPerfilFedValidadeImpostosId() -> str:
        return "ALTER TABLE tmp_imp_tributacao DROP COLUMN IF EXISTS tb_perfil_fed_validade_impostos_id"

    @staticmethod
    def obterSQLAddColunaTbPerfilFedId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_perfil_fed_id UUID"

    @staticmethod
    def obterSQLAddColunaTbPerfilFedValidadeId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_perfil_fed_validade_id UUID"

    @staticmethod
    def obterSQLAddColunaTbPerfilFedValidadeImpostosId() -> str:
        return "ALTER TABLE tmp_imp_tributacao ADD COLUMN tb_perfil_fed_validade_impostos_id UUID"

    @staticmethod
    def obterSQLSelecionarPerfisFederais() -> str:
        return "\
            SELECT\
                pl_pis_cst,\
                pl_pis_aliquota,\
                pl_cofins_cst,\
                pl_cofins_aliquota,\
                pl_ipi_cst,\
                pl_ipi_aliquota\
            FROM\
                tmp_imp_tributacao\
            GROUP BY\
                1, 2, 3, 4, 5, 6\
        "

    @staticmethod
    def obterSQLInserirPerfilTributarioFederal() -> str:
        return "INSERT INTO estoque.perfiltrib_fed (perfiltrib_fed, codigo, descricao) VALUES (%s, %s, %s)"

    @staticmethod
    def obterSQLInserirPerfilTributarioFederalValidades() -> str:
        return "INSERT INTO estoque.perfiltrib_fed_validades (perfiltrib_fed_validade, perfiltrib_fed, data) VALUES (%s, %s, %s)"

    @staticmethod
    def obterSQLInserirPerfilTributarioFederalValidadesImpostos() -> str:
        return "\
            INSERT INTO estoque.perfiltrib_fed_validades_impostos(\
                perfiltrib_fed_validade_imposto,\
                perfiltrib_fed_validade,\
                ipi_cst_entrada,\
                ipi_aliquota,\
                ipi_cst_saida,\
                pis_cst,\
                pis_aliquota,\
                cofins_cst,\
                cofins_aliquota\
            ) VALUES(\
                %s,\
                %s,\
                %s,\
                (replace(%s, ',', '.'))::numeric,\
                %s,\
                %s,\
                (replace(%s, ',', '.'))::numeric,\
                %s,\
                (replace(%s, ',', '.'))::numeric\
            )\
        "

    @staticmethod
    def obterSQLAtualizarPerfilFederal() -> str:
        return "\
            UPDATE\
                tmp_imp_tributacao\
            SET\
                tb_perfil_fed_id = %s,\
                tb_perfil_fed_validade_id = %s,\
                tb_perfil_fed_validade_impostos_id= %s\
            WHERE\
                pl_pis_cst = %s AND\
                pl_pis_aliquota = %s AND\
                pl_cofins_cst = %s AND\
                pl_cofins_aliquota = %s AND\
                pl_ipi_cst = %s AND\
                pl_ipi_aliquota = %s\
        "