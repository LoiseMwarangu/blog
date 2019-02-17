from . import auth
from flask import render_template,redirect,request,url_for,flash
from . import auth
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm
from ..models import User
from .forms import RegistrationForm
from .. import db