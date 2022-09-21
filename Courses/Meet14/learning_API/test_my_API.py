import requests

from Courses.Meet14.learning_API.learning_API_test_wrapper import call_get_method


def test_status_code_for_get_method():
    x = call_get_method()
    assert x[1] == 200


def test_content_is_dict():
    x = call_get_method()
    assert type(x[0]) is dict


def test_email_in_json():
    x = call_get_method()
    assert 'email' in x[0]["users"][0].keys()
