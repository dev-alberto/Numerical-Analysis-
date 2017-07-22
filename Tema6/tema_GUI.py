# from eigen_values import Solver
from .eigen_values import Solver

# from util import ListStream

from flask import Flask
from flask import render_template, request

app = Flask(__name__)


'''
check driver.py for call examples
'''

@app.route('/')
def hello_world():
	name = 'Flask app'
	return render_template('index.html', name=name)


# ##### Homework 6 routes #####

@app.route('/hw6/largest_eigen', methods=['GET'])
def find_largest_eigen_value_wrapper():
	solver = Solver("m_rar_sim_2017.txt", 1500)
	return str(solver.find_largest_eigen_value()) #rand=True


@app.route('/hw6/random_v0', methods=['GET'])
def generate_random_v0_wrapper():
	solver = Solver("m_rar_sim_2017.txt", 1500)
	return str(solver.generate_random_v0())


@app.route('/hw6/multiply_column_line', methods=['POST'])
def multiply_column_vector_with_line_vector_wrapper():
	# [1, 2, 3], [1, 0, 1]

	solver = Solver("m_rar_sim_2017.txt", 1500)

	print(request.get_json()) #force=True
	col_vector = request.get_json()["col_vector"]
	lin_vector = request.get_json()["lin_vector"]

	print(eval(col_vector))
	print(eval(lin_vector))

	return str(solver.multiply_column_vector_with_line_vector(eval(col_vector), eval(lin_vector)))


@app.route('/hw6/multiply_matrix_vector', methods=['POST'])
def multiply_matrix_with_vector_wrapper():
	# [[1, 0, 1], [2, 0, 2], [3, 0, 3]], [1, 2, 3]
	solver = Solver("m_rar_sim_2017.txt", 1500)

	print(request.get_json()) #force=True
	matrix = request.get_json()["matrix"]
	vector = request.get_json()["vector"]

	print(eval(matrix))
	print(eval(vector))

	return str(solver.multiply_matrix_with_vector(eval(matrix), eval(vector)))


@app.route('/hw6/svd_matrix', methods=['GET'])
def generate_svd_matrix_wrapper():
	solver = Solver("m_rar_sim_2017.txt", 1500)
	return str(solver.generate_svd_matrix())


@app.route('/hw6/svd_eigen', methods=['POST'])
def find_svd_eigen_values_wrapper():
	solver = Solver("m_rar_sim_2017.txt", 1500)

	print(request.get_json()) #force=True
	a = request.get_json()["a"]
	b = request.get_json()["b"]

	print(int(a))
	print(int(b))

	return str(solver.find_svd_eigen_values(int(a), int(b)))


@app.route('/result')
def smth_wrapper():
	return str('Not implemented')
