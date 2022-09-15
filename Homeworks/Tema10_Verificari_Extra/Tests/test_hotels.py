import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Homeworks.Tema10_Verificari_Extra.Pages.hotels import Hotels


class TestHotels(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://phptravels.net/')

    def test_1(self):
        hotel = Hotels(self.driver)
        hotel.search_by_city('Amsterdam')
        time.sleep(2)
        hotel.enter_checkin('10-09-2022')
        time.sleep(2)
        hotel.enter_checkout('11-09-2022')
        time.sleep(2)
        hotel.enter_travellers_dropdown('1', '2', '0')
        time.sleep(2)
        hotel.search_btn()

    def tearDown(self) -> None:
        self.driver.quit()