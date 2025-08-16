from unittest.mock import MagicMock

def mock_bun():
    mock = MagicMock(spec=Bun)
    mock.get_name.return_value = "Mock Bun"
    mock.get_price.return_value = 100
    return mock

def mock_ingredient(ingredient_type, name, price):
    mock = MagicMock(spec=Ingredient)
    mock.get_type.return_value = ingredient_type
    mock.get_name.return_value = name
    mock.get_price.return_value = price
    return mock