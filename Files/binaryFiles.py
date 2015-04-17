__author__ = 'inamoto21'


def main():
    buffer_size = 1000
    infile = open('kiwi.jpeg', 'rb')
    outfile = open('new.jpeg', 'wb')
    buffer = infile.read(buffer_size)  # it is not an iterable object

    while len(buffer):
        outfile.write(buffer)
        print('.')
        buffer = infile.read(buffer_size)

    print()
    print('Done.')

if __name__ == '__main__':
    main()
