from flask import Flask, jsonify, Request, Response, request
from dotenv import load_dotenv
from itsdangerous import NoneAlgorithm

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
        ingredients = []
        dict_recipe = recipe.as_dict()
        dict_recipe["pictures"] = [picture for picture in dict_recipe["pictures"].split(",")]
        for ingredient in db.session.query(Ingredient).all():
            if ingredient.recipe_id == dict_recipe["id"]:
                ingredients.append(ingredient.as_dict())
                # print(f"{ingredient.name} : {dict_recipe["name"]}")
        dict_recipe["ingredients"] = ingredients
        # print(dict_recipe)
        recipes.append(dict_recipe)
    if len(recipes) == 0 :
        return jsonify({'recipes': []}) , 200
    return jsonify(recipes) , 200

@app.route("/api/recipes/<int:recipe_id>" , methods = ['GET'])
def get_recipe(recipe_id):
    for recipe in db.session.query(Recipe).all():
        if recipe.as_dict().get("id") == recipe_id:
            dict_recipe = recipe.as_dict()
            dict_recipe["pictures"] = [picture for picture in dict_recipe["pictures"].split(",")]
            ingredients = []
            for ingredient in db.session.query(Ingredient).all():
                if ingredient.recipe_id == dict_recipe["id"]:
                    ingredients.append(ingredient.as_dict())
                    dict_recipe["ingredients"] = ingredients
            return jsonify(dict_recipe)

    return jsonify({"error": "Recipe not found"}) , 404

#tema validate
def validate(*args):
    for arg in args:
        if arg is None:
            return False
    return True
@app.route("/api/recipes" , methods = ["POST"])
def create_recipe():
    if not validate(request.json.get("name"),request.json.get("duration"),request.json.get("pictures"), request.json.get("instructions")):
        return jsonify({"error": "Bad request"}), 400
    print(request.json.get("name"))
    recipe = Recipe(
        name = request.json.get("name"),
        duration = request.json.get("duration"),
        pictures = ",".join(request.json.get("pictures")),
        instructions = request.json.get("instructions"),
    )
    db.session.add(recipe)
    # recipes.append(new_recipe)
    return jsonify(recipe.as_dict()), 201

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

