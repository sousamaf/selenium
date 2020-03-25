from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup

command_executor='http://127.0.0.1:4444/wd/hub'
desired_capabilities=DesiredCapabilities.CHROME

browser = webdriver.Remote(command_executor, desired_capabilities)

browser.get("https://www.unitins.br/nPortal/portal/noticias/todas")

dados = browser.find_element_by_class_name("page-content")
html = dados.get_attribute("innerHTML")
soup = BeautifulSoup(html, "html.parser")

## Tratar para capturar apenas link e título.
print(soup)