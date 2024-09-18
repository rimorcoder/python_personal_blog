from flask import Blueprint, render_template, request
from ..models.Blog import Blog
from flask_login import current_user

bp = Blueprint('search', __name__, template_folder='templates', url_prefix="/search")

@bp.route('/', strict_slashes=False)
def search():
    try:
        search = request.args.get('query')
        if search:
             search_term = f"%{search}%"
             search_results = Blog.query.filter(Blog.title.ilike(search_term)).limit(5).all()
        else:
            search_results = []
    except Exception as e:
        print(e)
    
    return render_template('search.html', user_logged_in=current_user.is_authenticated, search_results=search_results, search_query=search)