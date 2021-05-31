#	Chapter 7 of Head First Python
#	Will implement same webapp with Database

from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)

#	My homepage - will implement a homepage with access to other
#	webapps
@app.route('/')
def hello() -> 'html':
	return render_template('homepage.html')

def log_request(req:"flask request",res:str) -> None:
	''' log details of web searches and results'''
	dbconfig = {"host":"127.0.0.1",
				"user":"vsearch",
				"password":"test123",
				"database":"vsearchlogDB",}
	conn = mysql.connector.connect(**dbconfig)
	cursor = conn.cursor()	
	_SQL = """ insert into log 
			(phrase, letter, ip, browser_string, results)
			values (%s,%s, %s, %s, %s) """
	log_data = (req.form['phrase'],
				req.form['letters'],
				req.remote_addr,
				req.user_agent.browser,
				res,)
	cursor.execute(_SQL, log_data)
	conn.commit()
	cursor.close()
	conn.close()
				
@app.route('/search4/', methods=['POST'])
def do_search() -> 'html':
	phrase = request.form['phrase']
	letters = request.form['letters'] 
	title = "Here are the Results: "
	results = str(search4letters(phrase,letters))
	log_request(request, results)	
	return render_template('results.html',
									the_phrase=phrase,
									the_title=title,
									the_letters=letters,
									the_results=results,)

@app.route('/entry/')
def entry_page() -> 'html':
	return render_template('entry.html',
			the_title='Welcome to search4letters online!')

@app.route('/viewlog/')
def view_log()->'html':
	contents = []
	with open('vsearch.log') as log:
		for line in log:
			contents.append([])
			for item in line.split('|'):
				contents[-1].append(escape(item))
	titles = ('Form_Data','Remote_Addr','User_Agent','Results')
	return render_template('viewlog.html',
							the_title='View Log',
							the_row_titles=titles,
							the_data=contents,)

if __name__ == '__main__':
	app.run(debug=True)

