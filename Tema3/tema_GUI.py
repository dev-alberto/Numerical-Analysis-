# from tema import LDL_Decomposition
# from sympy import Matrix
from solver import Gauss

import sys
from solver import ListStream

from flask import Flask
from flask import render_template

app = Flask(__name__)


import sys

class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        #print(s)
        self.data.append(s)

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


# Route handlers
@app.route('/result')
def result():
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



