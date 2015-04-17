__author__ = 'inamoto21'


def main():
    s = 'This is a string of words'
    words = s.split()

    for w in words:
        print(w)

    new = ':'.join(words)
    print(new)


if __name__ == '__main__':
    main()
