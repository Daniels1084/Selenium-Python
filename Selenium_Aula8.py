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


driver.get("https://www.ligamagic.com.br/")

driver.implicitly_wait(3)

campoBusca = driver.find_element(By.NAME,"card")
campoBusca.send_keys("Teste")

#campoBusca2 = driver.find_element(By.NAME,"filtro_nome_deck")
#campoBusca2.send_keys("Deck mto pika")
