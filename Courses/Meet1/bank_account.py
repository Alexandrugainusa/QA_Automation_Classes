"""
get the user, password and current sold from console
validate the user and password
enable the login through an enter
display the sold after the login
retrieve an amount of cash
display the password encrypted e.g. instead of 'abcd' show '****'
be aware that the nr of '*' should be equal with the length of the password
- Pylint usage. Adjust the existing exercises to have a score equal to 10.
"""

EXPECTED_USER = 'Alex'
EXPECTED_PASS = 'abc'
EXPECTED_SOLD = 125

user = input('Enter a valid user ')
assert user == EXPECTED_USER
pwd = input('Enter a valid pass ')
assert pwd == EXPECTED_PASS

input('press enter to login ')
print("You're login")
try:
    sold = input('Enter a valid sold ')
    assert sold == EXPECTED_SOLD , 'ok'
except AssertionError as msg:
    print(msg)
print('Retrieve an amount of cash')
amount = int(input('How much do you want to retrieve: '))
print(f'Your Sold is now: {(EXPECTED_SOLD - amount)}')

pwd = input('Please enter again the pass: ')
for i in pwd:
    if i.replace(pwd, '*'):
        print('*', end='')
    else:
        print(i, end='')
