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


driver.get("https://expert.brasil.adp.com/ipclogin/1/loginform.html?TYPE=33554433&REALMOID=06-000a1470-e058-1656-b22f-441e0bf0d04d&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-hUZSibC0c0PGmKIGA5zqdHLfTPXyq1YLIqk8DXbGAekgoWJJCq1%2btDRL41DxmZ4j&TARGET=-SM-https%3a%2f%2fexpert%2ebrasil%2eadp%2ecom%2fexpert%2f")

driver.implicitly_wait(3)

Usuario = driver.find_element(By.XPATH,"/html/body/div/div/section[1]/div/form/div[1]/input")

Usuario.send_keys("daniel.lazarini.1")

Senha = driver.find_element(By.XPATH,"/html/body/div/div/section[1]/div/form/div[2]/input[1]")

Senha.send_keys("Dan39365308@")

Login = driver.find_element(By.XPATH,"/html/body/div/div/section[1]/div/form/div[3]/div/button")

Login.click()

