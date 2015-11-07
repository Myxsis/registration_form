from flask import Flask, render_template, redirect, request, session, flash
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
	elif request.form['confirmpass'] != request.form['password']:
		flash('Passwords do not match!')
	else:
		flash('Successfully registered!')
	return redirect('/')

app.run(debug=True)