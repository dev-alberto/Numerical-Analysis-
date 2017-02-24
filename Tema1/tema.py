import random
import math
import time

### Primu Exercitiu ###


def find_precision():
    m = 0
    while 1.0 + 10 ** (-m) != 1.0:
        m += 1
    return 10 ** (-m + 1)

print("Smallest u that satisfies said property is " + str(find_precision()))

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

print("Addition Associativity: ")
print(add_assoc(1.0))
print("\n Multiplication associativity for a given number of iterations: ")
print(mul_assoc(100))

### Exercitiul 3 ###

c = [1/math.factorial(3), 1/math.factorial(5), 1/math.factorial(7), 1/math.factorial(9),
     1 / math.factorial(11), 1/math.factorial(13)]


def first_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-c[0] + c[1] * y))


def second_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-c[0] + y * (c[1] - c[2] * y)))


def third_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-c[0] + y * (c[1] + y * (-c[2] + c[3] * y))))


def fourth_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-0.166 + y * (0.00833 + y * (-c[2] + c[3] * y))))


def fifth_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-c[0] + y * (c[1] + y * (-c[2] + y * (c[3] - c[4] * y)))))


def sixth_poly_horner(x):
    y = x ** 2
    return x * (1 + y * (-c[0] + y * (c[1] + y * (-c[2] + y * (c[3] + y * (-c[4] + c[5] * y))))))


def first_poly(x):
    return x - c[0]*x**3 + c[1]*x**5


def second_poly(x):
    return x - c[0]*x**3 + c[1]*x**5 - c[2]*x**7


def third_poly(x):
    return x - c[0]*x**3 + c[1]*x**5 - c[2]*x**7 + c[3]*x**9


def fourth_poly(x):
    return x - 0.166*x**3 + 0.00833*x**5 - c[2]*x**7 + c[3]*x**9


def fifth_poly(x):
    return x - c[0]*x**3 + c[1]*x**5 - c[2]*x**7 + c[3]*x**9 - c[4]*x**11


def sixth_poly(x):
    return x - c[0]*x**3 + c[1]*x**5 - c[2]*x**7 + c[3]*x**9 - c[4]*x**11 + c[5]*x**13


def sin_values(x):
    return first_poly(x), second_poly(x), third_poly(x), fourth_poly(x), fifth_poly(x), sixth_poly(x)


random_numbers = []
r = 0
while r < 100000:
    random_numbers.append(random.uniform(-math.pi/2, math.pi/2))
    r += 1


def compute_ith_poly_error(i):
    result = []
    for j in range(0, len(random_numbers)):
        result.append(abs(sin_values(random_numbers[j])[i] - math.sin(random_numbers[j])))
    return result


def compute_ith_poly_mean_error(i):
    return sum(compute_ith_poly_error(i))/100000


def make_error_mean_list():
    mean_errors = []
    for j in range(0, 6):
        mean_errors.append(compute_ith_poly_mean_error(j))
    return mean_errors


def get_best_poly():
    return make_error_mean_list().index(min(make_error_mean_list())) + 1


def test_time():
    start1 = time.time()
    for j in random_numbers:
        first_poly_horner(j)
    end1 = time.time()
    print("Efficient First poly time is " + str((end1 - start1)))

    start2 = time.time()
    for j in random_numbers:
        second_poly_horner(j)
    end2 = time.time()
    print("Efficient Second poly time is " + str((end2 - start2)))

    start3 = time.time()
    for j in random_numbers:
        third_poly_horner(j)
    end3 = time.time()
    print("Efficient Third poly time is " + str((end3 - start3)))

    start4 = time.time()
    for j in random_numbers:
        fourth_poly_horner(j)
    end4 = time.time()
    print("Efficient Fourth poly time is " + str((end4 - start4)))

    start5 = time.time()
    for j in random_numbers:
        fifth_poly_horner(j)
    end5 = time.time()
    print("Efficient Fifth poly time is " + str((end5 - start5)))

    start6 = time.time()
    for j in random_numbers:
        sixth_poly_horner(j)
    end6 = time.time()
    print("Efficient Sixth poly time is " + str((end6 - start6)))

    print("************")

    start = time.time()
    for j in random_numbers:
        sixth_poly(j)
    end = time.time()

    print("Normal Sixth poly is " + str(end - start))

print("Best poly by error is: ")
print(get_best_poly())
test_time()



