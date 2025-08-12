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
    print(protocolo)
    pesquisar_protocolo(browser, protocolo)
    ler_planilha[linha.Index, 'Razão Social'] = copiar_razao_social(browser)
    #copiar_razao_social(browser)
    limpar_filtro(browser)

nome_arquivo = f"Planilha Finalizada {datetime.now().strftime('%d-%m-%Y__%H-%M-%S')}.xlsx"
lerPlanilha.to_excel(nome_arquivo, index=False)


