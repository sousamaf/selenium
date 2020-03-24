# Utilização do Selenium com Docker

Permite a raspagem de dados sem a abertura de navegador em ambiente gráfico.

## Para baixar o container:
docker pull selenium/standalone-chrome

## Para executar o container em modo debug:
docker run -d -p 4444:4444 --net "host" -v /dev/shm:/dev/shm selenium/standalone-chrome-debug:lastest

## Para executar o container:
docker run -d -p 4444:4444 --net "host" -v /dev/shm:/dev/shm selenium/standalone-chrome-debug:lastest

## Exemplo de código python para uso do container:
~~~~
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
~~~~
