"""
Tema8 - Selector By ID
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")

# nagivare catre un URL
driver.get('https://formy-project.herokuapp.com/form')

# maximizare fereastra
driver.maximize_window()

# selectam dupa ID
first_name = driver.find_element(By.ID, "first-name").send_keys("Alex")
time.sleep(2)

last_name = driver.find_element(By.ID, "last-name").send_keys("37")
time.sleep(2)

date_formy = driver.find_element(By.ID, 'datepicker').send_keys("01/23/1999")
time.sleep(3)

driver.quit()
