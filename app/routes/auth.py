from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from ..models.User import User
from ..extensions import login_manager

bp = Blueprint('auth', __name__, template_folder='templates', url_prefix="/auth")

login_manager.login_view = 'auth/login'
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"{username} : {password}")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin.admin'))
        else:
            message = "Invalid username/password"
            return render_template('login.html', message=message)
    return render_template('login.html')

@bp.route('/logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))