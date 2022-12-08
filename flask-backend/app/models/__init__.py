from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True) #no validations
    happiness = db.Column(db.Integer) #no validations
    image_url = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)  #no validations
    pokemon_id = db.Column(db.Integer, nullable=False)  #no validations

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True,  nullable=False)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
    name = db.Column(db.String(1000), nullable=False, unique=True)
    type = db.Column()
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float)
    catch_rate = db.Column(db.Float)
    captured = db.Column(db.Boolean)  #no validations