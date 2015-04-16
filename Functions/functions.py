__author__ = 'inamoto21'


def main():
    testfunc(1, 2, 3, 42, 43, 45, 46)


def testfunc(this, that, other, *args):  # arbitrary list of arguments
    print(this, that, other)
    for n in args:  # args are in tuple
        print(n, end=' ')

if __name__ == '__main__':
    main()