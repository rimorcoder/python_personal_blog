from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

class Blog(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    author = db.Column(db.String(64))
    tags = db.Column(db.Text, index=True)
    blog = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.utc))

    def set_tags(self, ctags_list):
        self.tags = json.dumps(tags_list)

    def get_tags(self):
        return json.loads(self.tags)