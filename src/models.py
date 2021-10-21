import enum 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password  = db.Column(db.String(50), unique=False, nullable=False)
    fav_character = db.relationship('Fav_Character', backref='user')
    fav_planet = db.relationship('Fav_Planet', backref='user')

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
    eye_color = db.Column(db.String(20), unique=False, nullable=True)
    fav_character = db.relationship('Fav_Character', backref='character')

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    rotation_period = db.Column(db.Integer, unique=False, nullable=True)
    orbital_period = db.Column(db.Integer, unique=False, nullable=True)
    diameter = db.Column(db.Integer, unique=False, nullable=True)
    climate = db.Column(db.String(20), unique=False, nullable=True)
    gravity = db.Column(db.String(20), unique=False, nullable=True)
    terrain = db.Column(db.String(20), unique=False, nullable=True)
    surface_water = db.Column(db.Integer, unique=False, nullable=True)
    population = db.Column(db.Integer, unique=False, nullable=False)
    fav_planet = db.relationship('Fav_Planet', backref='planet')

class Fav_Character(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)

class Fav_Planet(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), primary_key=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }