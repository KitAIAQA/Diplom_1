import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def bun():
    return Bun("Test Bun", 100)

@pytest.fixture
def sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "Sauce", 50)

@pytest.fixture
def filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "Filling", 100)