"""
SELECTORI
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")
time.sleep(2)
# nagivare catre un URL
driver.get("https://www.google.com/")

# maximizare fereastra
driver.maximize_window()

# selector by ID
driver.find_element(By.ID, 'L2AGLb').click()

# selector by NAME
search_field = driver.find_element(By.NAME, 'q')

# cautam cuvantul "harti"
search_field.send_keys("harti")
search_field.submit()
driver.quit()  # inchide conexiunea cu browserul complet


# ToDo - is visible - doar daca e vizibil sa dam click pe el
