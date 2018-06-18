from datetime import datetime 
from flask import render_template,session,redirect,url_for,flash
from flask_login import login_required
from . import main 
from .forms import NameForm
from .. import db 
from ..models import User

@main.route('/asshole',methods=['GET','POST'])
@main.route('/',methods=['GET'])
def asshole():
	return render_template('asshole.html')