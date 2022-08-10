"""
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
"""

import unittest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    # se pun elementele in pagina
    LOGIN_LABEL = (By.XPATH, '//h2')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button/i')
    ELEMENTAL_LINK = (By.XPATH, '//a[@href = "http://elementalselenium.com/"]')
    LOGIN_ERROR = (By.XPATH, '//div[@class="flash error"]')
    X_BUTTON = (By.XPATH, '//a[@class="close"]')

    # se ruleaza inainte de fiecare test
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//a[text() = "Form Authentication"]').click()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.driver.quit()

    # verifica daca noul URL este corect
    def test1_url(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    # verificam page title (head)
    def test2_page_title(self):
        actual = self.driver.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page Title is incorrect')

    # verificam textul de pe elementul xpath = //h2
    def test3_label(self):
        actual = self.driver.find_element(*self.LOGIN_LABEL).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Text Label is incorrect')

    # verificam daca butonul de Login este displayed
    def test4_button_login(self):
        login = self.driver.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(login.is_displayed(), 'Login button is not displayed')

    # Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
    def test5_atribut_link(self):
        actual = self.driver.find_element(*self.ELEMENTAL_LINK).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, "Elemental Selenium doesn't have href link atribute")
        # self.assertEqual(actual, expected, "Elemental Selenium doesn't have href link atribute")

    """
● Test 6
- Lasă goale user și pass
- Click login
- Verifică dacă eroarea e displayed
    """

    def test6_error_displayed(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        error = self.driver.find_element(*self.LOGIN_ERROR)
        self.assertTrue(error.is_displayed(), f"The {error} it's not displayed")

    """
● Test 7
- Completează cu user și pass invalide
- Click login
- Verifică dacă mesajul de pe eroare e corect
- Este și un x pus acolo extra așa că vom folosi soluția de mai jos
expected = 'Your username is invalid!'
self.assertTrue(expected in actual, 'Error message text is
incorrect')
    """

    def test7_error_displayed2(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('Nume')
        self.driver.find_element(*self.PASS_INPUT).send_keys('Parola')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        actual = self.driver.find_element(*self.LOGIN_ERROR).text
        print(actual)
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    """
● Test 8
- Lasă goale user și pass
- Click login
- Apasă x la eroare
- Verifică dacă eroarea a dispărut
"""

    def test8_error_not_displayed(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        self.driver.find_element(*self.X_BUTTON).click()
        time.sleep(3)
        # expected = None
        # self.assertEqual(expected, actual, 'The error message is still displayed')
        try:
            self.driver.find_element(*self.LOGIN_ERROR)
            raise Exception("The error message is still displayed!")
        except NoSuchElementException:
            pass

    """
 ● Test 9
- Ia ca o listă toate //label
- Verifică textul ca textul de pe ele să fie cel așteptat (Username și
Password)
- Aici e ok să avem 2 asserturi
"""

    def test9_label_text(self):
        lista_label = self.driver.find_elements(By.XPATH, '//label')
        actual = (lista_label)[0].text
        expected = 'Username'
        self.assertEqual(actual, expected, "Username label text it's correct")
        actual2 = (lista_label)[1].text
        expected2 = 'Password'
        self.assertEqual(actual2, expected2, "Password label text it's correct")

    """
● Test 10
- Completează cu user și pass valide
- Click login
- Verifică ca noul url CONTINE /secure
- Folosește un explicit wait pentru elementul cu clasa ’flash succes’
- Verifică dacă elementul cu clasa=’flash succes’ este displayed
- Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
"""

    def test10_login(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.driver.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        # verifica ca noul url contine -> secure
        actual = self.driver.current_url
        expected = 'secure'
        self.assertTrue(expected in actual, "The link doesn't contains secure")
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="flash"]')))
        except TimeoutException:
            self.assertTrue(False,
                            "I've been waiting for 5 seconds but I haven't found the element with 'flash success' class")
        # Verifica ca elementul cu clasa=’flash succes’ este displayed
        element_class = self.driver.find_element(By.XPATH, '//*[@class="flash success"]')
        self.assertTrue(element_class.is_displayed(), "Green element not displayed")
        # Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!
        actual2 = element_class.text
        expected2 = 'secure area'
        self.assertTrue(expected2 in actual2, 'The text of the green element does NOT contain secure area')

    """
    ● Test 11
- Completează cu user și pass valide
- Click login
- Click logout
- Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    """

    def test11_login_logout(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        self.driver.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected, actual, "You're not in the right place")
