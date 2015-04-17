__author__ = 'inamoto21'


def main():
    d = dict(bob=5, fred=42)

    new_string = 'this is {bob} and that is {fred}'.format(**d)
    print(new_string)


if __name__ == '__main__':
    main()
