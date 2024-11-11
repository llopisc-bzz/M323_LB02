from dataclasses import dataclass


@dataclass
class Recipe:
    id: int
    title: str
    ingredients: list
    servings: int
    catergory: str
