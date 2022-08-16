import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Courses.Meet11_POM.Pages.homepage import Homepage


class TestHomepage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://formy-project.herokuapp.com/')

    def test_1(self):
        home = Homepage(self.driver)

        home.click_on_checkbox()

    def tearDown(self) -> None:
        self.driver.quit()
