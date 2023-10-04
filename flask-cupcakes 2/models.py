"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    # def __repr__(self):
    #     p = self
    #     return f" Hello my name is {p.first_name} {p.last_name}, here is my user picture {p.image_url}"
    
    # def get_first_name(cls, first_name):
    #  return cls.query.filter(first_name)
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    flavor = db.Column(db.String,
                     nullable=False,
                     unique=True)
    size = db.Column(db.String
                     , nullable = False)
    rating = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=True, default='https://tinyurl.com/demo-cupcake')
    
    def serialize(self):
        return {
            'id' : self.id,
            'flavor' : self.flavor,
            'size' : self.size,
            'rating' : self.rating, 
            'image' : self.image
        }