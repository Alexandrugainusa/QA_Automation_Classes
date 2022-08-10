"""
MULTI TABS TEST
"""

import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestMultiTabs(unittest.TestCase):
    MULTI_TAB = (By.CSS_SELECTOR, '#content > div > a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_back(self):
        self.driver.back()

    def test_forward(self):
        self.driver.forward()

    # def test_context_menu(self):
    #     self.driver.find_element(*self.CONTEXT_MENU).click()
    #     action = ActionChains(self.driver) # ii trimitem driverul nostru de chrome
    #     action.context_click(self.driver.find_element(*self.RIGHT_CLICK)).perform()
    #     self.driver.switch_to.alert.accept() # accepta Alerta
    #     time.sleep(3)

    def test_multi_tabs(self):
        self.driver.get('https://the-internet.herokuapp.com/windows')
        self.driver.find_element(*self.MULTI_TAB).click()
        tab1 = self.driver.window_handles[0]
        tab2 = self.driver.window_handles[1]
        # STRESS TEST: PUTEM SA RULAM DE 1000 DE ORI
        e = 0
        while e < 15:
            self.driver.switch_to.window(tab2)
            time.sleep(3)
            self.driver.switch_to.window(tab1)
            time.sleep(3)
            e += 1
