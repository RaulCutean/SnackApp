# from flask import Flask, jsonify, Request, Response, request
# from dotenv import load_dotenv
#
# load_dotenv()
# from config import Config
# from models import db
#
# from models.recipe import Recipe
# from models.association import recipe_category
# from models.category import Category
# from models.ingredient import Ingredient
#
# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
#
# recipes = [
#     {
#         "id": 1,
#         "name": "Chocolate Chip Cookies",
#         "duration": "30 minutes",
#         "pictures": [
#             "https://handletheheat.com/wp-content/uploads/2020/10/BAKERY-STYLE-CHOCOLATE-CHIP-COOKIES-9-637x637-1.jpg"
#         ],
#         "instructions": "Preheat oven to 180\u00b0C. Mix butter and sugar, add eggs and vanilla, then fold in flour, baking soda, and chocolate chips. Scoop onto a baking sheet and bake for 12-15 minutes.",
#         "categories": [
#             "Cookies",
#             "Baking"
#         ],
#         "ingredients": [
#             {
#                 "quantity": "250",
#                 "unit": "g",
#                 "name": "all-purpose flour"
#             },
#             {
#                 "quantity": "125",
#                 "unit": "g",
#                 "name": "butter"
#             },
#             {
#                 "quantity": "100",
#                 "unit": "g",
#                 "name": "sugar"
#             },
#             {
#                 "quantity": "1",
#                 "unit": None,
#                 "name": "egg"
#             },
#             {
#                 "quantity": "5",
#                 "unit": "g",
#                 "name": "vanilla extract"
#             },
#             {
#                 "quantity": "3",
#                 "unit": "g",
#                 "name": "baking soda"
#             },
#             {
#                 "quantity": "150",
#                 "unit": "g",
#                 "name": "chocolate chips"
#             }
#         ]
#     },
#     {
#         "id": 2,
#         "name": "Tiramisu",
#         "duration": "4 hours",
#         "pictures": [
#             "https://staticcookist.akamaized.net/wp-content/uploads/sites/22/2024/09/THUMB-VIDEO-2_rev1-56.jpeg",
#             "https://retete.unica.ro/wp-content/uploads/2010/07/tiramisu-pas-cu-pas1.jpg"
#         ],
#         "instructions": "Mix mascarpone, sugar, and egg yolks. Dip ladyfingers in coffee and layer with mascarpone mixture. Repeat and top with cocoa powder. Refrigerate for at least 4 hours before serving.",
#         "categories": [
#             "Italian",
#             "No-bake"
#         ],
#         "ingredients": [
#             {
#                 "quantity": "250",
#                 "unit": "g",
#                 "name": "mascarpone cheese"
#             },
#             {
#                 "quantity": "100",
#                 "unit": "g",
#                 "name": "sugar"
#             },
#             {
#                 "quantity": "3",
#                 "unit": None,
#                 "name": "egg yolks"
#             },
#             {
#                 "quantity": "200",
#                 "unit": "g",
#                 "name": "ladyfingers"
#             },
#             {
#                 "quantity": "300",
#                 "unit": "ml",
#                 "name": "brewed coffee"
#             },
#             {
#                 "quantity": "20",
#                 "unit": "g",
#                 "name": "cocoa powder"
#             }
#         ]
#     },
#     {
#         "id": 3,
#         "name": "Apple Pie",
#         "duration": "1.5 hours",
#         "pictures": [
#             "https://www.southernliving.com/thmb/bbDY1d_ySIrCFcq8WNBkR-3x6pU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/2589601_Mailb_Mailbox_Apple_Pie_003-da802ff7a8984b2fa9aa0535997ab246.jpg"
#         ],
#         "instructions": "Prepare a pastry dough and chill. Slice apples and mix with sugar, cinnamon, and lemon juice. Roll out dough, fill with apples, cover with top crust, and bake at 190\u00b0C for 45 minutes.",
#         "categories": [
#             "Pie",
#             "Baking"
#         ],
#         "ingredients": [
#             {
#                 "quantity": "300",
#                 "unit": "g",
#                 "name": "all-purpose flour"
#             },
#             {
#                 "quantity": "150",
#                 "unit": "g",
#                 "name": "butter"
#             },
#             {
#                 "quantity": "50",
#                 "unit": "g",
#                 "name": "sugar"
#             },
#             {
#                 "quantity": "4",
#                 "unit": None,
#                 "name": "apples"
#             },
#             {
#                 "quantity": "50",
#                 "unit": "g",
#                 "name": "brown sugar"
#             },
#             {
#                 "quantity": "5",
#                 "unit": "g",
#                 "name": "cinnamon"
#             },
#             {
#                 "quantity": "10",
#                 "unit": "ml",
#                 "name": "lemon juice"
#             }
#         ]
#     }
# ]
#
#
# @app.route('/')
# def hello_world():
#     return 'Welcome to my Snack App!'
#
#
# @app.route('/api/recipes', methods=['GET'])
# def get_recipes():
#     return jsonify(recipes)
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=['GET'])
# def get_recipe(recipe_id):
#     for recipe in recipes:
#         print(recipe)
#         if recipe.get("id") == recipe_id:
#             return jsonify(recipe)
#     return jsonify({"error": "Recipe not found"}), 404
#
#
# # tema validare
# @app.route("/api/recipes", methods=["POST"])
# def create_recipe():
#     new_recipe = {
#         "id": len(recipes) + 1,
#         "name": request.json.get("name"),
#         "duration": request.json.get("duration"),
#         "pictures": request.json.get("pictures"),
#         "instructions": request.json.get("instructions"),
#         "ingredients": request.json.get("ingredients"),
#         "categories": request.json.get("categories"),
#     }
#     recipes.append(new_recipe)
#     return jsonify(new_recipe), 201
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
# def delete_recipe(recipe_id):
#     for recipe in recipes:
#         if recipe.get("id") == recipe_id:
#             recipes.remove(recipe)
#             return jsonify(recipe), 200
#
#     return jsonify({"error": "Recipe not found"}), 404
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=["PUT"])
# def update_recipe(recipe_id):
#     for recipe in recipes:
#         if recipe.get("id") == recipe_id:
#             for key in recipe.keys():
#                 if key == "id":
#                     continue
#                 recipe[key] = name if (name := request.json.get(key)) else recipe[key]
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         # db.drop_all()
#         db.create_all()
#     app.run(debug=True)
#


