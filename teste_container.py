from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

command_executor='http://127.0.0.1:4444/wd/hub'
desired_capabilities=DesiredCapabilities.CHROME

browser = webdriver.Remote(command_executor, desired_capabilities)

# Busca o site do google.
browser.get("http://www.google.com")

# Salva uma imagem da página buscada.
browser.save_screenshot("google.png")