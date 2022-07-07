"""
Mini framework de testare
- conectare
- video si audio
- share screen
- chat
-use of call function
- people list
"""


def connect(user, pdw):
    print(f' {user} {pdw} you are succesfully connected')


# ToDo - sa ne gandim cum ar fi logic incat sa ne conectam pe bune
# -> un if daca user si parola sunt OK

def video_audio(microphone='ON', video='ON'):  # by default sunt deschise
    if microphone == 'ON':
        print('The other collegues can hear me')
    print("Microphone is OFF")
    if video == "ON":
        print('The others can see me')
    print('Camera is OFF')


def share_screen(button_share):
    if button_share == 'Clicked':
        print('I have the option to select a window or any other tool')
    elif button_share == 'Hover':
        print('An user is presenting')
    else:
        print('The other functionalities')  # ToDo - homework


# ToDo - the other functions, not print, but with a logic from a real app

# ToDo - test cases to be implemented in another module

def test_case_connect():
    connect('Alex', '1234')
    print('Successful connection')


def test_case_invalid_connect():
    connect('Alex', '123')
    print('Wrong passsword')


# ToDo - pt fiecare feature sa ne gandim la cat mai multe teste (user invalid, pass invalid,etc)

test_case_connect()
test_case_invalid_connect()
