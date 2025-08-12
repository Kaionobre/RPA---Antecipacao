

class Configuracoes:
    def __init__(self):
        self._caminho_planilha = 'C:\\Users\\kaion\\OneDrive\\Área de Trabalho\\teste antecipacao.xlsx'
        self._pagina_planilha = 'Planilha1'

    def get_caminho_planilha(self):
        return self._caminho_planilha
    
    def get_pagina_planilha(self):
        return self._pagina_planilha

