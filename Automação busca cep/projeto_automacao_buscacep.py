import pyautogui as py
import time
import os
from openpyxl import load_workbook

#Pegamos o caminho do arquivo no computador
file_name = "PesquisaEndereco.xlsx"
workbook = load_workbook(file_name)

#Selecionamos a sheet de Dados
select_column_cep = workbook['CEP']

from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By as by
from webdriver_manager.chrome import ChromeDriverManager

#Abre o navegador do Google Chrome e abre o site
service = Service(executable_path=ChromeDriverManager().install())
chrome = wd.Chrome(service=service)
chrome.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
chrome.maximize_window()
time.sleep(0.1)

for i in range(2, len(select_column_cep['A']) + 1):

    # Imprime o CEP no campo do CEP
    pesquisa = select_column_cep['A%s' % i].value
    cepesquisa = chrome.find_element(by.NAME, "endereco")
    time.sleep(0.3)
    assert isinstance(pesquisa, object)
    cepesquisa.send_keys(pesquisa)
    time.sleep(0.1)

    #Clica no botão de Pesquisar
    csearch = chrome.find_element(by.NAME, "btn_pesquisar")
    time.sleep(0.3)
    csearch.click()
    py.click(525, 658)
    time.sleep(0.1)

    #Pega os dados da Rua no site
    street = chrome.find_element(by.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')
    time.sleep(0.3)
    street = street.text
    print("Rua: ", street)
    time.sleep(0.1)

    #Pega os dados do bairro no site
    time.sleep(0.3)
    district = chrome.find_element(by.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')
    time.sleep(0.3)
    district = district.text
    print("Bairro: ", district)
    time.sleep(0.1)

    #Pega os dados da Cidade no site
    time.sleep(0.3)
    city = chrome.find_element(by.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')
    time.sleep(0.3)
    city = city.text
    print("Cidade: ", city)
    time.sleep(0.1)

    #Pega os dados do CEP no site
    time.sleep(0.3)
    zipcode = chrome.find_element(by.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')
    time.sleep(0.3)
    zipcode = zipcode.text
    print("CEP: ", zipcode)
    time.sleep(0.1)

    #Selecionamos a sheet de Dados
    select_column_dados = workbook['Dados']
    time.sleep(0.3)

    #Clica no botão de voltar
    csearch = chrome.find_element(by.NAME, "btn_voltar")
    time.sleep(0.3)
    csearch.click()
    py.click(525, 658)
    time.sleep(0.1)

    #Pegamos a ultima linha preenchida na coluna a e acrescentamos + 1
    line = len(select_column_dados['A']) + 1
    columna = 'A' + str(line)
    time.sleep(0.3)
    columnb = 'B' + str(line)
    time.sleep(0.3)
    columnc = 'C' + str(line)
    time.sleep(0.3)
    columnd = 'D' + str(line)
    time.sleep(0.1)

    #Imprimimos as informacoes do site na planilha
    select_column_dados[columna] = street
    time.sleep(0.3)
    select_column_dados[columnb] = district
    time.sleep(0.3)
    select_column_dados[columnc] = city
    time.sleep(0.3)
    select_column_dados[columnd] = zipcode
    time.sleep(0.1)

#Salvamos o arquivo do Excel com as novas informações
workbook.save(filename=file_name)

#Abrimos o arquivo
os.startfile(file_name)
