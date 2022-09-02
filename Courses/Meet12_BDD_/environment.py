"""
Hooks.
"""
import time


def before_all(context):
    print('Pycharm is open')


def before_step(context):
    time.sleep(2)


def after_all(context):
    print('close the test environment')
