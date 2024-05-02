from . import db
from datetime import datetime


class Movies(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    description = db.Column(db.String(80), nullable=False)
    poster = db.Column(db.String(80), nullable=False)
