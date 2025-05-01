from flask import Flask, jsonify, Request, Response, request
from dotenv import load_dotenv

load_dotenv()
from config import Config
from models import db

from models.recipe import Recipe
from models.association import recipe_category
from models.category import Category
from models.ingredient import Ingredient

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Welcome to my Snack App!'

@app.route('/api/recipes' , methods = ['GET'])
def get_recipes():
    recipes = []
    for recipe in db.session.query(Recipe).all():
        recipes.append(recipe.as_dict())
    return jsonify(recipes)

@app.route("/api/recipes/<int:recipe_id>" , methods = ['GET'])
def get_recipe(recipe_id):
    for recipe in db.session.query(Recipe).all():
        if recipe.as_dict().get("id") == recipe_id:
            return jsonify(recipe.as_dict())
    return jsonify({"error": "Recipe not found"}) , 404

#tema validare
@app.route("/api/recipes" , methods = ["POST"])
def create_recipe():
    new_recipe = {
        "id": len(recipes) + 1,
        "name": request.json.get("name"),
        "duration": request.json.get("duration") ,
        "pictures": request.json.get("pictures") ,
        "instructions": request.json.get("instructions") ,
        "ingredients": request.json.get("ingredients") ,
        "categories": request.json.get("categories") ,
    }
    recipes.append(new_recipe)
    return jsonify(new_recipe), 201

@app.route("/api/recipes/<int:recipe_id>" , methods = ["DELETE"])
def delete_recipe(recipe_id):
    for recipe in recipes:
        if recipe.get("id") == recipe_id:
             recipes.remove(recipe)
             return jsonify(recipe), 200

    return jsonify({"error" : "Recipe not found"}) , 404

@app.route("/api/recipes/<int:recipe_id>" , methods = ["PUT"])
def update_recipe(recipe_id):

    for recipe in recipes :
        if recipe.get("id") == recipe_id:
            for key in recipe.keys():
                if key == "id":
                    continue
                recipe[key] = name if (name := request.json.get(key)) else recipe[key]


if __name__ == '__main__':
    with app.app_context():
       # db.drop_all()
        db.create_all()
    app.run(debug=True)

