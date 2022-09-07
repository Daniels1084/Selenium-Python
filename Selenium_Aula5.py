from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)


driver.get("https://www.infomoney.com.br/")

#Delay de 3 segundos, pois pode ser que a aplicação tente pegar os dados da página e ela não carregou, retonará erro.
driver.implicitly_wait(3) #seconds

#Pega o sommente por 1 unidade de elemento
dados1 = driver.find_element(By.ID,"high").text

#Pega por posição na lista de elementos
dados1 = driver.find_elements(By.ID,"high")[0].text
print(dados1)