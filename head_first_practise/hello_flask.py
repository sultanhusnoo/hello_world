
from flask import Flask
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
	return "Hello. Fuck you from Flask!"

@app.route('/search4/')
def do_search() -> str:
	result = search4letters("sultan")
	return str(result)

app.run()

