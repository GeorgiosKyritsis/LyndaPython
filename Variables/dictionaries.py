__author__ = 'inamoto21'


def main():
    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}  # dictionary
    print(d)

    for k in sorted(d.keys()):
        print(k, d[k])

    dic = dict(  # more convenient way to define dictionary
        one=1,
        two=2,
        three=3,
        four=4,
        five=5
    )
    dic['seven'] = 7

    print(dic)

if __name__ == '__main__':
    main()