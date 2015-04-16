__author__ = 'inamoto21'


class Duck:
    def __init__(self, value):  # the purpose is to initialize some data
        self._v = value
        print('constructor')

    def quack(self):  # it is a method of a class
        print("Quaaaaaack!", self._v)

    def walk(self):
        print("Walks like a duck.", self._v)


def main():
    donald = Duck(47)
    donald.quack()  # attribute dereference operator
    donald.walk()


if __name__ == '__main__':
    main()
