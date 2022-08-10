"""
CONTEXT MENU
"""
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestContextMenu(unittest.TestCase):
    CONTEXT_MENU = (By.CSS_SELECTOR, '#hot-spot')
    RIGHT_CLICK = (By.ID, 'hot-spot')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/context_menu')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_context_menu(self):
        self.driver.find_element(*self.CONTEXT_MENU).click()
        action = ActionChains(self.driver)  # ii trimitem driverul nostru de chrome
        action.context_click(self.driver.find_element(*self.RIGHT_CLICK)).perform()
        self.driver.switch_to.alert.accept()  # accepta Alerta
        time.sleep(3)
