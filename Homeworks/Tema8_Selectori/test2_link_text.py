"""
Selector By LINK TEXT and PARTIAL_LINK_TEXT
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")

# nagivare catre un URL
driver.get('https://formy-project.herokuapp.com')

# maximizare fereastra
driver.maximize_window()
time.sleep(1)

# Buttons -> back -> Checkbox -> bifeaza checkbox 1 -> dropdown menu catre Enabled and Disabled Elements -> exit
driver.find_element(By.LINK_TEXT, "Buttons").click()
time.sleep(3)
# goes back one step in history
driver.back()
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Checkbox").click()
time.sleep(2)
driver.find_element(By.ID, "checkbox-1").click()
time.sleep(2)
driver.find_element(By.ID, "navbarDropdownMenuLink").click()
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "Enabled").click()
time.sleep(3)

driver.quit()
