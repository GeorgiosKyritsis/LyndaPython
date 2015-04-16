__author__ = 'inamoto21'


def main():
    x = (1, 2, 3)  # tuple, immutable object
    print(type(x), x)
    y = [1, 2, 3]  # list, mutable object
    y.append(5)
    y.insert(2, 7)
    print(type(y), y)
    z = 'string'
    print(type(z), z[2:4])

    for i in z:
        print(i)

if __name__ == '__main__':
    main()
