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


CATEGORY_COLORS = {
    'Baking': '#FFA500',  # orange
    'Cookies': '#D2691E',  # chocolate
    'Pie': '#FFD700',  # gold
    'Italian': '#FF0000',  # red
    'No-bake': '#ADD8E6'  # lightblue
}


def get_categories_helper(recipe_id, categories):
    categories_id = []
    for recipe_cat in db.session.query(recipe_category).all():
        if recipe_cat.recipe_id == recipe_id:
            categories_id.append(recipe_cat.category_id)
    for _id in categories_id:
        for category in db.session.query(Category).all():
            if category.id == _id:
                categories.append(category.name)

    return categories


@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = []
    for recipe in db.session.query(Recipe).all():
        dict_recipe = recipe.as_dict()
        categories = []

        dict_recipe["ingredients"] = [ingredient.as_dict() for ingredient in recipe.ingredients]

        categories = get_categories_helper(dict_recipe["id"], categories)
        dict_recipe["categories"] = categories

        recipes.append(dict_recipe)

    return jsonify(recipes), 200


@app.route("/api/recipes/<int:recipe_id>", methods=['GET'])
def get_recipe(recipe_id):
    for recipe in db.session.query(Recipe).all():
        if recipe.as_dict().get("id") == recipe_id:
            dict_recipe = recipe.as_dict()

            dict_recipe["ingredients"] = [ingredient.as_dict() for ingredient in recipe.ingredients]

            categories = []
            categories = get_categories_helper(dict_recipe["id"], categories)

            dict_recipe["categories"] = categories

            return jsonify(dict_recipe)

    return jsonify({"error": "Not found"}), 404


@app.route("/api/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()
    fields = ["name", "duration", "instructions", "pictures", "categories"]
    for field in fields:
        if data.get(field) is None:
            return jsonify({"error": f"Field {field} not found."}), 404

    category_objs = []
    for category_name in data.get("categories"):
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(
                name=category_name,
                color=CATEGORY_COLORS[category_name],
            )
        category_objs.append(category)
    recipe = Recipe(
        name=request.json.get("name"),
        duration=request.json.get("duration"),
        pictures=",".join(request.json.get("pictures")),
        instructions=request.json.get("instructions"),
        categories=category_objs
    )
    db.session.add(recipe)
    db.session.commit()
    return jsonify(recipe.as_dict()), 201


@app.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if not recipe:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(recipe)
    db.session.commit()
    return None, 204


@app.route("/api/recipes/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    data = request.get_json()

    recipe = db.session.get(Recipe, recipe_id)

    for key in data.keys():
        if key not in ["ingredients", "categories"]:
            setattr(recipe, key, data[key])

    if "categories" in data:
        updated_categories = []
        for category_data in data["categories"]:
            category = Category.query.filter_by(name=category_data["name"]).first()
            if not category:
                category = Category(name=category_data["name"], color=category_data["color"])
                db.session.add(category)
            else:
                for k, v in category_data.items():
                    setattr(category, k, v)
            updated_categories.append(category)
        recipe.categories = updated_categories

    if "ingredients" in data:
        for ingredient_data in data["ingredients"]:
            ingredient = Ingredient.query.filter_by(name=ingredient_data["name"]).first()
            if not ingredient:
                ingredient = Ingredient(name=ingredient_data["name"]
                                        , quantity=ingredient_data["quantity"]
                                        , unit=ingredient_data["unit"]
                                        , recipe_id=recipe_id)
                db.session.add(ingredient)
            else:
                for k, v in ingredient_data.items():
                    setattr(ingredient, k, v)

    db.session.commit()
    return jsonify(recipe.as_dict()), 204


@app.route("/api/categories", methods=["GET"])
def get_categories():
    categories = [category.as_dict() for category in db.session.query(Category).all()]
    return categories, 200


@app.route("/api/categories", methods=["POST"])
def create_category():
    data = request.get_json()
    fields = ["name", "color"]
    for field in fields:
        if data.get(field) is None:
            return jsonify({"error": f"Field {field} not found."}), 404
    category = Category.query.filter_by(name=data["name"]).first()
    if category:
        return jsonify({"error": "Category already exists"}), 400

    category = Category(
        name=data["name"],
        color=data["color"]
    )
    db.session.add(category)
    db.session.commit()
    return jsonify(category.as_dict()), 201


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
