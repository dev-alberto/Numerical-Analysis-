from werkzeug.wsgi import DispatcherMiddleware

import front as frontend
from front import app as front
#from Tema1 import tema_GUI as tema1


# flask version
from flask import Flask
application = Flask(__name__)

application.wsgi_app = DispatcherMiddleware(front, {
    '/tema1': tema1
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