from flask import Blueprint, render_template, request
from ..models.Blog import Blog

bp = Blueprint('search', __name__, template_folder='templates', url_prefix="/search")

@bp.route('/', strict_slashes=False)
def search():
    try:
        search = request.args.get('query')
        if search:
             search_results = Blog.query.filter(Blog.title.ilike(f'%{search}%')).limit(5).all()
        else:
            search_results = []
    except Exception as e:
        print(e)
    
    return render_template('search.html', search_results=search_results, search_query=search)