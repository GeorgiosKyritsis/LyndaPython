__author__ = 'inamoto21'


def b(n): print('{:08b}'.format(n))

def main():
    b(5)
    x, y = 0x55, 0xaa
    b(x)
    b(y)
    b(x | y)  # or
    b(x & y)  # and
    b(x ^ y)  # exclusive or
    b(x << 4)  # shift left by 4 bits
    b(x >> 4)  # shift right by 4 bits
    b(~ x)  # complement


if __name__ == '__main__':
    main()