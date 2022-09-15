from behave import *


@given('home_page: I am on the https://the-internet.herokuapp.com/ page')
def step_impl(context):
    context.home_page.navigate_to_web_page()


@when('home_page: I click on the Form Authentication link')
def step_impl(context):
    context.home_page.click_form_auth()


@when(u'login_page: I fill tomsmith in the username field')
def step_impl(context):
    context.login_page.fill_username('tomsmith')


@when(u'login_page: I fill SuperSecretPassword! in the password field')
def step_impl(context):
    context.login_page.fill_password('SuperSecretPassword!')


@when(u'login_page: I click on the Login button')
def step_impl(context):
    context.login_page.click_login()


@when(u'secure_page: I see the login succes message')
def step_impl(context):
    context.secure_page.see_message_succes_banner()


@when(u'secure_page: I click on the Logout button')
def step_impl(context):
    context.secure_page.click_logout()


@then(u'secure_page: I verify that I am on the login_page')
def step_impl(context):
    context.secure_page.navigate_to_login_page()
