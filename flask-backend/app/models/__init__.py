
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