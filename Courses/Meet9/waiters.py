"""
WAIT-ERS IN SELENIUM
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://formy-project.herokuapp.com/form')
driver.maximize_window()
# time.sleep(3)
driver.implicitly_wait(3)

first_name = driver.find_element(By.ID, 'first-name').send_keys('Alex')
time.sleep(3)

# submit_button = driver.find_element(By.XPATH, '/html/body/div/form/div/div[8]/a').click()
submit_button = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.XPATH, '/html/body/div/form/div/div[8]/a')))
submit_button.click()
# ToDo - anumite butoane care se incarca mai greu in unele site uri - implicit and explicit wait
