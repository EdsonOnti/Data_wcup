from selenium import webdriver
from selenium.webdriver.chrome.service import Service





path='C:\\Users\\2D\\Documents\\chromedriver'
service=Service(executable_path=path)
driver=webdriver.Chrome(service=service)

web='https://es.wikipedia.org/wiki/Copa_Am%C3%A9rica_2021'
options = webdriver.ChromeOptions()
#


try:
    driver.get(web)
    input('Presiona cualquier tecla para cerrar el navegador...')
    driver.quit()
    
except Exception as e:
    print(e)



