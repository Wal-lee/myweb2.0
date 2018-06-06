from datetime import datetime 
from flask import render_template,session,redirect,url_for,flash
from flask_login import login_required
from . import main 
from .forms import NameForm
from .. import db 
from ..models import User

@main.route('/asshole',methods=['GET','POST'])
@login_required
def asshole():
	form=NameForm()
	if form.validate_on_submit():
		user=User.query.filter_by(username=form.name.data).first()
		if user is None:
			user=User(username=form.name.data)
			db.session.add(user)
			session['known']=False
		else:
			session['known']=True
		session['name']=form.name.data 
		form.name.data=''
		old_name=session.get('name')
		if old_name is not None and old_name!=form.name.data:
			flash('looks like you have changed your name')
		return redirect(url_for('.asshole'))
	return render_template('asshole.html',name=session.get('name'),form=form,known=session.get('known',False))