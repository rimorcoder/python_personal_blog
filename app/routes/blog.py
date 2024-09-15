from flask import Blueprint, render_template, request

bp = Blueprint('blog', __name__, template_folder='templates', url_prefix='/blog')

@bp.route('/')
def blog():
    return render_template('blog_search.html')

@bp.route('/<int:id>')
def get_blog(id):
    title = "Lorem ipsum dolor sit amet consectetur"
    blog = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Soluta debitis culpa facere reiciendis ex quia officiis esse assumenda recusandae maxime quasi, ea suscipit mollitia architecto voluptas saepe voluptatibus corporis inventore."
    return render_template('blog.html', title=title, blog=blog)
