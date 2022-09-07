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

PrimeiroDado = driver.find_element(By.XPATH,"/html/body/main[2]/div/div[1]/div[1]/section/div[2]/div/div/ul/li[8]/div[3]/div/ul/li[1]").text


driver.get("https://www.ligamagic.com.br/?view=cards%2Fcard&card=Joven&tipo=1")


SegundoDado = driver.find_element(By.XPATH,"/html/body/main/div[4]/div[1]/div/div[4]/div[5]/div[2]/div/div[6]").text


print(PrimeiroDado)

print("Joven preço:", SegundoDado)