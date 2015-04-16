__author__ = 'inamoto21'


def main():
    testfunc(5, 6, 7, 8, 9, 10, one=1, two=2, three=3, four=42)  # named arguments, 8, 9, 10 will be in tuple, next there are keyword arguments!


def testfunc(this, that, other, *args, **kwargs):
    print('This is a test function',
          this, that, other,args,
          kwargs['one'], kwargs['two'], kwargs['four'])

    for k in kwargs:
        print(k, kwargs[k])
    for k in args:
        print(k)

if __name__ == '__main__':
    main()