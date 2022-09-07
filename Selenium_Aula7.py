from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)


driver.get("https://statusinvest.com.br/acoes/itub4")

driver.implicitly_wait(3)

dados1 = driver.find_element(By.TAG_NAME,"table").text
dados2 = driver.find_elements(By.TAG_NAME,"table")[1].text
dados3 = driver.find_elements(By.TAG_NAME,"table")[2].text

print("Dados1 ELEMENT:", dados1,"\n")
print("Dados2 ELEMENTs:", dados2,"\n")
print("Dados3 ELEMENTs:", dados3,"\n")