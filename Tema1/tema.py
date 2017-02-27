import random
import math
import time
import numpy


### Exercitiu 1 ###

def find_precision():
    m = 0
    while 1.0 + 10 ** (-m) != 1.0:
        m += 1
    return 10 ** (-m + 1)


### Exercitiu 2 ###

def add_assoc(x):
    precision = find_precision()
    y = precision
    z = y
    return (x + y) + z == x + (y + z)


def mul_assoc(iterations):
    not_assoc = 0
    while iterations != 0:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        if (x * y) * z != x * (y * z):
            not_assoc += 1
        iterations -= 1
    return not_assoc


### Exercitiul 3 ###

class PolynomialApproximator:
    def __init__(self, c, random_numbers):
        self.c = c
        self.random_numbers = random_numbers
        self.n = len(random_numbers)

    def first_poly(self, x):
        return x - self.c[0] * x ** 3 + self.c[1] * x ** 5

    def second_poly(self, x):
        return x - self.c[0] * x ** 3 + self.c[1] * x ** 5 - self.c[2] * x ** 7

    def third_poly(self, x):
        return x - self.c[0] * x ** 3 + self.c[1] * x ** 5 - self.c[2] * x ** 7 + self.c[3] * x ** 9

    def fourth_poly(self, x):
        return x - 0.166 * x ** 3 + 0.00833 * x ** 5 - self.c[2] * x ** 7 + self.c[3] * x ** 9

    def fifth_poly(self, x):
        return x - self.c[0] * x ** 3 + self.c[1] * x ** 5 - self.c[2] * x ** 7 + self.c[3] * x ** 9 - self.c[4] * x ** 11

    def sixth_poly(self, x):
        return x - self.c[0] * x ** 3 + self.c[1] * x ** 5 - self.c[2] * x ** 7 + self.c[3] * x ** 9 - self.c[4] * x ** 11 + self.c[5] * x ** 13

    def sin_values(self, x):
        return self.first_poly(x), self.second_poly(x), self.third_poly(x), self.fourth_poly(x), self.fifth_poly(
            x), self.sixth_poly(x)

    def compute_ith_poly_error(self, i):
        result = []
        for j in range(0, len(self.random_numbers)):
            result.append(abs(self.sin_values(self.random_numbers[j])[i] - math.sin(self.random_numbers[j])))
        return result

    def compute_ith_poly_mean_error(self, i):
        return sum(self.compute_ith_poly_error(i)) / self.n

    def make_error_mean_list(self):
        mean_errors = []
        for j in range(0, 6):
            mean_errors.append(self.compute_ith_poly_mean_error(j))
        return mean_errors

    def get_best_poly(self):
        error_mean_list = numpy.array(self.make_error_mean_list())
        sorted_indeces = numpy.argsort(error_mean_list)
        return sorted_indeces

    def first_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + self.c[1] * y))

    def second_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] - self.c[2] * y)))

    def third_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + self.c[3] * y))))

    def fourth_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-0.166 + y * (0.00833 + y * (-self.c[2] + self.c[3] * y))))

    def fifth_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + y * (self.c[3] - self.c[4] * y)))))

    def sixth_poly_horner(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + y * (self.c[3] + y * (-self.c[4] + self.c[5] * y))))))

    def test_time(self):
        output = ''

        start1 = time.time()
        for j in self.random_numbers:
            self.first_poly_horner(j)
        end1 = time.time()
        print("Efficient first poly time is " + str((end1 - start1)))
        output += "<br/>Efficient First poly time is " + str((end1 - start1))

        start2 = time.time()
        for j in self.random_numbers:
            self.second_poly_horner(j)
        end2 = time.time()
        print("Efficient second poly time is " + str((end2 - start2)))
        output += "<br/>Efficient Second poly time is " + str((end2 - start2))

        start3 = time.time()
        for j in self.random_numbers:
            self.third_poly_horner(j)
        end3 = time.time()
        print("Efficient third poly time is " + str((end3 - start3)))
        output += "<br/>Efficient Third poly time is " + str((end3 - start3))

        start4 = time.time()
        for j in self.random_numbers:
            self.fourth_poly_horner(j)
        end4 = time.time()
        print("Efficient fourth poly time is " + str((end4 - start4)))
        output += "<br/>Efficient Fourth poly time is " + str((end4 - start4))

        start5 = time.time()
        for j in self.random_numbers:
            self.fifth_poly_horner(j)
        end5 = time.time()
        print("Efficient fifth poly time is " + str((end5 - start5)))
        output += "<br/>Efficient Fifth poly time is " + str((end5 - start5))

        start6 = time.time()
        for j in self.random_numbers:
            self.sixth_poly_horner(j)
        end6 = time.time()
        print("Efficient Sixth poly time is " + str((end6 - start6)))
        output += "<br/>Efficient Sixth poly time is " + str((end6 - start6))

        start = time.time()
        for j in self.random_numbers:
            self.sixth_poly(j)
        end = time.time()
        print("Normal sixth poly time is " + str((end - start)))
        output += "<br/>Normal sixth poly time is " + str((end - start))
        return output


def poly_tests():
    random_numbers = []
    r = 0
    while r < 1000:
        random_numbers.append(random.uniform(-math.pi / 2, math.pi / 2))
        r += 1
    c = [1 / math.factorial(3), 1 / math.factorial(5), 1 / math.factorial(7), 1 / math.factorial(9),
         1 / math.factorial(11), 1 / math.factorial(13)]
    PA = PolynomialApproximator(c, random_numbers)

   # print(PA.make_error_mean_list())
    print(PA.get_best_poly())

    return str(PA.get_best_poly()) + '\n' + str(PA.test_time())

if __name__ == "__main__":
    # Exe 1
    print("Smallest u that satisfies said property is " + str(find_precision()))

    # Exe 2
    print("Addition Associativity: ")
    print(add_assoc(1.0))
    print("\n Multiplication associativity for a given number of iterations: ")
    print(mul_assoc(100))

    # Exe 3
    poly_tests()

