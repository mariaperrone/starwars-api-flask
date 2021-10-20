from flask_sqlalchemy import SQLAlchemy
import enum

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password  = db.Column(db.String(50), unique=False, nullable=False)

class GenderEnum(enum.Enum):
    male=1
    female=2
    not_specified=3

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birth_year = db.Column(db.Integer, unique=False, nullable=False)
    gender= db.Column(db.Enum(GenderEnum, unique=False, nullable=True))
    height= db.Column(db.Integer, unique=False, nullable=True)
    skin_color = db.Column(db.String(20), unique=False, nullable=True)
    eye_color = Column(String(20), unique=False, nullable=True)

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Integer, unique=False, nullable=True)
    diameter = db.Column(db.Integer, unique=False, nullable=True)
    climate = Column(db.String(20), unique=False, nullable=True)
    gravity = Column(db.String(20), unique=False, nullable=True)
    terrain = Column(db.String(20), unique=False, nullable=True)
    surface_water = db.Column(db.Integer, unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }