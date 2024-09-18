from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from ..models.Blog import Blog

bp = Blueprint('admin', __name__, template_folder='templates', url_prefix="/admin")

@bp.route('/', strict_slashes=False)
@login_required
def admin():
    all_blogs = Blog.query.all()
    return render_template('admin.html', user_logged_in=current_user.is_authenticated, all_blogs=all_blogs)
