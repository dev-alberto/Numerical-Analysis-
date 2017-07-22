from werkzeug.wsgi import DispatcherMiddleware

import front as frontend
from front import app as front
#from Tema1 import tema_GUI as tema1
from Tema1.tema_GUI import app as tema1
from Tema2.tema_GUI import app as tema2
from Tema3.tema_GUI import app as tema3
from Tema5.tema_GUI import app as tema5
from Tema6.tema_GUI import app as tema6

# flask version
from flask import Flask
application = Flask(__name__)

application.wsgi_app = DispatcherMiddleware(front, {
    '/tema1': tema1,
    '/tema2': tema2,
    '/tema3': tema3,
    '/tema5': tema5,
    '/tema6': tema6
})

application.run(debug=True)

# wsgi version
# from werkzeug.serving import run_simple
# 
# application = DispatcherMiddleware(frontend, {
#     '/tema1': tema1
# })

# if __name__ == '__main__':
# 	run_simple('localhost', 5000, application, 
# 		use_reloader=True, use_debugger=True, use_evalex=True)