from flask import Flask, render_template, flash, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm  # Assuming RegisterForm and LoginForm are defined in forms.py
from models import db, User  # Assuming db and User are defined in models.py
from flask_bcrypt import Bcrypt
from functools import wraps

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "donotsteal"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # SQLite database file is named db.sqlite in the current directory
    
    db.init_app(app)
    bcrypt = Bcrypt(app)
    
    with app.app_context():
        db.create_all()
        
    def login_required(f):
        @wraps(f)
        def decorated_function(*args , **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            return f(*args , **kwargs)
        return decorated_function
            


    @app.route('/')
    def home():
        return render_template("home.html")

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id
                session['username'] = user.username  # Assuming username is the correct attribute
                flash('You have been logged in!', 'success')
                return redirect(url_for('dashboard'))  # Redirect to the dashboard page after successful login
            else:
                flash('Login unsuccessful. Please check your email and password.', 'danger')
        return render_template("login.html", form=form)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        form = RegisterForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=hashed_password
            )
            db.session.add(user)
            db.session.commit()
            flash("Your account has been created!", 'success')
            return redirect(url_for('login'))
        return render_template("register.html", form=form)

    @app.route('/dashboard')
    @login_required
    def dashboard():
        return render_template("dashboard.html")
    
    @app.route('/logout')
    def logout():
     session.pop('user_id', None)  # Safely remove 'user_id' from session
     session.pop('username', None)  # Safely remove 'username' from session
     flash('You have been logged out!', 'success')
     return redirect(url_for('home'))  # Redirect to the home page after logging out


    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
