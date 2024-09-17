from collections import defaultdict
from flask import Blueprint, render_template, request
from ..models.Blog import Blog

bp = Blueprint('home', __name__, template_folder='templates')

@bp.route('/', strict_slashes=False)
def home():
    # get latest blogs
    latest_blogs = Blog.query.order_by(Blog.updated_at.desc()).limit(8).all()
    
    # get latest blogs by category
    blogs = Blog.query.with_entities(Blog.id, Blog.title, Blog.category, Blog.updated_at).all()
    blogs_by_category = defaultdict(list)
    for blog in blogs:
        blogs_by_category[blog.category].append(blog)
    latest_blogs_by_category = {}
    for category, blogs in blogs_by_category.items():
        # Sort blogs by updated_at in descending order and take the top 5
        sorted_blogs = sorted(blogs, key=lambda x: x.updated_at, reverse=True)
        latest_blogs_by_category[category] = sorted_blogs[:5]
    
    return render_template('home.html', latest_blogs=latest_blogs, latest_blogs_by_category=latest_blogs_by_category)
