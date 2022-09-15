from behave import *


@given('I have Behave installed')
def step_impl(context):
    print('First given')


@when('I type Behave on Console')
def step_impl(context):
    print('Second when')


@then('My first test should fail')
def step_impl(context):
    print('Third then')


@given(u'I have a Digi coonection')
def step_impl(context):
    print('Stable Internet')


@given(u'I have a valid username and password')
def step_impl(context):
    print('Print I have credentials')


@when(u'I login to website herokup')
def step_impl(context):
    print('On the website')


@then(u'I am able to connect my account')
def step_impl(context):
    print('On the account')
    assert 'Gicu' == 'Gica'


@given(u'User Popescu is valid')
def step_impl(context):
    print('i have credential')


@when(u'He is entering the password Abcd1234')
def step_impl(context):
    print('On the website')


@then(u'He is logged into the Netflix account')
def step_impl(context):
    print('On the account')


@given(u'User "{user_name}" is valid')
def step_impl(context, user_name):
    print(f'{user_name}')


@when(u'He is entering the password "{password_name}"')
def step_impl(context, password_name):
    print(f'{password_name}')
