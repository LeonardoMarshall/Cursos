from selenium import webdriver
from selenium.webdriver.common.keys import Keys



navegador = webdriver.Chrome("chromedriver.exe")
navegador.get("https://www.google.com/webhp?hl=pt-BR&sa=X&sqi=2&pjf=1&ved=0ahUKEwiFrbGUxcDzAhX2rpUCHStmAmoQPAgI")
navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("Cotação do Dolar")
navegador.find_element_by_xpath(
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element_by_xpath(
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

print(cotacao_dolar)