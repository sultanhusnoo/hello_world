
from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> 'html':
	return render_template('homepage.html')

def log_request(req:request,res:str) -> None:
	with open('vsearch.log','a') as log:
		print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

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

