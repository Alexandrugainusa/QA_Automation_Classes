"""
Meet 10 authentification
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

username = 'admin'
password = 'admin'

driver.find_element(By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a').click()
# tOdO - SINTAXA PENTRU AUTENTIFICARE PE PAGINA !!!
driver.get('https://' + username + ':' + password + '@the-internet.herokuapp.com/basic_auth')
driver.save_screenshot('basic_auth.png')  # face print screeen la ecran!!!
print(datetime.now())

# ToDo - sa concatenam si ora curenta si ziua la numele imaginii, folosim modulul time (date time)
