#import tema as tm
from . import tema as tm

from flask import Flask
from flask import render_template

app = Flask(__name__)

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


@app.route('/mul-ex')
def mul_ex_assoc_hardcoded_wrapper():
    return str(tm.print_not_assoc_mul())


@app.route('/polynomial')
def polynomial_hardcoded_wrapper():
    return tm.poly_tests()
