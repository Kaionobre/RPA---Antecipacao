from selenium import webdriver
from selenium.webdriver.common.by import By
from config.Configuracoes import Configuracoes
from scripts.navegacao import *
from datetime import datetime 
import time
import pandas as pd

config = Configuracoes()
browser = webdriver.Chrome()

ler_planilha = pd.read_excel(config.get_caminho_planilha(), config.get_pagina_planilha())

abrir_site(browser, 'https://sgc-pss.safewebpss.com.br/gerenciamentoac/#/pages/dashboard')
ir_para_protocolo(browser)

for linha in ler_planilha.itertuples():
    protocolo = linha.Protocolo
    pesquisar_protocolo(browser, protocolo)

    ler_planilha.at[linha.Index, 'Razão Social'] = copiar_razao_social(browser)
    ler_planilha.at[linha.Index, 'AGR'] = copiar_nome_agr(browser)

    limpar_filtro(browser)

nome_arquivo = f"Planilha Finalizada {datetime.now().strftime('%d-%m-%Y__%H-%M-%S')}.xlsx"
ler_planilha.to_excel(nome_arquivo, index=False)




