"""
FORMY - SELECTORI
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")

driver.get('https://formy-project.herokuapp.com/form')

driver.maximize_window()

driver.find_element(By.ID, "first-name").send_keys('Alexandru')
time.sleep(2)

driver.find_element(By.ID, "last-name").send_keys('Catalin')
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="logo"]').click()
time.sleep(2)

driver.find_element(By.LINK_TEXT, 'Autocomplete').click()

driver.quit()

#ToDo - de completat pagina cu teste - Formy Project - Autocomplete , Buttons etc.