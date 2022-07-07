"""
Nested function
"""


def nest_function(msg):
    print('I am here')

    def another_nest_function():
        print('Start test case execution')
        print(f'Checking for test {msg}')

        def another2_nest_function():
            print('Test case completed')

        another2_nest_function()

    another_nest_function()


nest_function('Login Page')
