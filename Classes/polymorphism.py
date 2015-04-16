__author__ = 'inamoto21'


class Duck():
    def quack(self):  # it is a method of a class
        print("Quaaaaaack!")

    def walk(self):
        print("Walks like a duck.")

    def bark(self):
        print('The duck cannot bark')

    def fur(self):
        print('The duck has feathers')

class Dog():
    def bark(self):
        print('Woof')

    def fur(self):
        print("The dog has white and brown fur")

    def quack(self):
        print('The dog cannot quack')

    def walk(self):
        print('walks like a dog')

def main():
    donald = Duck()
    jack = Dog()

    for o in (donald, jack):
        o.quack()
        o.fur()
        o.walk()
        o.bark()

    in_the_forest(donald)
    in_the_pond(jack)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()


if __name__ == '__main__':
    main()
