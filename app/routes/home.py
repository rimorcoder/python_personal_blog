from flask import Blueprint, render_template, request
from ..models.Blog import Blog

bp = Blueprint('home', __name__, template_folder='templates')

@bp.route('/', strict_slashes=False)
def home():
    # process search
    search_results = ''
    search = request.args.get('search')
    if search:
        search_results = Blog.query.filter_by(category=search).all()
    
    # get latest blogs
    latest_blogs = Blog.query.order_by(Blog.updated_at.desc()).limit(5).all()
    
    # get latest blogs by category
    latest_blogs_by_category = ''



    return render_template('home.html', search_results=search_results, latest_blogs=latest_blogs, latest_blogs_by_category=latest_blogs_by_category)
