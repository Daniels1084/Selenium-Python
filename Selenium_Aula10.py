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
#minimiza
driver.minimize_window()

driver.implicitly_wait(3)
#maximiza
driver.maximize_window()

driver.implicitly_wait(3)

#volta a página
driver.implicitly_wait(3)
driver.back()

#avança a página
driver.implicitly_wait(3)
driver.forward()

#atualiza a página
driver.implicitly_wait(3)
driver.refresh()

#fecha a página
driver.implicitly_wait(3)
driver.close()