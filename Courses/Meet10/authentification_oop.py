"""
Authentification OOP
"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestAuth(unittest.TestCase):
    PROMPT_MENU = (By.CSS_SELECTOR, '#content > ul > li:nth-child(3) > a')
    VALID_USER = 'admin'
    INVALID_USER = 'ananas'
    VALID_PASS = 'admin'
    INVALID_PASS = 'anana123'

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_invalid_credential(self):
        self.driver.find_element(*self.PROMPT_MENU).click()
        self.driver.get(
            'https://' + self.INVALID_USER + ':' + self.INVALID_PASS + '@the-internet.herokuapp.com/basic_auth')

    def test_valid_credential(self):
        self.driver.find_element(*self.PROMPT_MENU).click()
        self.driver.get(
            'https://' + self.VALID_USER + ':' + self.VALID_PASS + '@the-internet.herokuapp.com/basic_auth')
