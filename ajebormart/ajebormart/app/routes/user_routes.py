from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import RegistrationForm, LoginForm

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # create user account
        flash('Account created successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login user
        flash('Login successful!')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')