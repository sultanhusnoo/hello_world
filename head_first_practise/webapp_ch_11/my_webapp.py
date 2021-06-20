
#	Chapter 11: Head First Python
#	Implementing Exception Handling
#	Implementing threading

from flask import Flask, render_template, request, redirect, escape, session
from flask import copy_current_request_context

from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

from threading import Thread
from time import sleep

app = Flask(__name__)

app.config['dbconfig'] = {	
		"host":"127.0.0.1",	
		"user":"vsearch",
		"password":"test123", 
		"database":"vsearchlogDB",}

@app.route('/')
def hello() -> 'html':
	#	My homepage
	return render_template('homepage.html', the_title="My Website")

@app.route('/search4/', methods=['POST'])	#	Called when user clicks
def do_search() -> 'html':					#	'Do It' on 'entry' pg

	#***********************************************************************
	@copy_current_request_context	#	This is using THREADING
	def log_request(req:"flask request",res:str) -> None:
		#	log details of web searches and results.
		#	Exception raised by log_request and sent to do_search function
		#sleep(15)	#	No longer making user wait deliberately
		with UseDatabase(app.config['dbconfig']) as cursor:
			_SQL = """ insert into log (phrase, letter, ip, browser_string, results)
					values (%s,%s, %s, %s, %s) """
			log_data = (req.form['phrase'],	req.form['letters'],
						req.remote_addr, req.user_agent.browser, res,)
			cursor.execute(_SQL, log_data)
	#***********************************************************************
	
	phrase = request.form['phrase']
	letters = request.form['letters'] 
	title = "Here are the Results: "
	
	#	All this code exists to do this one line
	#
	results = str(search4letters(phrase,letters))	#*****************
	#
	#
	
	try:
		log_request(request, results)	
	except Exception as err:	#	Error will occur in log_request
		print("*** *** *** Error: ", str(err),"*** *** ***")
	
	return render_template('results.html', the_phrase=phrase,
		the_title=title, the_letters=letters, the_results=results,)

@app.route('/entry/')
def entry_page() -> 'html':
	return render_template('entry.html',
			the_title='Welcome to search4letters online!')

@app.route('/viewlog/')
@check_logged_in
def view_log()->'html':
	""" Display the contents of the log file as an HTML table """
	try:
		
		with UseDatabase(app.config['dbconfig']) as cursor:
			_SQL = """ select id, phrase,letter,ip,
						browser_string,results from log """
			cursor.execute(_SQL)
			contents = cursor.fetchall()
		titles = ('ID','Phrase','Letters','Remote_Addr', 
					'User_Agent','Results')
		return render_template('viewlog.html', the_title='View Log',
								the_row_titles=titles, the_data=contents,)
								
	except ConnectionError as err:
		print("Is your database switched ON? Error in view_log fn: ", str(err))
	except CredentialsError as err:
		print("User-id/pw error: ", str(err))
	except SQLError as err:
		print("Is your SQL ok? Error: ", str(err))
	except Exception as err:
		print("Something fucked up in view_log function: ", str(err))
	return 'An Error occured in view_log function.'	
		
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
