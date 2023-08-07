from src.models.ingredient import Restriction, Ingredient


# Req 1
def test_ingredient():
    # difinindo ingredientes aleatorios da classe ingrediente
    cheese_one = Ingredient("queijo parmesão")
    cheese_extra = Ingredient("queijo parmesão")
    cheese_two = Ingredient("queijo provolone")
    cheese_three = Ingredient("queijo mussarela")

    # o método mágico __hash__ funcione como esperado.
    assert hash(cheese_one) == hash(cheese_extra)
    assert hash(cheese_one) != hash(cheese_two)
    assert cheese_three != cheese_two
    assert cheese_one == cheese_extra
    assert cheese_two.name == "queijo provolone"

    # o método mágico __repr__ funcione como esperado
    assert repr(cheese_extra) == "Ingredient('queijo parmesão')"

    # Conjuntos de ingredientes
    assert Ingredient("queijo gorgonzola").restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert Ingredient("massa de ravioli").restrictions != {
        Restriction.ANIMAL_DERIVED,
        Restriction.SEAFOOD,
    }
