"""
ENCAPSULATION
"""


class Encapsulation:
    def public(self):
        print('You are here, everyone can see me')

    def _protected(self):
        print('Not everyone can see me')

    def __private(self):
        print('I am visible inside encapsulation class')

    def get_private_info(self):
        self.__private()


class Child(Encapsulation):
    def use_protected_method(self):
        self._protected()


my_encapsulation = Encapsulation()
my_encapsulation.public()
# my_encapsulation._protected()
# my_encapsulation.__private()
my_encapsulation.get_private_info()

child_cls = Child()
child_cls.use_protected_method()

