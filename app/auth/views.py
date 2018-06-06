from flask import render_template, flash, url_for, redirect, request 
from flask_login import login_user,login_required,login_user
from . import auth
from .forms import LoginForm 
from ..models import User

@auth.route('/', methods=['GET','POST'])
@auth.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		user=User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user,form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.asshole'))
		flash('Invalid username or password')
	return render_template('auth/login.html',form=form)

@auth.route('logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('auth/login'))
'''
@auth.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed'
'''