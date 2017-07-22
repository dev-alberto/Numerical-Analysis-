# from hw3_test import Test
# from hw4_solver import Gauss
from .hw3_test import Test
from .hw4_solver import Gauss

# from util import ListStream

from flask import Flask
from flask import render_template

app = Flask(__name__)


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
@app.route('/hw4/system/1')
def system_1_wrapper():
    gauss1 = Gauss("sisteme/m_rar_2017_1.txt")
    return str(gauss1.check_solution())


@app.route('/hw4/system/2')
def system_2_wrapper():
    gauss2 = Gauss("sisteme/m_rar_2017_2.txt")
    return str(gauss2.check_solution())


@app.route('/hw4/system/3')
def system_3_wrapper():
    gauss3 = Gauss("sisteme/m_rar_2017_3.txt")
    return str(gauss3.check_solution())


@app.route('/hw4/system/4')
def system_4_wrapper():
    gauss4 = Gauss("sisteme/m_rar_2017_4.txt")
    return str(gauss4.check_solution())


@app.route('/result')
def smth_wrapper():
    # sys.stdout = x = ListStream()
    # f = open('_dmpFile', 'w+')

    # print() # ...

    # sys.stdout = sys.__stdout__
    # f.write( ''.join(x.data) )

    # read_output = f.read()
    # f.close()

    # return str(read_output)
    return str('Not implemented')
