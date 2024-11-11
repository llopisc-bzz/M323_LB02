import sqlite3
from recipeItem import Recipe


class RecipeDao:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def create_recipe_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS recipes""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, title TEXT, ingredients LIST, servings INTEGER, category TEXT)""")
        self.conn.commit()

    def add_recipe(self, recipe):
        self.cursor.execute("INSERT INTO recipes (title, ingredients, servings, category) VALUES (?, ?, ?, ?)",
                            (recipe.title, recipe.ingredients, recipe.servings, recipe.catergory),)
        self.conn.commit()

    def get_recipe_by_id(self, id):
        self.cursor.execute("SELECT * FROM recipe WHERE id = ?", (id,))

