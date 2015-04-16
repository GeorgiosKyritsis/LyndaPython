__author__ = 'inamoto21'

# read the lines from  file
fh = open("lines.txt")
for line in fh.readlines():
    print(line, end = '')
