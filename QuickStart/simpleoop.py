__author__ = 'inamoto21'


class Fibonacci():  # simple Fibonacci series
    def __init__(self, a, b):  # constructor
        self._a = a
        self._b = b

    def series(self):  # generator of iterator
        while True:
            yield self._b
            self._a, self._b = self._b, self._a + self._b


f = Fibonacci(0, 1)  # instance of the class
for r in f.series():  # call the generator function
    if r > 100:
        break
    print(r, end=' ')