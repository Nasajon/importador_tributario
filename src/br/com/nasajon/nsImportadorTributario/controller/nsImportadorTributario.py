#!/usr/bin/env python
# -*- coding: cp1252 -*-

import multiprocessing
import uuid
from re import match
import sys
import gc
import threading
import traceback
from src.br.com.nasajon.resources.singleton import Singleton
from src.br.com.nasajon.resources.utilidades_log import ModuloLog

from typing import List
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_tabela_temporaria import ControladorTabelaTemporaria
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_carregar_dados import ControladorCarregarDados
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_operacoes import ControladorParametrizacaoFiscalOperacoes
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_operacoes_cfops_movimentos import ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_perfis_federais import ControladorParametrizacaoFiscalPerfisFederais
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_perfis_estaduais import ControladorParametrizacaoFiscalPerfisEstaduais
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_figuras_tributarias import ControladorParametrizacaoFiscalFigurasTributarias
from src.br.com.nasajon.nsImportadorTributario.controller.controlador_parametrizacao_fiscal_atualizar_produtos import ControladorParametrizacaoFiscalAtualizarProdutos
from src.br.com.nasajon.nsImportadorTributario.dto.operacao_dto import OperacaoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.grupo_de_operacoes_dto import GrupoDeOperacoesDTO
from src.br.com.nasajon.nsImportadorTributario.dto.movimento_dto import MovimentoDTO
from src.br.com.nasajon.nsImportadorTributario.dto.perfil_federal_dto import PerfilFederalDTO
from src.br.com.nasajon.nsImportadorTributario.dto.perfil_estadual_dto import PerfilEstadualDTO
from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_dto import FiguraTributariaDTO
from src.br.com.nasajon.nsImportadorTributario.dto.figura_tributaria_template_dto import FiguraTributariaTemplateDTO
from src.br.com.nasajon.constants.constants import Constants

mutex_notificacao = threading.Lock()

