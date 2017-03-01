from tema import LDL_Decomposition
from sympy import Matrix

from flask import Flask
from flask import render_template

app = Flask(__name__)

CH = LDL_Decomposition(Matrix([[1, 2.5, 3], [2.5, 8.25, 15.5], [3, 15.5, 43]]), [2, 3, 1], 10**(-10))


@app.route('/')
def hello_world():
    name = 'Flask app'
    return render_template('index.html', name=name)


# Route handlers
@app.route('/decompose')
def decompose():
	return str(CH.decompose_wrapper())

@app.route('/determinant')
def determinant():
	return str(CH.compute_determinant_wrapper())


@app.route('/solution')
def solution():
	return str(CH.solution_wrapper())

@app.route('/library-solution')
def library_solution():
	return str(CH.library_solution_wrapper())

@app.route('/precision')
def precision():
	return str(CH.check_precision())
