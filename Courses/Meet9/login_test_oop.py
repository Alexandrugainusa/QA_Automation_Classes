"""

"""
import unittest

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):
    user = (By.ID, 'username')
    password = (By.ID, 'password')
    login = (By.XPATH, '//*[@id="login"]/button/i')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_invalid_login(self):
        self.driver.find_element(*self.user).send_keys('test')
        self.driver.find_element(*self.password).send_keys('abc123')
        time.sleep(3)
        self.driver.find_element(*self.login).click()

#ToDo - sa validam si testul corect

    def test_valid_login(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.login).click()