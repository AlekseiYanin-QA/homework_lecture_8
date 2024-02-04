"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(500)
        assert not product.check_quantity(1500)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(200)
        assert product.quantity == 800

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1100)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 10)
        assert product in cart.products
        assert cart.products[product] == 10

    def test_remove_product(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product, 8)
        assert cart.products[product] == 2

    def test_remove_product_completely(self, cart, product):
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, cart, product):
        cart.add_product(product, 10)
        cart.clear()
        assert not cart.products

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 10)
        expected_total = 10 * product.price
        assert cart.get_total_price() == expected_total

    def test_buy_success(self, cart, product):
        cart.add_product(product, 1)
        cart.buy()
        assert product.quantity == 999

    def test_buy_error(self, product, cart):
        cart.add_product(Product("headphones", 100, "This is headphones", 2),
                         5)
        with pytest.raises(ValueError):
            cart.buy()
