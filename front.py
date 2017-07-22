from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return jsonify({
    	"info": "Check subdomains like: tema[1-6]/"
    })