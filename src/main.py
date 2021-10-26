"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Fav_Character, Fav_Planet
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
#from models import Person

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "token"
jwt = JWTManager(app)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username, password=password).first()
    if user is None:
        raise APIException('Incorrect username or password', status_code=401)

    access_token = create_access_token(identity=user.id)
    return jsonify(access_token=access_token)

@app.route('/character', methods=["GET"])
def get_character():
    character_query = Character.query.all()
    all_characters = list(map(lambda x: x.serialize(), character_query))
    return jsonify(all_characters)

@app.route('/character/<int:character_id>', methods=["GET"])
def get_ind_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        raise APIException("Character not found", status_code=404)
    character = character.serialize()
    return jsonify(character)

@app.route('/planet', methods=["GET"])
def get_planet():
    planet_query = Planet.query.all()
    all_planets = list(map(lambda x: x.serialize(), planet_query))
    return jsonify(all_planets)

@app.route('/planet/<int:planet_id>', methods=["GET"])
def get_ind_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if id is None:
        raise APIException("Planet not found", status_Code=404)
    planet=planet.serialize()
    return jsonify(planet)

@app.route('/users', methods=["GET"])
@jwt_required()
def get_users():
    users_query = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users_query))
    return jsonify(all_users)

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
