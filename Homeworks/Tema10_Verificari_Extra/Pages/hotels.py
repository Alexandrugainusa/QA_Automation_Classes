import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Homeworks.Tema10_Verificari_Extra.Pages.baze import BazePage


class Hotels(BazePage):
    CITY_NAME = (By.ID, "select2-hotels_city-container")
    CHECKIN = (By.ID, "checkin")
    CHECKOUT = (By.ID, "checkout")
    TRAVELLERS_DROPDOWN = (By.XPATH, '//*[@id="hotels-search"]/div/div/div[3]/div/div/div/a/p')
    SEARCH_BTN = (By.XPATH, '//*[@id="submit"]/span[1]')

    def search_by_city(self,city):
        self.driver.find_element(*Hotels.CITY_NAME).send_keys(city)

