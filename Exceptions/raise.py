__author__ = 'inamoto21'


def main():
    try:
        for line in readfile('lines.doc'):
            print(line.strip())
    except IOError as e:
        print('cannot read file:', e)
    except ValueError as e:
        print('bad file name:', e)


def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .txt')


if __name__ == '__main__':
    main()