class Importador(metaclass=Singleton):

    def __init__(self):
        self.__log = ModuloLog()
    
    def importar(self):
        try:
            self.__log.iniciarModuloLog()
            self.__log.info("Iniciando importação tributária")

            self.criarTabelaTemporaria()
            self.carregarDados()
            self.importarParametrizacaoFiscalOperacoes()
            self.importarParametrizacaoFiscalOperacoesCFOPsMovimentos()
            self.importarParametrizacaoFiscalPerfisFederais()
            self.importarParametrizacaoFiscalPerfisEstaduais()
            self.importarParametrizacaoFiscalFigurasTributarias()
            self.importarParametrizacaoFiscalAtualizarProdutos()

            self.__log.info("Importação tributária finalizada")
            self.__log.finalizarModuloLog()

        except Exception as e:
            tb = traceback.format_exc()
            self.__log.erro(tb,e)
            sys.exit("Erro {} em {}".format(e, tb))

    def criarTabelaTemporaria(self):
        try:
            self.__log.info("Criando tabela temporária")

            ControladorTabelaTemporaria().criarTabelaTemporaria()

            self.__log.info("Tabela temporária criada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao criar tabela temporária.")
            raise

    def carregarDados(self):
        try:
            self.__log.info("Carregando dados")

            ControladorCarregarDados().carregarDados()

            self.__log.info("Dados carregados")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao carregar dados.")
            raise

    def importarParametrizacaoFiscalOperacoes(self):
        try:
            self.__log.info("Importando Parametrização Fiscal de Operações")

            ControladorParametrizacaoFiscalOperacoes().criarCampoOperacaoID()

            operacoes: List[OperacaoDTO] = ControladorParametrizacaoFiscalOperacoes().selecionarOperacoes()
            for operacao in operacoes:
                operacao_codigo = operacao.pl_operacao_codigo.translate(operacao.pl_operacao_codigo.maketrans(Constants.CONST_TRANSLATE_SPECIAL_CHARACTERS))
                operacao_codigo = operacao_codigo.replace(" ", "")
                operacao_codigo = operacao_codigo.upper()

                if operacao.pl_tipo.upper() == Constants.CONST_ENTRADA:
                    operacao_sinal = 1
                else:
                    operacao_sinal = 0

                operacao_natureza = operacao.pl_natureza.translate(operacao.pl_natureza.maketrans(Constants.CONST_TRANSLATE_SPECIAL_CHARACTERS)).upper()

                operacao_grupo: List[GrupoDeOperacoesDTO] = ControladorParametrizacaoFiscalOperacoes().selecionarGrupoDeOperacoes(operacao_natureza)

                if not operacao_grupo:
                    operacao_grupo[0].grupodeoperacao = ControladorParametrizacaoFiscalOperacoes().inserirGrupoDeOperacoes(operacao_natureza, operacao.pl_natureza)

                operacao_id = ControladorParametrizacaoFiscalOperacoes().inserirOperacao(
                    operacao_codigo,
                    operacao.pl_operacao_descricao,
                    operacao_sinal,
                    operacao_grupo[0].grupodeoperacao)

                ControladorParametrizacaoFiscalOperacoes().atualizarOperacaoId(
                    operacao_id,
                    operacao.pl_tipo,
                    operacao.pl_natureza,
                    operacao.pl_operacao_codigo,
                    operacao.pl_operacao_descricao,
                )

            self.__log.info("Parametrização Fiscal de Operações importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal de Operações.")
            raise

    def importarParametrizacaoFiscalOperacoesCFOPsMovimentos(self):
        try:
            self.__log.info("Importando Parametrização Fiscal de Operações - CFOPs Movimentos")

            movimentos: List[MovimentoDTO] = ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().selecionarMovimentos()
            for movimento in movimentos:

                cfops = movimento.pl_cfop.split(',')
                for cfop_atual in cfops:

                    cfop = ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().selecionarCFOP(cfop_atual)
                    cfop_id = cfop[0].id

                    operacaocfop = ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().inserirOperacoesCFOP(
                        movimento.tb_operacao_id,
                        cfop_id
                    )

                    if movimento.pl_mov_fiscal.upper() == 'SIM':

                        entrada = movimento.pl_tipo.upper() == 'ENTRADA'

                        ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().inserirOperacoesCFOPsSlots(
                            movimento.tb_operacao_id,
                            operacaocfop,
                            'FISCAL',
                            entrada
                        )

                    if movimento.pl_mov_prop_em_terc.upper() == 'SIM':

                        entrada = movimento.pl_tipo.upper() != 'ENTRADA'

                        ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().inserirOperacoesCFOPsSlots(
                            movimento.tb_operacao_id,
                            operacaocfop,
                            'PROP-EMPODERTERC',
                            entrada
                        )

                    if movimento.pl_mov_terc_em_meu_poder.upper() == 'SIM':

                        entrada = movimento.pl_tipo.upper() == 'ENTRADA'

                        ControladorParametrizacaoFiscalOperacoesCFOPsMovimentos().inserirOperacoesCFOPsSlots(
                            movimento.tb_operacao_id,
                            operacaocfop,
                            'TERC-EMSEUPODER',
                            entrada
                        )

            self.__log.info("Parametrização Fiscal de Operações - CFOPs Movimentos importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal de Operações - CFOPs Movimentos.")
            raise

    def importarParametrizacaoFiscalPerfisFederais(self):
        try:
            self.__log.info("Importando Parametrização Fiscal de Perfis Federais")

            ControladorParametrizacaoFiscalPerfisFederais().excluirColunaTbPerfilFedId()
            ControladorParametrizacaoFiscalPerfisFederais().excluirColunaTbPerfilFedValidadeId()
            ControladorParametrizacaoFiscalPerfisFederais().excluirColunaTbPerfilFedValidadeImpostosId()

            ControladorParametrizacaoFiscalPerfisFederais().addColunaTbPerfilFedId()
            ControladorParametrizacaoFiscalPerfisFederais().addColunaTbPerfilFedValidadeId()
            ControladorParametrizacaoFiscalPerfisFederais().addColunaTbPerfilFedValidadeImpostosId()

            contador = 0

            perfis_federais: List[PerfilFederalDTO] = ControladorParametrizacaoFiscalPerfisFederais().selecionarPerfisFederais()
            for perfil_federal in perfis_federais:

                contador += 1
                codigo = str(contador).zfill(4)
                descricao = 'PIS: ' + perfil_federal.pl_pis_cst + ' COFINS: ' + perfil_federal.pl_cofins_cst + ' IPI: ' + perfil_federal.pl_ipi_cst

                perfiltrib_fed = ControladorParametrizacaoFiscalPerfisFederais().inserirPerfilTributarioFederal(codigo, descricao)
                perfiltrib_fed_validade = ControladorParametrizacaoFiscalPerfisFederais().inserirPerfilTributarioFederalValidades(perfiltrib_fed, None)

                match perfil_federal.pl_ipi_cst:
                    case '50':
                        ipi_cst = 1
                    case '51':
                        ipi_cst = 2
                    case '52':
                        ipi_cst = 3
                    case '53':
                        ipi_cst = 4
                    case '54':
                        ipi_cst = 5
                    case '55':
                        ipi_cst = 6
                    case '99':
                        ipi_cst = 7
                    case _:
                        ipi_cst = 0

                match perfil_federal.pl_pis_cst:
                    case '01':
                        pis_cst = 1
                    case '02':
                        pis_cst = 2
                    case '03':
                        pis_cst = 3
                    case '04':
                        pis_cst = 4
                    case '05':
                        pis_cst = 5
                    case '06':
                        pis_cst = 6
                    case '07':
                        pis_cst = 7
                    case '08':
                        pis_cst = 8
                    case '09':
                        pis_cst = 9
                    case '49':
                        pis_cst = 10
                    case '50':
                        pis_cst = 11
                    case '51':
                        pis_cst = 12
                    case '52':
                        pis_cst = 13
                    case '53':
                        pis_cst = 14
                    case '54':
                        pis_cst = 15
                    case '55':
                        pis_cst = 16
                    case '56':
                        pis_cst = 17
                    case '60':
                        pis_cst = 18
                    case '61':
                        pis_cst = 19
                    case '62':
                        pis_cst = 20
                    case '63':
                        pis_cst = 21
                    case '64':
                        pis_cst = 22
                    case '65':
                        pis_cst = 23
                    case '66':
                        pis_cst = 24
                    case '67':
                        pis_cst = 25
                    case '70':
                        pis_cst = 26
                    case '71':
                        pis_cst = 27
                    case '72':
                        pis_cst = 28
                    case '73':
                        pis_cst = 29
                    case '74':
                        pis_cst = 30
                    case '75':
                        pis_cst = 31
                    case '98':
                        pis_cst = 32
                    case '99':
                        pis_cst = 33
                    case '206':
                        pis_cst = 34
                    case _:
                        pis_cst = 0

                match perfil_federal.pl_cofins_cst:
                    case '01':
                        cofins_cst = 1
                    case '02':
                        cofins_cst = 2
                    case '03':
                        cofins_cst = 3
                    case '04':
                        cofins_cst = 4
                    case '05':
                        cofins_cst = 5
                    case '06':
                        cofins_cst = 6
                    case '07':
                        cofins_cst = 7
                    case '08':
                        cofins_cst = 8
                    case '09':
                        cofins_cst = 9
                    case '49':
                        cofins_cst = 10
                    case '50':
                        cofins_cst = 11
                    case '51':
                        cofins_cst = 12
                    case '52':
                        cofins_cst = 13
                    case '53':
                        cofins_cst = 14
                    case '54':
                        cofins_cst = 15
                    case '55':
                        cofins_cst = 16
                    case '56':
                        cofins_cst = 17
                    case '60':
                        cofins_cst = 18
                    case '61':
                        cofins_cst = 19
                    case '62':
                        cofins_cst = 20
                    case '63':
                        cofins_cst = 21
                    case '64':
                        cofins_cst = 22
                    case '65':
                        cofins_cst = 23
                    case '66':
                        cofins_cst = 24
                    case '67':
                        cofins_cst = 25
                    case '70':
                        cofins_cst = 26
                    case '71':
                        cofins_cst = 27
                    case '72':
                        cofins_cst = 28
                    case '73':
                        cofins_cst = 29
                    case '74':
                        cofins_cst = 30
                    case '75':
                        cofins_cst = 31
                    case '98':
                        cofins_cst = 32
                    case '99':
                        cofins_cst = 33
                    case '206':
                        cofins_cst = 34
                    case _:
                        cofins_cst = 0

                perfiltrib_fed_validade_imposto = ControladorParametrizacaoFiscalPerfisFederais().inserirPerfilTributarioFederalValidadesImpostos(
                        perfiltrib_fed_validade,
                        None,
                        perfil_federal.pl_ipi_aliquota,
                        ipi_cst,
                        pis_cst,
                        perfil_federal.pl_pis_aliquota,
                        cofins_cst,
                        perfil_federal.pl_cofins_aliquota
                )

                ControladorParametrizacaoFiscalPerfisFederais().atualizarPerfilFederal(
                        perfiltrib_fed,
                        perfiltrib_fed_validade,
                        perfiltrib_fed_validade_imposto,
                        perfil_federal.pl_pis_cst,
                        perfil_federal.pl_pis_aliquota,
                        perfil_federal.pl_cofins_cst,
                        perfil_federal.pl_cofins_aliquota,
                        perfil_federal.pl_ipi_cst,
                        perfil_federal.pl_ipi_aliquota
                )

            self.__log.info("Parametrização Fiscal de Perfis Federais importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal de Perfis Federais.")
            raise

    def importarParametrizacaoFiscalPerfisEstaduais(self):
        try:
            self.__log.info("Importando Parametrização Fiscal de Perfis Estaduais")

            ControladorParametrizacaoFiscalPerfisEstaduais().excluirColunaTbPerfilEstId()
            ControladorParametrizacaoFiscalPerfisEstaduais().excluirColunaTbPerfilEstValidadeId()

            ControladorParametrizacaoFiscalPerfisEstaduais().addColunaTbPerfilEstId()
            ControladorParametrizacaoFiscalPerfisEstaduais().addColunaTbPerfilEstValidadeId()

            contador = 0

            perfis_estaduais: List[PerfilEstadualDTO] = ControladorParametrizacaoFiscalPerfisEstaduais().selecionarPerfisEstaduais()
            for perfil_estadual in perfis_estaduais:

                contador += 1
                codigo = str(contador).zfill(4)
                descricao = 'CST ' + perfil_estadual.pl_icms_cst_contribuinte_icms;

                perfiltrib_est = ControladorParametrizacaoFiscalPerfisEstaduais().inserirPerfilTributarioEstadual(codigo, descricao, perfil_estadual.uf_referencia, perfil_estadual.pl_icms_aliquota_interna)
                perfiltrib_est_validade = ControladorParametrizacaoFiscalPerfisEstaduais().inserirPerfilTributarioEstadualValidades(perfiltrib_est, None)

                match perfil_estadual.pl_icms_cst_nao_contribuinte_icms:
                    case '00':
                        icms_cst_nao_contr = 1
                    case '10':
                        icms_cst_nao_contr = 2
                    case '20':
                        icms_cst_nao_contr = 3
                    case '30':
                        icms_cst_nao_contr = 4
                    case '40':
                        icms_cst_nao_contr = 5
                    case '41':
                        icms_cst_nao_contr = 6
                    case '50':
                        icms_cst_nao_contr = 7
                    case '51':
                        icms_cst_nao_contr = 8
                    case '60':
                        icms_cst_nao_contr = 9
                    case '70':
                        icms_cst_nao_contr = 10
                    case '90':
                        icms_cst_nao_contr = 11
                    case _:
                        icms_cst_nao_contr = 0

                match perfil_estadual.pl_icms_cst_contribuinte_icms:
                    case '00':
                        icms_cst = 1
                    case '10':
                        icms_cst = 2
                    case '20':
                        icms_cst = 3
                    case '30':
                        icms_cst = 4
                    case '40':
                        icms_cst = 5
                    case '41':
                        icms_cst = 6
                    case '50':
                        icms_cst = 7
                    case '51':
                        icms_cst = 8
                    case '60':
                        icms_cst = 9
                    case '70':
                        icms_cst = 10
                    case '90':
                        icms_cst = 11
                    case _:
                        icms_cst = 0

                match perfil_estadual.pl_icms_st_modalidade_base_calculo:
                    case '0=Preço tabelado ou máximo sugerido':
                        icms_st_mod = 0
                    case '1=Lista Negativa (valor)':
                        icms_st_mod = 1
                    case '2=Lista Positiva (valor)':
                        icms_st_mod = 2
                    case '3=Lista Neutra (valor)':
                        icms_st_mod = 3
                    case '4=Margem Valor Agregado (%)':
                        icms_st_mod = 4
                    case '5=Pauta (valor);':
                        icms_st_mod = 5
                    case _:
                        icms_st_mod = -1

                match perfil_estadual.pl_icms_st_modalidade_base_calculo:
                    case '0=Margem Valor Agregado (%)':
                        icms_mod = 1
                    case '1=Pauta (Valor)':
                        icms_mod = 2
                    case '2=Preço Tabelado Máx. (valor)':
                        icms_mod = 3
                    case '3=Valor da operação':
                        icms_mod = 4
                    case _:
                        icms_mod = 0

                match perfil_estadual.pl_icms_st_modalidade_base_calculo:
                    case 'Não sujeito a Substituição Tributária':
                        icms_st_for_cob = 1
                    case 'Recolhimento do Imposto (Substituto Tributário)':
                        icms_st_for_cob = 2
                    case 'Recolhimento do Imposto (Apenas para operações dentro do Estado)':
                        icms_st_for_cob = 3
                    case 'Recolhimento do Imposto (Com redução de Base/Oper.Interna)':
                        icms_st_for_cob = 4
                    case 'Retenção do Imposto de Terceiros (Distribuidor,Atacadista)':
                        icms_st_for_cob = 5
                    case 'Retenção do Imposto de Terceiros (Apenas para operações dentro do Estado)':
                        icms_st_for_cob = 6
                    case 'Retenção do Imposto de Terceiros (Com redução de Base/Oper.Interna)':
                        icms_st_for_cob = 7
                    case _:
                        icms_st_for_cob = 0

                ControladorParametrizacaoFiscalPerfisEstaduais().inserirPerfilTributarioEstadualValidadesImpostos(
                        perfiltrib_est_validade,
                        perfil_estadual.pl_icms_uf_destino,
                        icms_cst,
                        perfil_estadual.pl_icms_percentual_reducao,
                        perfil_estadual.pl_icms_st_percentual_mva,
                        perfil_estadual.pl_icms_st_percentual_reducao,
                        icms_st_for_cob,
                        perfil_estadual.entrada,
                        perfil_estadual.saida,
                        perfil_estadual.pl_icms_aliquota_fecp,
                        perfil_estadual.pl_icms_percentual_diferimento,
                        icms_st_mod,
                        icms_mod,
                        icms_cst_nao_contr,
                        perfil_estadual.pl_icms_st_aliquota_fecp
                )

                ControladorParametrizacaoFiscalPerfisEstaduais().atualizarPerfilEstadual(
                        perfiltrib_est,
                        perfiltrib_est_validade,
                        perfil_estadual.pl_estabelecimento,
                        perfil_estadual.pl_icms_aliquota_interna,
                        perfil_estadual.pl_icms_cst_contribuinte_icms,
                        perfil_estadual.pl_icms_cst_nao_contribuinte_icms,
                        perfil_estadual.pl_icms_modalidade_base_calculo,
                        perfil_estadual.pl_icms_aliquota_fecp,
                        perfil_estadual.pl_icms_percentual_diferimento,
                        perfil_estadual.pl_icms_percentual_reducao,
                        perfil_estadual.pl_icms_st_aliquota_fecp,
                        perfil_estadual.pl_icms_st_percentual_mva,
                        perfil_estadual.pl_icms_st_percentual_reducao,
                        perfil_estadual.pl_icms_st_modalidade_base_calculo,
                        perfil_estadual.pl_icms_st_forma_cobranca_st,
                        perfil_estadual.pl_icms_uf_destino
                )

            self.__log.info("Parametrização Fiscal de Perfis Estaduais importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal de Perfis Estaduais.")
            raise

    def importarParametrizacaoFiscalFigurasTributarias(self):
        try:
            self.__log.info("Importando Parametrização Fiscal de Figuras Tributárias")

            lista_figuras = '{}'
            count = 0
            figuratributaria = None

            ControladorParametrizacaoFiscalFigurasTributarias().excluirColunaTbFiguraId()

            ControladorParametrizacaoFiscalFigurasTributarias().addColunaTbFiguraId()

            ncms: List[FiguraTributariaDTO] = ControladorParametrizacaoFiscalFigurasTributarias().selecionarNCMs()
            for ncm in ncms:

                if ncm.id == None:
                    raise Exception("NCM {} não foi encontrado..".format(ncm.pl_ncm))
                else:
                    primeira = True

                    figuras_tributarias: List[FiguraTributariaDTO] = ControladorParametrizacaoFiscalFigurasTributarias().selecionarFigurasTributarias(ncm.ncm)
                    for figura_tributaria in figuras_tributarias:

                        figurastributariastemplates: List[FiguraTributariaTemplateDTO] = ControladorParametrizacaoFiscalFigurasTributarias().selecionarFigurasTributariasTemplates(figura_tributaria.tb_operacao_id, figura_tributaria.tb_perfil_est_id, figura_tributaria.tb_perfil_fed_id, primeira, lista_figuras)

                        lista_figuras = self.montarListaFigurasTributarias(figurastributariastemplates)

                        primeira = False

                    primeira = False

                    if len(figurastributariastemplates) >= 1:
                        figuratributaria = figurastributariastemplates[1].figuratributaria

                    if figuratributaria == None:

                        count = (count or 0) + 1

                        figuratributaria = ControladorParametrizacaoFiscalFigurasTributarias().inserirFiguraTributaria(count)

                        ControladorParametrizacaoFiscalFigurasTributarias().inserirFiguraTributariaTemplate(
                            figuratributaria,
                            ncm.ncm
                        )

                    ControladorParametrizacaoFiscalFigurasTributarias().inserirFiguraTributariaNCM(figuratributaria, ncm.ncm)

                    ControladorParametrizacaoFiscalFigurasTributarias().atualizarFiguraTributaria(figuratributaria, ncm.ncm)

            self.__log.info("Parametrização Fiscal de Figuras Tributárias importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal de Figuras Tributárias.")
            raise

    def importarParametrizacaoFiscalAtualizarProdutos(self):
        try:
            self.__log.info("Importando Parametrização Fiscal - Atualizar Produtos")

            ControladorParametrizacaoFiscalAtualizarProdutos().atualizarProdutos()

            self.__log.info("Parametrização Fiscal - Atualizar Produtos importada")

        except Exception as e:
            tb = traceback.format_exc()
            ModuloLog.erro(tb, e)
            ModuloLog.erro(f"Erro ao importar Parametrização Fiscal - Atualizar Produtos.")
            raise

    def montarListaFigurasTributarias(self, figurastributariastemplates) -> str:
        posicao = 0
        lista_figuras = '{}'
        for figurastributariastemplate in figurastributariastemplates:
            posicao += 1
            if posicao == 1:
                lista_figuras = '{'
            lista_figuras += figurastributariastemplate.figuratributaria
            if posicao != len(figurastributariastemplates):
                lista_figuras += ','
            else:
                lista_figuras += '}'
        return lista_figuras


if __name__ == '__main__':
    Importador().importar()