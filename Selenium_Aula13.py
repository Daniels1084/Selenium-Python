from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import urllib.request


opts = ChromeOptions()
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.ligamagic.com.br/")

driver.implicitly_wait(3)

botaoPropa = driver.find_element(By.ID, "campanha-del-1").click()

driver.implicitly_wait(3)

#divImagens = driver.find_element(By.CLASS_NAME,"hm-news-ad")
PrimeiraImagem = driver.find_element(By.TAG_NAME,"img")
atributoScr = PrimeiraImagem.get_attribute("src")

print("Linkão:", atributoScr)

try:
    urllib.request.urlretrieve(atributoScr,r"C:\Users\Daniel Lazarini\Desktop\Curso_python\teste.png")
    print("Imagem Baixada")

except:
    print("Ocrreu erro")

