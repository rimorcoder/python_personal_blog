from flask import Blueprint, render_template, request

bp = Blueprint('home', __name__, template_folder='templates')

@bp.route('/')
def home():
    return render_template('home.html')
