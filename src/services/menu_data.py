from src.models.ingredient import Ingredient
from src.models.dish import Dish
import csv


# Requisito 3
class MenuData:
    def __init__(self, caminho: str) -> None:
        self.pratos_menu = {}

        with open(caminho, "r") as arquivo:
            for pratos in csv.DictReader(arquivo):
                preco_prato = pratos["dish"]
                if preco_prato not in self.pratos_menu:
                    self.pratos_menu[preco_prato] = Dish(
                        preco_prato, float(pratos["price"])
                    )

                self.pratos_menu[preco_prato].add_ingredient_dependency(
                    Ingredient(pratos["ingredient"]),
                    int(pratos["recipe_amount"]),
                )
        self.dishes = set(self.pratos_menu.values())
