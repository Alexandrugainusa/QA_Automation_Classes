"""
LOGIN TEST
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# user ID = username
# pass ID = password
# button xpath = //*[@id="login"]/button/i
# selectorul este mai rapid decat XPATH

# user = driver.find_element(By.ID, 'username').send_keys('tomsmith')
# time.sleep(3)
# pst = driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
# time.sleep(1)
# button = driver.find_element(By.XPATH, '//*[@id="login"]/button/i')
# time.sleep(3)

#locatori
user = (By.ID, 'username')
password = (By.ID, 'password')
login = (By.XPATH, '//*[@id="login"]/button/i')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

print('test 1 invalid login')
driver.find_element(*user).send_keys('test@ana.ro')


# def select_user(user):
#     driver.find_element(*user).send_keys('test@ana.ro')
#
#
# select_user('test@ana.ro')

driver.find_element(*password).send_keys('123')
driver.find_element(*login).click()

#ToDo - de facut validare ca apare cu rosu - your user is invalid

print('test 2 succesful logon')
driver.find_element(*user).send_keys('tomsmith')
driver.find_element(*password).send_keys('SuperSecretPassword!')
driver.find_element(*login).click()

#ToDo - sa preluam mesajul cu verde si sa-l validam
#ToDo - testul ptr delogare
#ToDo - preluarea in mod dinamic username si parola - hint slicing din textul de documentatie