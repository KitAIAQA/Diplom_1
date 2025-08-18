import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    # Фикстура для создания мок-объекта булочки
    mock = MagicMock(spec=Bun)
    mock.get_name.return_value = "Mock Bun"
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_ingredient(request):
    # Фикстура для создания мок-объекта ингредиента
    # Получаем параметры из теста
    ingredient_type = request.param[0]
    name = request.param[1]
    price = request.param[2]

    mock = MagicMock(spec=Ingredient)
    mock.get_type.return_value = ingredient_type
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock





