__author__ = 'inamoto21'


def main():
    print("This is a python file")
    for i in inclusive_range(1,10):
        print(i, end=' ')


def inclusive_range(*args):
    arglen = len(args)
    if arglen < 1: raise TypeError("requires at least one argument")
    elif arglen == 1:
        start = 0
        stop = args[0]
        step = 1
    elif arglen == 2:
        start, stop = args
        step = 1
    elif arglen == 3:
        start, stop, step = args
    else:
        raise TypeError('{} arguments are given'.format(arglen))

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == '__main__':
    main()