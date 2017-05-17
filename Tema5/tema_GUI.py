from inverse_calculator import Inverse

# from util import ListStream

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = 'Flask app'
    return render_template('index.html', name=name)


# ##### Homework 5 routes #####

@app.route('/hw5/inverse')
def calculate_inverse_wrapper():
    test = Inverse(3, [[1.0, 2.0, 3.0], [0, 4, 5], [1, 0, 6]])
    return str(test.computeInverse())

@app.route('/result')
def smth_wrapper():
    return str('Not implemented')
