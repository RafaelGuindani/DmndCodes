import os
import time
import pyautogui as py
from datetime import datetime
from openpyxl import *

#Pegamos o caminho do arquivo no computador

file_name = "GoogleFinance - Base.xlsx"
workbook = load_workbook(file_name)

from selenium.webdriver.chrome.service import Service
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#Abre o navegador do Google Chrome e abre o site
service = Service(executable_path=ChromeDriverManager().install())
chrome = wd.Chrome(service=service)
chrome.get('https://www.google.com/finance/?hl=pt')
chrome.maximize_window()
time.sleep(0.1)

chrome.execute_script("window.history.go(-1)")
chrome.refresh()
time.sleep(0.1)

#Clica em Moedas
moedas = chrome.find_element(By.XPATH, '//*[@class="AHyjFe QwFhgb"]')
time.sleep(0.1)
moedas.click()
time.sleep(0.1)
py.click(859,255)

#coletar valor dolar
usd = chrome.find_element(By.XPATH, '(//*[@class="YMlKec"])[1]')
usd = usd.text
print(f'Dolar: R$ {usd}')
time.sleep(0.1)

#coletar valor euro
eur = chrome.find_element(By.XPATH, '(//*[@class="YMlKec"])[3]')
eur = eur.text
print(f'Euro: R$ {eur}')
time.sleep(0.1)

#colatar valor libra
gbp = chrome.find_element(By.XPATH, '(//*[@class="YMlKec"])[5]')
gbp = gbp.text
print(f'Libra esterlina: R$ {gbp}')
time.sleep(0.1)

#colatar valor Iene
jpy = chrome.find_element(By.XPATH, '(//*[@class="YMlKec"])[7]')
jpy = jpy.text
print(f'Iene: R$ {jpy}')
time.sleep(0.1)

#coletar valor Dólar australiano
aud = chrome.find_element(By.XPATH, '(//*[@class="YMlKec"])[9]')
aud = aud.text
print(f'Dólar australiano: R$ {aud}')
time.sleep(0.1)


#Selecionamos a sheet de Dados
select_sheet_base = workbook['Base']

#Pegamos a ultima linha preenchida na coluna a e acrescentamos + 1
line = len(select_sheet_base['A']) + 1
columna = 'A' + str(line)
time.sleep(0.3)
columnb = 'B' + str(line)
time.sleep(0.3)
columnc = 'C' + str(line)
time.sleep(0.3)
columnd = 'D' + str(line)
time.sleep(0.3)
columne = 'E' + str(line)
time.sleep(0.3)
columnf = 'F' + str(line)
time.sleep(0.1)

#Imprimimos as informacoes do site na planilha
select_sheet_base[columna] = usd
time.sleep(0.1)
select_sheet_base[columnb] = eur
time.sleep(0.1)
select_sheet_base[columnc] = gbp
time.sleep(0.1)
select_sheet_base[columnd] = jpy
time.sleep(0.1)
select_sheet_base[columne] = aud
time.sleep(0.1)
select_sheet_base[columnf] = datetime.now()
time.sleep(0.1)

#Salvamos o arquivo do Excel com as novas informações
workbook.save(filename=file_name)

#Abrimos o arquivo
os.startfile(file_name)
