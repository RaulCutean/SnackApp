from flask import Flask, jsonify, Request, Response, request
from dotenv import load_dotenv

from import_script import get_all_recipes, populate_db

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

ERROR404_RESPONSE = {'error': 'recipe not found'}


def add_ingredients_to_db(ingredients, recipe_id):
    for ing in ingredients:
        try:
            quantity = float(ing['quantity'])
        except ValueError as exc:
            return jsonify({'error': f'quantity is not of type float: {exc}'}), 400

        ingredient = Ingredient(
            name=ing['name'],
            quantity=quantity,
            unit=ing['unit'],
            recipe_id=recipe_id,
        )
        db.session.add(ingredient)


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
    fields = ["name", "duration", "instructions", "pictures", "categories" , "ingredients"]

    for field in fields:
        if data.get(field) is None:
            return jsonify({"error": f"Field {field} not found."}), 404
    pictures = data.get("pictures")
    if not pictures or not isinstance(pictures, list):
        return jsonify({"error": "pictures field is required"}), 400
    for cat in data['categories']:
        if 'name' not in cat:
            return jsonify({'error': 'categories must contain a name'}), 400
    for ing in data['ingredients']:
        if 'name' not in ing or 'quantity' not in ing:
            return jsonify({'error': 'ingredients must contain a name, quantity and unit (optional)'}), 400
    try:
        category_objs = []
        for cat in data.get("categories"):
            category = Category.query.filter_by(name=cat["name"]).first()
            if not category:
                return jsonify({"error": f"category {cat["name"]} not found"}), 400
            category_objs.append(category)
        recipe = Recipe(
            name=request.json.get("name"),
            duration=request.json.get("duration"),
            pictures=",".join(request.json.get("pictures")),
            instructions=request.json.get("instructions"),
            categories=category_objs
        )
        db.session.add(recipe)
        db.session.flush()
        add_ingredients_to_db(data['ingredients'], recipe.id)
        db.session.commit()
        return jsonify(recipe.as_dict()), 201
    except Exception as exc:
        db.session.rollback()
        return jsonify({'error': f'something went wrong: {exc}'}), 500


@app.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if not recipe:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(recipe)
    db.session.commit()
    return {}, 204



@app.route('/api/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    try:
        recipe = Recipe.query.get(recipe_id)
        if not recipe:
            return jsonify(ERROR404_RESPONSE), 404

        recipe.name = new_name if (new_name := request.json.get('name')) else recipe.name
        recipe.duration = new_duration if (new_duration := request.json.get('duration')) else recipe.duration
        recipe.pictures = new_pictures if (new_pictures := request.json.get('pictures')) else recipe.pictures
        recipe.instructions = new_instr if (new_instr := request.json.get('instructions')) else recipe.instructions

        if new_categories := request.json.get('categories'):
            category_objs = []
            for cat in new_categories:
                category = Category.query.filter_by(name=cat['name']).first()
                if not category:
                    return jsonify({'error': f'category {cat["name"]} not found'}), 400
                category_objs.append(category)
            recipe.categories = category_objs

        if new_ingredients := request.json.get('ingredients'):
            Ingredient.query.filter_by(recipe_id=recipe_id).delete()
            add_ingredients_to_db(new_ingredients, recipe.id)

        db.session.commit()
        print(f'Updated recipe: {recipe.name}')
        return jsonify(recipe.as_dict()), 201
    except Exception as exc:
        db.session.rollback()
        return jsonify({'error': f'something went wrong: {exc}'}), 500


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
        db.drop_all()
        db.create_all()
        populate_db(get_all_recipes(), app, db)
    app.run(host="0.0.0.0", debug=True, port=5000)
