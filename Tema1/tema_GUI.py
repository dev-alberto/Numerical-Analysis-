import tema as tm
import random
import math

from flask import Flask
from flask import render_template

app = Flask(__name__)

'''

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
PA = PolynomialApproximator(c)

print(PA.get_best_poly())

PA.test_time()
'''

@app.context_processor
def utility_processor():
	def find_precision_wrapper():
		return str(tm.find_precision())
	def add_assoc_hardcoded_wrapper():
		return str(tm.add_assoc(1.0))
	def mul_assoc_hardcoded_wrapper():
		return str(tm.mul_assoc(100))

	def polyomial_hardcoded_wrapper():
		random_numbers = []
		r = 0
		while r < 100000:
			random_numbers.append(random.uniform(-math.pi/2, math.pi/2))
			r += 1

		c = [0.16666666666666666666666666666667, 0.00833333333333333333333333333333, 1.984126984126984126984126984127e-4,
			 2.7557319223985890652557319223986e-6,
			 2.5052108385441718775052108385442e-8, 1.6059043836821614599392377170155e-10]
		PA = tm.PolynomialApproximator(c, random_numbers)

		return str(PA.get_best_poly()) + '\n' + str(PA.test_time())

	def polyomial_time_hardcoded_wrapper():
		return str(PA.test_time())

	return dict(
		find_precision 	= find_precision_wrapper,
		add_assoc		= add_assoc_hardcoded_wrapper,
		mul_assoc 		= mul_assoc_hardcoded_wrapper,
		polynomial 		= polyomial_hardcoded_wrapper
	)

@app.route('/')
def hello_world():
	name = 'Flask app'
	return render_template('index.html', name=name)


# Route handlers
@app.route('/precision')
def find_precision_wrapper():
	return str(tm.find_precision())

@app.route('/add')
def add_assoc_hardcoded_wrapper():
	return str(tm.add_assoc(1.0))

@app.route('/mul')
def mul_assoc_hardcoded_wrapper():
	return str(tm.mul_assoc(100))

@app.route('/polynomial')
def polyomial_hardcoded_wrapper():
	random_numbers = []
	r = 0
	while r < 100000:
		random_numbers.append(random.uniform(-math.pi/2, math.pi/2))
		r += 1

	c = [0.16666666666666666666666666666667, 0.00833333333333333333333333333333, 1.984126984126984126984126984127e-4,
		 2.7557319223985890652557319223986e-6,
		 2.5052108385441718775052108385442e-8, 1.6059043836821614599392377170155e-10]
	PA = tm.PolynomialApproximator(c, random_numbers)

	print(PA.get_best_poly())
	print(PA.test_time())


	return str(PA.get_best_poly()) + '\n' + str(PA.test_time())
