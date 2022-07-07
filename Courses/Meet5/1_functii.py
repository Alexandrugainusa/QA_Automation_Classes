"""
Curs5 - Functii
"""

print('Hellow World')
print('Hello World', 'Hello Romania')
print('Hello World', 'Hello Romania', sep=' *** ')  # separator


# print('Hello World', 'Hello Romania', end=' -> ')
# print('Hello World', 'Hello Romania', end='')


def custom_print(user):
    """
    Custom example
    :param user:
    :return:
    """
    print(f'Hi {user}')


custom_print('Alex')
custom_print('Bijuu')


def improved_custom_print(value: int):
    """
    Custom
    :param value:
    :return:
    """
    print(f'Given number is {value}')


improved_custom_print(5)
improved_custom_print(10)
print(improved_custom_print.__doc__) # documentam
