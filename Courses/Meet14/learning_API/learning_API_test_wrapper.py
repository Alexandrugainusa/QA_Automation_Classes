import requests
import json


def call_get_method():
    print('GET METHOD STARTED')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "name": "Alex",
        "email": "alex@bcr.ro"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json(), response.status_code


def call_post_method(name, email, salary):
    print('POST METHOD STARTED')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "name": name,
        "email": email,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)

    return response.status_code


def call_delete_method(name, email, salary):
    print('DELETE METHOD STARTED')
    url = "http://localhost:5000/users"

    payload = json.dumps({
        "name": name,
        "email": email,
        "salary": salary
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)


b = call_post_method('Ilie', 'Ilie@nemuritoru.ro', 35000)
print(b)

a = call_get_method()
print(a[0])
print(a[1])

c = call_delete_method('Ilie', 'Ilie@nemuritoru.ro', 35000)
print(c)
