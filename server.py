from flask import Flask, render_template, redirect, request, session, flash
import re, time, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^.(?=.[a-z])(?=.[A-Z])(?=.[\d\W]).*$')
DOB_REGEX = re.compile(r'^.(\b\d{1,2}[-/:]\d{1,2}[-/:]\d{4}\b)')
app=Flask(__name__)
app.secret_key='BUSYUDODIS2ME'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/new', methods=['POST'])
def new():
	session['email'] = request.form['email']
	session['fname'] = request.form['first_name']
	session['lname'] = request.form['last_name']
	session['pass'] = request.form['password']

	if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['confirmpass']) < 1:
		flash('Please fill out all fields!')
	elif len(request.form['password']) < 8 or len(request.form['confirmpass']) < 8:
		flash('Password must be 8 characters or longer!')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address!')
	elif not PASS_REGEX.match(request.form['password']):
		flash('Password must contain at least 1 uppercase letter and 1 number.')
	elif session['fname'].isalpha() == False or session['lname'].isalpha() == False:
		flash('Name cannot contain numbers!')
	elif request.form['confirmpass'] != request.form['password']:
		flash('Passwords do not match!')
	elif any(session['password'].isdigit() for char in session) == False:
		flash('Password must contain at least 1 number!')
	else:
		flash('Successfully registered!')
	return redirect('/')

app.run(debug=True)