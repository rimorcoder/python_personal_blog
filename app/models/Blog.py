from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
db = SQLAlchemy()

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(64))
    category = db.Column(db.String(64),index=True)
    blog = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    @classmethod
    def exists(cls, title):
        return db.session.query(cls.id).filter_by(title=title).scalar() is not None