from selenium.webdriver.common.by import By

from Courses.Meet11_POM.Pages.base import BasePage


class Form(BasePage):
    FIRSTNAME = (By.ID, 'first-name')
    LASTNAME = (By.ID, '#last-name')
    JOBTITLE = (By.ID, 'job-title')
    SUBMIT = (By.CSS_SELECTOR, 'body > div > form > div > div:nth-child(15) > a')

    # ToDo- de extras restul locatorilor

    def enter_firstname(self,name):
        self.driver.find_element(*Form.FIRSTNAME).send_keys(name)

    def enter_lastname(self,lastname):
        self.driver.find_element(*Form.LASTNAME).send_keys(lastname)

    def enter_jobtitle(self):
        self.driver.find_element(*Form.JOBTITLE).click()

    def click_on_submit(self):
        self.driver.find_element(*Form.SUBMIT).click()