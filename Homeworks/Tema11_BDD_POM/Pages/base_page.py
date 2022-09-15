import unittest


class BasePage(unittest.TestCase):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

