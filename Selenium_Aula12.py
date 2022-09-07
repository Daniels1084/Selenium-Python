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


botaoPropa = driver.find_element(By.ID, "campanha-del-1").click()

Lista = Select(driver.find_element(By.NAME, "tipo"))

Lista.select_by_value(2)

driver.implicitly_wait(3)



