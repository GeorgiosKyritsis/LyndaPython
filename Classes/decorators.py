__author__ = 'inamoto21'


class Duck():
    def __init__(self, **kwargs):
        self.properties = kwargs

    def quack(self):  # it is a method of a class
        print("Quaaaaaack!")

    def walk(self):
        super().walk()
        print("Walks like a duck.")

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']


def main():
    donald = Duck()
    donald.color = 'blue'
    print(donald.color)

if __name__ == '__main__':
    main()
