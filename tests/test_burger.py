import pytest
from unittest.mock import patch, MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_bun(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_length(self, burger, sauce):
        burger.add_ingredient(sauce)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_content(self, burger, sauce):
        burger.add_ingredient(sauce)
        assert burger.ingredients[0] == sauce

    def test_remove_ingredient(self, burger, sauce):
        burger.add_ingredient(sauce)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_first_position(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == filling

    def test_move_ingredient_second_position(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == sauce

    @pytest.mark.parametrize("bun_price, ingredients_prices, expected_price", [
        (100, [50, 100], 350),
        (200, [100, 200, 300], 1000),
        (0, [0, 0], 0)
    ])
    def test_get_price(self, burger, bun_price, ingredients_prices, expected_price):
        mock_bun = MagicMock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredients_prices:
            mock_ingredient = MagicMock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt_success(self, burger, bun, sauce, filling):
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        expected_receipt = (
            "(==== Test Bun ====)\n"
            "= sauce Sauce =\n"
            "= filling Filling =\n"
            "(==== Test Bun ====)\n"
            '\n'
            "Price: 350"
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_error(self, burger, sauce, filling):
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        with pytest.raises(AttributeError):
            burger.get_receipt()
