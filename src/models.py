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

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }

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

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "fav_character": self.fav_character,
        }

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

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water" : self.surface_water,
            "population" : self.population,
        }

class Fav_Character(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
        }

class Fav_Planet(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), primary_key=True)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }