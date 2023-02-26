from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")
# passing variable by adding it after loginhtml user="bruno", userList=["maja", "antek", "bruno"] (for instance and u can write if statment in loi)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash(' Enter a proper email', category='error')
        elif len(firstName) < 2:
            flash(' Name must have more then 2 characters', category='error')
        elif password1 != password2:
            flash(' Passwords do not match', category='error')
        elif len(password1) < 7:
            flash(' Password must have more than 7 characters', category='error')
        else:
            flash('You created an account', category='valid')
    return render_template("sign_up.html")


@auth.route('/gallery')
def gallery():
    return render_template("gallery.html")