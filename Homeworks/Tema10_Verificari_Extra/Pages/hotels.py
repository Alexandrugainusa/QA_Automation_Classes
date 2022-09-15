import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Homeworks.Tema10_Verificari_Extra.Pages.baze import BazePage


class Hotels(BazePage):
    HOTELS_BTN = (By.XPATH, '//*[@id="fadein"]/header/div/div/div/div/div/div[2]/div/div[1]/nav/ul/li[1]/a')
    CITY_NAME = (By.ID, "select2-hotels_city-container")
    CHECKIN = (By.ID, "checkin")
    CHECKOUT = (By.ID, "checkout")
    TRAVELLERS_DROPDOWN = (By.XPATH, '//*[@id="hotels-search"]/div/div/div[3]/div/div/div/a/p')
    ROOMS = (By.CSS_SELECTOR,
             '#hotels-search > div > div > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div > label')
    ADULTS = (By.CSS_SELECTOR,
              '#hotels-search > div > div > div:nth-child(3) > div > div > div > div > div:nth-child(2) > div > label')
    CHILDS = (By.CSS_SELECTOR,
              '#hotels-search > div > div > div:nth-child(3) > div > div > div > div > div:nth-child(3) > div > label')
    SEARCH_BTN = (By.XPATH, '//*[@id="submit"]/span[1]')

    def search_by_city(self, city):
        self.driver.find_element(*Hotels.CITY_NAME).send_keys(city)

    def enter_checkin(self, checkin):
        self.driver.find_element(*Hotels.CHECKIN).send_keys(checkin)

    def enter_checkout(self, checkout):
        self.driver.find_element(*Hotels.CHECKOUT).send_keys(checkout)

    def enter_travellers_dropdown(self, rooms, adults, childs):
        self.driver.find_element(*Hotels.TRAVELLERS_DROPDOWN).click()
        self.driver.find_element(*Hotels.ROOMS).send_keys(rooms, adults, childs)

    def search_btn(self):
        self.driver.find_element(*Hotels.SEARCH_BTN).click()
