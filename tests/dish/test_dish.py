from src.models.dish import Dish
from src.models.ingredient import Restriction, Ingredient
import pytest


# Requisito 2
def test_dish():
    pizza = Dish("pizza", 39.90)
    fanta = Dish("fanta", 8.09)
    queijo = Dish("gorgonzola", 198)
    presunto = Ingredient("presunto")

    assert pizza.name == "pizza"
    assert fanta.name == "fanta"
    assert queijo.name == "gorgonzola"

    assert pizza != queijo
    assert fanta == fanta

    assert queijo.price == 198
    assert fanta.price == 8.09

    assert hash(fanta) != hash(pizza)
    assert hash(pizza) == hash(pizza)

    assert repr(queijo) == "Dish('gorgonzola', R$198.00)"

    # Adiciona um ingrediente ao ao produto
    pizza.add_ingredient_dependency(presunto, 1)

    # Verifica se ingrediente está no produto
    assert presunto in pizza.get_ingredients()

    assert Restriction.ANIMAL_DERIVED in pizza.get_restrictions()

    with pytest.raises(ValueError):
        Dish("dolly", -6)
