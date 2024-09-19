from datetime import datetime, timezone
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from ..models.Blog import Blog
from ..extensions import db 

bp = Blueprint('admin', __name__, template_folder='templates', url_prefix="/admin")

@bp.route('/', strict_slashes=False)
@login_required
def admin():
    all_blogs = Blog.query.all()
    return render_template('admin.html', user_logged_in=current_user.is_authenticated, all_blogs=all_blogs)


@bp.route('/delete' ,strict_slashes=False, methods=['POST'])
@login_required
def delete():
    id = request.form['blog_id']
    # Query the blog by ID
    blog = Blog.query.get(id)
    
    if blog:
        # Delete the blog from the database
        db.session.delete(blog)
        db.session.commit()
    return redirect(url_for('admin.admin'))

@bp.route('/update/<int:id>' ,strict_slashes=False, methods=['POST','GET'])
@login_required
def update(id):
    if request.method == 'GET':
        blog_entry = Blog.query.get(id)
        print(blog_entry)
        if blog_entry is None:
            return redirect(url_for('admin.admin'))
        return render_template('update.html', 
                            blog_entry=blog_entry,
                            user_logged_in=current_user.is_authenticated)
    
    if request.method == 'POST':
        blog_entry = Blog.query.get(id)
        if blog_entry is None:
            return redirect(url_for('admin.admin'))
        
        # Assuming you have form data to update the blog entry
        blog_entry.title = request.form['title']
        blog_entry.author = request.form['author']
        blog_entry.category = request.form['category']
        blog_entry.blog = request.form['blog']
        blog_entry.updated_at = datetime.now(timezone.utc)
        
        db.session.commit()
        
        return redirect(url_for('admin.admin'))