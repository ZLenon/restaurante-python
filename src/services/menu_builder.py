from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Requisito 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        cardapio = []
        for pratos in self.menu_data.dishes:
            if restriction not in pratos.get_restrictions():
                # A função all() é usada para verificar se todos os valores
                # dentro do gerador são verdadeiros
                if all(
                    self.inventory.inventory.get(ingredient, 0) > 0
                    for ingredient in pratos.get_ingredients()
                ):
                    cardapio.append(
                        {
                            "restrictions": pratos.get_restrictions(),
                            "ingredients": pratos.get_ingredients(),
                            "dish_name": pratos.name,
                            "price": pratos.price,
                        }
                    )
        return cardapio
