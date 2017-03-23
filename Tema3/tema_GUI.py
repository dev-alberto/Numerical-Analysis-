from hw3_test import Test
from hw4_solver import Gauss

import sys
#from solver import ListStream

from flask import Flask
from flask import render_template

app = Flask(__name__)


# class ListStream:
#     def __init__(self):
#         self.data = []
#     def write(self, s):
#         #print(s)
#         self.data.append(s)

'''
sys.stdout = x = ListStream()
f = open('_dmpFile', 'w')

gauss = Gauss("sisteme/m_rar_2017_1.txt")
print(gauss.size)
# gauss.formula3()
gauss.seidel()

sys.stdout = sys.__stdout__
# print(x.data)
f.write( ''.join(x.data) )

f.close()
'''


@app.route('/')
def hello_world():
	name = 'Flask app'
	return render_template('index.html', name=name)



# ##### Homework 3 routes #####
@app.route('/hw3/sum')
def test_matrix_sum_wrapper():
	test = Test()
	return str(test.test_matrix_sum())

@app.route('/hw3/vprod')
def test_vector_product_wrapper():
	test = Test()
	return str(test.test_vector_product())

@app.route('/hw3/mprod')
def test_matrix_product_wrapper():
	test = Test()
	return str(test.test_matrix_product())
	
	

# ##### Homework 4 routes #####

'''
print("First system, checking solution")
gauss1 = Gauss("sisteme/m_rar_2017_1.txt")
gauss1.check_solution()

print("Second system, checking solution")
gauss2 = Gauss("sisteme/m_rar_2017_2.txt")
gauss2.check_solution()

print("Third system, checking solution")
gauss3 = Gauss("sisteme/m_rar_2017_3.txt")
gauss3.check_solution()

print("Fourth system, checking solution")
gauss4 = Gauss("sisteme/m_rar_2017_4.txt")
print(gauss4.check_solution())
'''

@app.route('/result')
def smth_wrapper():
	#tema 3 
	#test.py

	#tema 4
	# sys.stdout = x = ListStream()
	# f = open('_dmpFile', 'w+')

	# gauss = Gauss("sisteme/m_rar_2017_1.txt")
	# print(gauss.size)
	# # gauss.formula3()
	# gauss.seidel()

	# sys.stdout = sys.__stdout__
	# f.write( ''.join(x.data) )

	# read_output = f.read()
	# f.close()

	#return str(read_output)
	return str('Not implemented')