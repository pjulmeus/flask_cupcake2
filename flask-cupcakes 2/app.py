"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/cupcakes')
def cupcake_list():
    all_cupcake = [c.serialize() for c in Cupcake.query.all()]
    return jsonify(all_cupcake = all_cupcake)

@app.route('/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake = cupcake.serialize())

@app.route('/cupcakes/<int:cupcake_id>', methods = ["POST"])
def create_cupcake():
    if new_cupcake_flavor:
        new_cupcake_flavor = request.json["flavor"]
    if new_cupcake_size:
        new_cupcake_size = request.json["size"]
    if new_cupcake_rating:
        new_cupcake_rating = request.json["rating"]
    if new_cupcake_image:
        new_cupcake_image = request.json["image"]
    
    new_cupcake = Cupcake(flavor = new_cupcake_flavor, size = new_cupcake_size, rating = new_cupcake_rating, image = new_cupcake_image)

    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(new_cupcake.serialize())
    return (response_json, 201)

@app.route('/cupcakes/<int:cupcake_id>', methods = ["PATCH"])
def edit_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    request.json.get('flavor', cupcake.flavor)
    request.json.get('size', cupcake.size)
    request.json.get('rating', cupcake.rating)
    request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())

@app.route('/cupcakes/<int:cupcake_id>', methods = ["PATCH"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit(jsonify(message= "deleted"))





