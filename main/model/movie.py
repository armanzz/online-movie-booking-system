from .. import db
import datetime 

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(db.String(255))
    movie_duration = db.Column(db.Integer)
    director = db.Column(db.String(255))
    genre = db.Column(db.String(255))
    release_date = db.Column(db.Date)  # Storing only the date part
    synopsis = db.Column(db.Text)  # Using Text type for potentially long text fields
    screening = db.relationship('Screening', lazy='dynamic', backref='movie')