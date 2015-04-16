__author__ = 'inamoto21'


def main():
    fh = open("lines.txt")
    for line in fh.readlines():  # for loop is designed to work with iterators
        print(line, end="")

    for i in [1, 2, 3, 4, 5]:
        print(i, end='')

    for j in 'string':
        print(j, end=" ")

if __name__ == '__main__':
    main()