# for recipe_cat in db.session.query(recipe_category).all():
#                if recipe_cat.recipe_id == dict_recipe["id"]:
#                    categories_id.append(recipe_cat.category_id)
#            for id in categories_id:
#                for category in db.session.query(Category).all():
#                    if category.id == id:
#                        categories.append(category.name)
# ingredients = []

# for ingredient in db.session.query(Ingredient).all():
#     if ingredient.recipe_id == dict_recipe["id"]:
#         ingredients.append(ingredient.as_dict())
# print(f"{ingredient.name} : {dict_recipe["name"]}")
# dict_recipe["ingredients"] = ingredients

# def validate_helper(dictionary , fields):
#     for key in dictionary:
#         if key not in fields and dictionary[key] is None:
#             return False
#     return True




#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////


# import csv
# import re
# import json
# from app import app, db
# from models.category import Category
# from models.ingredient import Ingredient
# from models.recipe import Recipe
#
# CATEGORY_COLORS = {
#     'Baking': '#FFA500',  # orange
#     'Cookies': '#D2691E',  # chocolate
#     'Pie': '#FFD700',  # gold
#     'Italian': '#FF0000',  # red
#     'No-bake': '#ADD8E6'  # lightblue
# }
#
#
# def get_all_recipes():
#     # Regex to match the ingredient format
#     ingredient_regex = re.compile(r'^(?P<quantity>\d+)(?P<unit>[a-zA-Z]*) (?P<name>.+)$')
#     # Open a CSV file to read all recipes and a JSON file to write the processed data
#     recipes = []
#     with open('../recipes.csv', 'r') as csvfile, open('../recipes.json', 'w') as jsonfile:
#         # Read CSV file in dict format with header as keys
#         dict_reader = csv.DictReader(csvfile)
#         for row in dict_reader:
#             row['Pictures'] = row['Pictures'].split(',')
#             row['Categories'] = row['Categories'].split(',')
#             row['Ingredients'] = row['Ingredients'].split(',')
#             ingredients = []
#             for ingredient in row['Ingredients']:
#                 ingredient_matches = ingredient_regex.match(ingredient)
#                 ingredients.append({
#                     'quantity': ingredient_matches['quantity'],
#                     'unit': unit if (unit := ingredient_matches['unit']) else None,
#                     'name': ingredient_matches['name'],
#                 })
#             row['Ingredients'] = ingredients
#             recipes.append(row)
#         # Write processed dict to JSON file
#         json.dump(recipes, jsonfile)
#     return recipes
#
#
# def populate_db(recipes):
#     # Start app context to access DB
#     with app.app_context():
#         try:
#             for recipe_data in recipes:
#                 # Handle categories
#                 category_objs = []
#                 for cat_name in recipe_data['Categories']:
#                     # Try to find an existing category
#                     category = Category.query.filter_by(name=cat_name).first()
#                     if not category:
#                         category = Category(
#                             name=cat_name,
#                             color=CATEGORY_COLORS.get(cat_name, '#848482')  # Default to gray in hex
#                         )
#                         db.session.add(category)
#                     category_objs.append(category)
#
#                 # Create a recipe
#                 recipe = Recipe(
#                     name=recipe_data['Recipe name'],
#                     duration=recipe_data['Duration'],
#                     pictures=','.join(recipe_data['Pictures']),
#                     instructions=recipe_data['Instructions'],
#                     categories=category_objs
#                 )
#                 db.session.add(recipe)
#                 db.session.flush()  # Ensure recipe.id is available
#
#                 # Add ingredients
#                 for ing in recipe_data['Ingredients']:
#
#                     ingredient = Ingredient(
#                         name=ing['name'],
#                         quantity=ing['quantity'],
#                         unit=ing['unit'],
#                         recipe_id=recipe.id
#                     )
#                     db.session.add(ingredient)
#
#                 print(f'Inserted recipe: {recipe.name}')
#
#             db.session.commit()
#             print('Database populated successfully!')
#
#         except Exception as exc:
#             db.session.rollback()
#             print('Error during population:', exc)
#
#
# if __name__ == '__main__':
#     all_recipes = get_all_recipes()
#     populate_db(all_recipes)


