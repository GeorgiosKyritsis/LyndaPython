__author__ = 'inamoto21'


class Duck:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def quack(self):  # it is a method of a class
        print("Quaaaaaack!")

    def walk(self):
        print("Walks like a duck.")

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    donald = Duck(feet=2)
    donald.set_variable('color', 'blue')
    print(donald.get_variable('feet'))
    print(donald.get_variable('color'))

if __name__ == '__main__':
    main()
