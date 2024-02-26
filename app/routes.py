from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, ProductForm


@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index page')


@app.route('/about_me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me Page')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been Registered successfully {form.username.data}')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Product URL"""
    form = ProductForm()
    if form.validate_on_submit():
        flash(f'Your Product has been added. {form.username.data}')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Product Addition', form=form)