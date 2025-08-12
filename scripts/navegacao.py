


from selenium import webdriver
from selenium.webdriver.common.by import By
from config.Configuracoes import Configuracoes
import time
import pandas as pd

config = Configuracoes()
def abrir_site(browser, url:str):
    while True:
        try:
            browser.get(url)
            break
        except:
            continue
    
def ir_para_protocolo(browser):
    while True:
        try:
            relatorios = browser.find_element(By.CSS_SELECTOR, '#link6').click()
            time.sleep(2)
            relatorio_emissao = browser.find_element(By.CSS_SELECTOR, '#link9').click()
            break
        except:
            continue


def pesquisar_protocolo(browser, protocolo):
    while True:
        try:
            input_protocolo = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.card.border-0.box-shadow > div.card-body.widget-body > pages-filter > div > div:nth-child(4) > div:nth-child(1) > input').send_keys(protocolo)
            button_pesquisar = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.card.border-0.box-shadow > div.card-body.widget-body > pages-filter > div > div:nth-child(9) > div > div > div > button.btn.btn-outline-primary.w-110p.mb-1.mr-1').click() 
            break
        except:
            continue

def copiar_razao_social(browser):
    while True:
        try:
            razao_social = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.table-responsive.table-light.table-striped.table-bordered.table-sm.ng-star-inserted > table > tbody > tr > td:nth-child(4)').text
            return str(razao_social)
        except:
            continue

def copiar_nome_agr(browser):
    while True:
        try:
            
            nome_agr = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.table-responsive.table-light.table-striped.table-bordered.table-sm.ng-star-inserted > table > tbody > tr > td:nth-child(10)').text
            return str(nome_agr)
        except:
            continue

def limpar_filtro(browser):
    while True:
        try:
            filtro = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.card.border-0.box-shadow > div.card-body.widget-body > pages-filter > div > div:nth-child(9) > div > div > div > button.btn.btn-outline-gray.w-110p.mb-1.mr-1').click()
            break
        except:
            continue

def elemento_nao_encontrado(browser):
    sem_elemento = browser.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > app-pages > div.wrapper-inner > div > div > app-relatorio-emissao-lista > form > div > div > div.col-md-12.ng-star-inserted').text
    return str(sem_elemento)