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

class Pokemon(db.Model):
    __tablename__ = 'pokemons'
