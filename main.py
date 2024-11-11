import json

from flask import Flask, jsonify, request

app = Flask(__name__)

recipe_list = [
    {
        "id": 1,
        "title": "Spaghetti Bolognese",
        "ingredients": [
            {"name": "Spaghetti", "quantity": 400, "unit": "g"},
            {"name": "Hackfleisch", "quantity": 250, "unit": "g"},
            {"name": "Tomatensauce", "quantity": 500, "unit": "ml"},
            {"name": "Zwiebel", "quantity": 1, "unit": "Stück"},
            {"name": "Knoblauch", "quantity": 2, "unit": "Zehen"},
            {"name": "Olivenöl", "quantity": 2, "unit": "EL"},
            {"name": "Salz", "quantity": 1, "unit": "Prise"},
            {"name": "Pfeffer", "quantity": 1, "unit": "Prise"}
        ],
        "servings": 4,
        "category": "Hauptgericht"
    },
    {
        "id": 2,
        "title": "Pfannkuchen",
        "ingredients": [
            {"name": "Mehl", "quantity": 200, "unit": "g"},
            {"name": "Milch", "quantity": 300, "unit": "ml"},
            {"name": "Eier", "quantity": 2, "unit": "Stück"},
            {"name": "Zucker", "quantity": 1, "unit": "EL"},
            {"name": "Butter", "quantity": 1, "unit": "EL"},
            {"name": "Salz", "quantity": 1, "unit": "Prise"}
        ],
        "servings": 3,
        "category": "Dessert"
    },
    {
        "id": 3,
        "title": "Caesar Salad",
        "ingredients": [
            {"name": "Römersalat", "quantity": 1, "unit": "Kopf"},
            {"name": "Hähnchenbrust", "quantity": 200, "unit": "g"},
            {"name": "Croutons", "quantity": 50, "unit": "g"},
            {"name": "Parmesan", "quantity": 30, "unit": "g"},
            {"name": "Caesar-Dressing", "quantity": 50, "unit": "ml"}
        ],
        "servings": 2,
        "category": "Salat"
    }
]


@app.route("/recipes/<int:id>")
def get_recipe_by_id(recipe_id):
    """Extracts a recipe by the given id"""
    specific_recipe = [recipe for recipe in recipe_list if recipe["id"] == recipe_id]  # The List comprehension gives
    # back a recipe if it corresponds to the given ID
    return specific_recipe


@app.route("/recipes/<int:title>")
def get_recipe_by_title(recipe_title):
    """Extracts a recipe by the given title"""
    return [recipe for recipe in recipe_list if recipe["title"] == recipe_title]


@app.route("/recipe_title")
def get_recipe_title(recipe):
    return recipe[0]["title"]


@app.route("/add_recipe", methods=["POST"])
def add_recipe(recipe, recipes):  # funktional
    new_recipe_list = recipes + recipe
    return new_recipe_list


# def add_recipe(recipe): #prozedural
#   recipe_list.append(recipe)

# def add_recipe(recipe): #Objekt orientiert
#   recipe_List.add_recipe(recipe)


def ingr_count(recipe):
    return len(recipe["ingredients"])


def most_ingredients():
    recipe_ingr_len = max([ingr_count(recipe) for recipe in recipe_list])
    return [recipe for recipe in recipe_list if len(recipe["ingredients"]) == recipe_ingr_len]


if __name__ == '__main__':
    print(get_recipe_by_id(2))
    print(get_recipe_title(get_recipe_by_id(1)))

    recipe_by_id = get_recipe_by_id
    print(recipe_by_id(2))

    ingr_count = list(map(ingr_count, recipe_list))

    ist_gerade = lambda x: x % 2 == 0
    print(ist_gerade(4))

    addieren = lambda x, y: x + y
    print(addieren(2, 3))

    kubik = lambda x, y, z: x * y * z
    print(kubik(2, 3, 2))
