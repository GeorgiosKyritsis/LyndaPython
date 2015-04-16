__author__ = 'inamoto21'


class Duck:
    def quack(self):  # it is a method of a class
        print("Quaaaaaack!")

    def walk(self):
        print("Walks like a duck.")


def main():
    donald = Duck()
    donald.quack()  # attribute dereference operator
    donald.walk()


if __name__ == '__main__':
    main()
