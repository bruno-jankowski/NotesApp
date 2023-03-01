from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user ##module of flask used for passing login user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') ##This referes to the email and password we posted so what we type in

        user = User.query.filter_by(email=email).first() ##returns the first resoult of filtering by column email so it finds the user with this column email and takkes all of his variables from a class
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='valid')
                login_user(user, remember=True)
                return redirect(url_for('auth.gallery'))
            else:
                flash('Inccorect password, try again', category='error')
        else:
            flash('There is no such user', category='error')

    return render_template("login.html")
# passing variable by adding it after loginhtml user="bruno", userList=["maja", "antek", "bruno"] (for instance and u can write if statment in loi)


@auth.route('/logout')
@login_required    ##this decorations we add to the pages user can not access unless they are login in 
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif len(email) < 4:
            flash(' Enter a proper email', category='error')
        elif len(first_name) < 2:
            flash(' Name must have more then 2 characters', category='error')
        elif password1 != password2:
            flash(' Passwords do not match', category='error')
        elif len(password1) < 7:
            flash(' Password must have more than 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256')) ##hashing the password and passing it to the user (sha256 is method  of hashing)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('You created an account', category='valid')
            return redirect(url_for('views.home'))
   
    user = current_user   
    return render_template("sign_up.html", user=user)


@auth.route('/gallery')
@login_required
def gallery():
    return render_template("gallery.html")