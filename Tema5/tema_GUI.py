from inverse_calculator import Inverse

# from util import ListStream

from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = 'Flask app'
    return render_template('index.html', name=name)


# ##### Homework 5 routes #####

@app.route('/hw5/inverse', methods=['GET'])
def calculate_inverse_wrapper():
    test = Inverse(3, [[1.0, 2.0, 3.0], [0, 4, 5], [1, 0, 6]])
    return str(test.computeInverse())

@app.route('/hw5/inverse', methods=['POST'])
def calculate_inverse_post_wrapper():
    #test = Inverse(3, [[1.0, 2.0, 3.0], [0, 4, 5], [1, 0, 6]])

    print(request.get_json()) #force=True
    size = request.get_json()["size"]
    matrix = request.get_json()["matrix"]

    print(size)
    print(eval(matrix))

    test = Inverse(int(size), eval(matrix))
    temp = test.computeInverse()

    return str(temp)


@app.route('/result')
def smth_wrapper():
    return str('Not implemented')
