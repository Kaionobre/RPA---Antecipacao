# 🤖 RPA - Antecipação de Protocolo

Automação em Python desenvolvida para a **Certsempre**, que otimiza o processo de antecipação de protocolos de certificados digitais.  

O robô recebe uma planilha com os **protocolos**, acessa o sistema **Gerenciamento**, consulta cada protocolo e retorna automaticamente a **Razão Social** do cliente e o nome do **AGR (Agente de Registro)** responsável pela emissão.  

No final, gera uma nova planilha pronta para ser enviada à supervisão.

---

## 📌 Contexto do Problema

Antes da automação, o processo era manual:
- Abrir o sistema de Gerenciamento
- Pesquisar protocolo por protocolo
- Copiar Razão Social
- Copiar nome do AGR
- Colar os dados na planilha
- Repetir até terminar

Na última vez que esse processo foi feito manualmente:
- **37 protocolos**  
- **10 minutos de execução**

Com o robô:
- **37 protocolos**  
- **1 minuto de execução**

⏱️ **Ganho de tempo:** 9 minutos economizados a cada 37 protocolos.  
📈 Projeção: em **370 protocolos**, o ganho seria de aproximadamente **1 hora e 30 minutos**.  

---

## ⚙️ Fluxo da Automação

1. Receber a planilha inicial com os protocolos  
2. Configurar caminho e nome da planilha no sistema (`Configuracoes.py`)  
3. Rodar o programa principal (`main.py`)  
4. O robô:
   - Abre o sistema Gerenciamento  
   - Pesquisa cada protocolo  
   - Copia **Razão Social**  
   - Copia **AGR**  
   - Atualiza a planilha  
5. O programa finaliza a planilha com os campos preenchidos  
6. Apenas enviar o arquivo gerado para a supervisão  
