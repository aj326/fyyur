from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

# ----------------------------------------------------------------------------#
# Models.
# ----------------------------------------------------------------------------#
app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False, unique=True)
    image_link = db.Column(db.String(500), nullable=True, unique=False)
    facebook_link = db.Column(db.String(120), nullable=True, unique=False)
    website = db.Column(db.String(120), nullable=True, unique=False)
    genres = db.Column(db.String, nullable=False)
    seeking_talent = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String, nullable=True, unique=False)
    shows = db.relationship('Show', backref='Venue', lazy=True)

    # upcoming and past shows are the result of joining venues and artists. (venue_id,artist_id,show_id, show_date)
    # website_link, genres,  seeking_talent, seeking_description, upcoming, past
    def __repr__(self):
        return f'<Venue {self.id}:{[self.name, self.address, self.city, self.state, self.phone, self.image_link, self.facebook_link, self.website, self.genres, self.seeking_talent, self.seeking_description]}'


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    city = db.Column(db.String(120), nullable=False, )
    state = db.Column(db.String(120), nullable=False, )
    phone = db.Column(db.String(120), nullable=True, unique=True)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=True, unique=False)
    website = db.Column(db.String(120), nullable=True, unique=False)
    facebook_link = db.Column(db.String(120), nullable=True, unique=False)
    seeking_venue = db.Column(db.Boolean, nullable=False)
    seeking_description = db.Column(db.String, nullable=True, unique=False)
    shows = db.relationship('Show', backref='Artist', lazy=True)

    def __repr__(self):
        return f'<Artist {self.id}:{[self.name, self.city, self.state, self.phone, self.image_link, self.facebook_link, self.website, self.genres, self.seeking_venue, self.seeking_description]}'


class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey(Venue.id), nullable=False)

    def __repr__(self):
        return f'<Artist {self.id}:{[self.venue_id, self.artist_id, self.start_time]}'
