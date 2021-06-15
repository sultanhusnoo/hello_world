
#	Chapter 9: Head First Python
#	Implementing same webapp with SQL Connector

from flask import Flask, render_template, request, redirect, escape, session
from vsearch import search4letters
from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

@app.route('/')
def hello() -> 'html':
	#	My homepage - will implement a homepage with access to other
	#	webapps and use more SQl databases
	return render_template('homepage.html', the_title="My Website")

app.config['dbconfig'] = {	"host":"127.0.0.1",
							"user":"vsearch",
							"password":"test123",
							"database":"vsearchlogDB",	}

def log_request(req:"flask request",res:str) -> None:
	#	log details of web searches and results.

	with UseDatabase(app.config['dbconfig']) as cursor:
		_SQL = """ insert into log 
				(phrase, letter, ip, browser_string, results)
				values (%s,%s, %s, %s, %s) """
		log_data = (req.form['phrase'],
					req.form['letters'],
					req.remote_addr,
					req.user_agent.browser,
					res,)
		cursor.execute(_SQL, log_data)

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
@check_logged_in
def view_log()->'html':
	""" Display the contents of the log file as an HTML table """
	with UseDatabase(app.config['dbconfig']) as cursor:
		_SQL = """ 	select id, phrase,letter,ip,
					browser_string,results from log """
		cursor.execute(_SQL)
		contents = cursor.fetchall()
	titles = ('ID','Phrase','Letters','Remote_Addr','User_Agent','Results')
	return render_template('viewlog.html',
							the_title='View Log',
							the_row_titles=titles,
							the_data=contents,)

@app.route('/login')
def do_login()-> str:
	session['logged_in'] = True
	return redirect('/')

@app.route('/logout')
def do_logout() -> str:
	session.pop('logged_in')
	return redirect('/')

app.secret_key = "secretkey123"

if __name__ == '__main__':
	app.run(debug=True)
