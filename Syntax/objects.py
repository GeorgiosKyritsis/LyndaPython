__author__ = 'inamoto21'


class Egg:
    def __init__(self, kind="fried"):
        self._kind = kind

    def whatKind(self):
        return self._kind


def main():
    fried = Egg()
    scrambled = Egg("scrambled")
    print(fried.whatKind())
    print(scrambled.whatKind())

if __name__ == '__main__':
    main()