#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////


#
#
# from flask import Flask, jsonify, Request, Response, request
# from dotenv import load_dotenv
#
# load_dotenv()
# from config import Config
# from models import db
#
# from models.recipe import Recipe
# from models.association import recipe_category
# from models.category import Category
# from models.ingredient import Ingredient
#
# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
#
#
# @app.route('/')
# def hello_world():
#     return 'Welcome to my Snack App!'
#
#
# CATEGORY_COLORS = {
#     'Baking': '#FFA500',  # orange
#     'Cookies': '#D2691E',  # chocolate
#     'Pie': '#FFD700',  # gold
#     'Italian': '#FF0000',  # red
#     'No-bake': '#ADD8E6'  # lightblue
# }
#
#
# def get_categories_helper(recipe_id, categories):
#     categories_id = []
#     for recipe_cat in db.session.query(recipe_category).all():
#         if recipe_cat.recipe_id == recipe_id:
#             categories_id.append(recipe_cat.category_id)
#     for _id in categories_id:
#         for category in db.session.query(Category).all():
#             if category.id == _id:
#                 categories.append(category.name)
#
#     return categories
#
#
# @app.route('/api/recipes', methods=['GET'])
# def get_recipes():
#     recipes = []
#     for recipe in db.session.query(Recipe).all():
#         dict_recipe = recipe.as_dict()
#         categories = []
#
#         dict_recipe["ingredients"] = [ingredient.as_dict() for ingredient in recipe.ingredients]
#
#         categories = get_categories_helper(dict_recipe["id"], categories)
#         dict_recipe["categories"] = categories
#
#         recipes.append(dict_recipe)
#
#     return jsonify(recipes), 200
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=['GET'])
# def get_recipe(recipe_id):
#     for recipe in db.session.query(Recipe).all():
#         if recipe.as_dict().get("id") == recipe_id:
#             dict_recipe = recipe.as_dict()
#
#             dict_recipe["ingredients"] = [ingredient.as_dict() for ingredient in recipe.ingredients]
#
#             categories = []
#             categories = get_categories_helper(dict_recipe["id"], categories)
#
#             dict_recipe["categories"] = categories
#
#             return jsonify(dict_recipe)
#
#     return jsonify({"error": "Not found"}), 404
#
#
# @app.route("/api/recipes", methods=["POST"])
# def create_recipe():
#     data = request.get_json()
#     fields = ["name", "duration", "instructions", "pictures", "categories"]
#     for field in fields:
#         if data.get(field) is None:
#             return jsonify({"error": f"Field {field} not found."}), 404
#
#     category_objs = []
#     for category_name in data.get("categories"):
#         category = Category.query.filter_by(name=category_name).first()
#         if not category:
#             category = Category(
#                 name=category_name,
#                 color=CATEGORY_COLORS[category_name],
#             )
#         category_objs.append(category)
#     recipe = Recipe(
#         name=request.json.get("name"),
#         duration=request.json.get("duration"),
#         pictures=",".join(request.json.get("pictures")),
#         instructions=request.json.get("instructions"),
#         categories=category_objs
#     )
#     db.session.add(recipe)
#     db.session.commit()
#     return jsonify(recipe.as_dict()), 201
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=["DELETE"])
# def delete_recipe(recipe_id):
#     recipe = db.session.query(Recipe).get(recipe_id)
#     if not recipe:
#         return jsonify({"error": "Not found"}), 404
#     db.session.delete(recipe)
#     db.session.commit()
#     return None, 204
#
#
# @app.route("/api/recipes/<int:recipe_id>", methods=["PUT"])
# def update_recipe(recipe_id):
#     data = request.get_json()
#
#     recipe = db.session.get(Recipe, recipe_id)
#
#     for key in data.keys():
#         if key not in ["ingredients", "categories"]:
#             setattr(recipe, key, data[key])
#
#     if "categories" in data:
#         updated_categories = []
#         for category_data in data["categories"]:
#             category = Category.query.filter_by(name=category_data["name"]).first()
#             if not category:
#                 category = Category(name=category_data["name"], color=category_data["color"])
#                 db.session.add(category)
#             else:
#                 for k, v in category_data.items():
#                     setattr(category, k, v)
#             updated_categories.append(category)
#         recipe.categories = updated_categories
#
#     if "ingredients" in data:
#         for ingredient_data in data["ingredients"]:
#             ingredient = Ingredient.query.filter_by(name=ingredient_data["name"]).first()
#             if not ingredient:
#                 ingredient = Ingredient(name=ingredient_data["name"]
#                                         , quantity=ingredient_data["quantity"]
#                                         , unit=ingredient_data["unit"]
#                                         , recipe_id=recipe_id)
#                 db.session.add(ingredient)
#             else:
#                 for k, v in ingredient_data.items():
#                     setattr(ingredient, k, v)
#
#     db.session.commit()
#     return None, 204
#
#
# @app.route("/api/categories", methods=["GET"])
# def get_categories():
#     categories = [category.as_dict() for category in db.session.query(Category).all()]
#     return categories, 200
#
#
# @app.route("/api/categories", methods=["POST"])
# def create_category():
#     data = request.get_json()
#     fields = ["name", "color"]
#     for field in fields:
#         if data.get(field) is None:
#             return jsonify({"error": f"Field {field} not found."}), 404
#     category = Category.query.filter_by(name=data["name"]).first()
#     if category:
#         return jsonify({"error": "Category already exists"}), 400
#
#     category = Category(
#         name=data["name"],
#         color=data["color"]
#     )
#     db.session.add(category)
#     db.session.commit()
#     return jsonify(category.as_dict()), 201
#
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         app.run(debug=True)
