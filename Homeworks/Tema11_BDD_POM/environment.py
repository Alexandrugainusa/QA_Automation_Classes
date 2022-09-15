import time

from Homeworks.Tema11_BDD_POM.Pages.home_page import Homepage
from Homeworks.Tema11_BDD_POM.Pages.login_page import LoginPage
from Homeworks.Tema11_BDD_POM.Pages.secure_page import SecurePage


def before_all(context):
    context.home_page = Homepage()
    context.login_page = LoginPage()
    context.secure_page = SecurePage()


def before_step(context):
    time.sleep(2)


def after_all(context):
    context.base_page.close()
