import random
import math
import time

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


    def first_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + self.c[1] * y))


    def second_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] - self.c[2] * y)))


    def third_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + self.c[3] * y))))


    def fourth_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-0.166 + y * (0.00833 + y * (-self.c[2] + self.c[3] * y))))


    def fifth_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + y * (self.c[3] - self.c[4] * y)))))


    def sixth_poly(self, x):
        y = x ** 2
        return x * (1 + y * (-self.c[0] + y * (self.c[1] + y * (-self.c[2] + y * (self.c[3] + y * (-self.c[4] + self.c[5] * y))))))


    def sin_values(self, x):
        return self.fifth_poly(x), self.second_poly(x), self.third_poly(x), self.fourth_poly(x), self.fifth_poly(x), self.sixth_poly(x)



    def compute_ith_poly_error(self, i):
        result = []
        for j in range(0, len(self.random_numbers)):
            result.append(abs(self.sin_values(self.random_numbers[j])[i] - math.sin(self.random_numbers[j])))
        return result


    def compute_ith_poly_mean_error(self, i):
        return sum(self.compute_ith_poly_error(i))/100000


    def make_error_mean_list(self):
        mean_errors = []
        for j in range(0, 6):
            mean_errors.append(self.compute_ith_poly_mean_error(j))
        return mean_errors


    def get_best_poly(self):
        return self.make_error_mean_list().index(min(self.make_error_mean_list())) + 1


    def test_time(self):
        output = ''

        start1 = time.time()
        for j in self.random_numbers:
            self.first_poly(j)
        end1 = time.time()
        print("First poly time is " + str((end1 - start1)))
        output += "\nFirst poly time is " + str((end1 - start1))

        start2 = time.time()
        for j in self.random_numbers:
            self.second_poly(j)
        end2 = time.time()
        print("Second poly time is " + str((end2 - start2)))
        output += "\nSecond poly time is " + str((end2 - start2))

        start3 = time.time()
        for j in self.random_numbers:
            self.third_poly(j)
        end3 = time.time()
        print("Third poly time is " + str((end3 - start3)))
        output += "\nThird poly time is " + str((end3 - start3))

        start4 = time.time()
        for j in self.random_numbers:
            self.fourth_poly(j)
        end4 = time.time()
        print("Fourth poly time is " + str((end4 - start4)))
        output += "\nFourth poly time is " + str((end4 - start4))

        start5 = time.time()
        for j in self.random_numbers:
            self.fifth_poly(j)
        end5 = time.time()
        print("Fifth poly time is " + str((end5 - start5)))
        output += "\nFifth poly time is " + str((end5 - start5))

        start6 = time.time()
        for j in self.random_numbers:
            self.sixth_poly(j)
        end6 = time.time()
        print("Sixth poly time is " + str((end6 - start6)))
        output += "\nSixth poly time is " + str((end6 - start6))

        return output



if __name__ == "__main__":

    # Exe 1
    print("Smallest u that satisfies said property is " + str(find_precision()))

    # Exe 2
    print("Addition Associativity: ")
    print(add_assoc(1.0))
    print("\n Multiplication associativity for a given number of iterations: ")
    print(mul_assoc(100))

    # Exe 3
    random_numbers = []
    r = 0
    while r < 100000:
        random_numbers.append(random.uniform(-math.pi/2, math.pi/2))
        r += 1
    
    print("Best poly is: ")

    c = [0.16666666666666666666666666666667, 0.00833333333333333333333333333333, 1.984126984126984126984126984127e-4,
         2.7557319223985890652557319223986e-6,
         2.5052108385441718775052108385442e-8, 1.6059043836821614599392377170155e-10]
    PA = PolynomialApproximator(c, random_numbers)

    print(PA.get_best_poly())

    PA.test_time()
