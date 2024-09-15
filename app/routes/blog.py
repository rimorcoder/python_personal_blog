from flask import Blueprint, render_template, request
from ..models.Blog import Blog

bp = Blueprint('blog', __name__, template_folder='templates', url_prefix='/blog')

@bp.route('/')
def blog():
    # List available catagories
    # list available tags
    return render_template('blog_search.html')

@bp.route('/<int:id>')
def get_blog(id):
    blog_entry = Blog.query.get(id)
    if blog_entry is None:
        return render_template('blog.html',error_message="Blog not found")
    return render_template('blog.html', title=blog_entry.title, blog=blog_entry.blog)
