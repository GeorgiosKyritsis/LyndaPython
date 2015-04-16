__author__ = 'inamoto21'

import re

def main():
    fh = open('raven.txt')
    pattern = re.compile('Nevermore', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(line, end='')

if __name__ == '__main__':
    main()