from tkinter.tix import Select
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)


driver.get("https://www.ligamagic.com.br")

driver.implicitly_wait(3)

#campoBusca = driver.find_element(By.NAME,"card")
#campoBusca.send_keys("Joven")

botaoPropa = driver.find_element(By.ID, "campanha-del-1").click()

driver.implicitly_wait(3)

campoBusca = driver.find_element(By.NAME,"card")
campoBusca.send_keys("Joven")

botao1 = driver.find_elements(By.CLASS_NAME,"l-header-search-submit")[1].click()

driver.implicitly_wait(3)

NomeCarta = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[4]/div/div[3]/div/div[2]/div/div[1]/a").text
ValorCarta = driver.find_element(By.XPATH, "/html/body/main/div[2]/div[4]/div/div[3]/div/div[3]/div/div[5]").text



print(f'Carta: {NomeCarta} Valor: {ValorCarta}')


driver.close()