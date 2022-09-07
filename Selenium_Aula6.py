from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.by import By
#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://statusinvest.com.br/")

driver.implicitly_wait(3)

dados1 = driver.find_element(By.CLASS_NAME,"mark").text

print(dados1)




