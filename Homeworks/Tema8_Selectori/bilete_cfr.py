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
search_field.send_keys("mersul trenurilor")
search_field.submit()

driver.find_element(By.CSS_SELECTOR, ".tF2Cxc > .yuRUbf .LC20lb").click()

driver.find_element(By.ID, "input-date-departure").click()
driver.find_element(By.LINK_TEXT, "3").click()


driver.find_element(By.ID, "input-station-departure-name").send_keys("Bucuresti Nord")

driver.find_element(By.ID, "input-station-arrival-name").send_keys("Busteni")

driver.find_element(By.XPATH, '//*[@id="form-search"]/button').click()

