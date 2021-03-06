from flask import render_template, flash, url_for, redirect, request 
from flask_login import login_user,login_required,logout_user
from . import auth
from .forms import LoginForm,RegistrationForm
from ..models import User
from .. import db

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

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('auth.login'))

@auth.route('/register',methods=['GET','POST'])
def register():
	form=RegistrationForm()
	if form.validate_on_submit():
		user=User(email=form.email.data,username=form.username.data,password=form.password.data)
		db.session.add(user)
		flash('You can now login')
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html',form=form)
'''
@auth.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed'
'''