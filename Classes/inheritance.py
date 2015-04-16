__author__ = 'inamoto21'


class Animal:
    def talk(self): print('talk')
    def walk(self): print('walk')
    def clothes(self): print('clothes')


class Duck(Animal):
    def quack(self):  # it is a method of a class
        print("Quaaaaaack!")

    def walk(self):
        super().walk()
        print("Walks like a duck.")

class Dog(Animal):
    def clothes(self):
        print('fur')

def main():
    donald = Duck()
    donald.walk()
    jack = Dog()
    jack.clothes()
    jack.walk()

if __name__ == '__main__':
    main()
