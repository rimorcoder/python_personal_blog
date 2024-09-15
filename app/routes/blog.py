from flask import Blueprint, render_template, request
from ..models.Blog import Blog

bp = Blueprint('blog', __name__, template_folder='templates', url_prefix="/blog")

@bp.route('/', strict_slashes=False)
def blog():
    category = request.args.get('category')
    
    if category:
        blogs = Blog.query.filter_by(category=category).all()
    else:
        blogs = Blog.query.order_by(Blog.updated_at.desc()).limit(5).all()
    
    categories = Blog.query.with_entities(Blog.category).distinct().all()
    categories = [c[0] for c in categories]
    
    return render_template('blog_search.html', categories=categories, blogs=blogs)

@bp.route('/<int:id>',  strict_slashes=False)
def get_blog(id):
    blog_entry = Blog.query.get(id)
    if blog_entry is None:
        return render_template('blog.html',error_message="Blog not found")
    return render_template('blog.html', 
                           title=blog_entry.title,
                           author=blog_entry.author,
                           category=blog_entry.category, 
                           created_at=blog_entry.created_at,
                           updated_at=blog_entry.updated_at,
                           blog=blog_entry.blog)
