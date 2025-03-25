import pytest

from main import Category, Product


@pytest.fixture
def products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


def test_init_product(products):
    """
    Тестирует корректность инициализации объектов класса Product.
    """
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[1].price == 210000.0
    assert products[2].quantity == 14


def test_product_count(products):
    """
    Тестирует подсчет количества продуктов.
    """
    start_count = Product.product_count
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert Product.product_count == start_count + 1


def test_init_category(products):
    """
    Тестирует корректность инициализации объектов класса Category.
    """
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products,
    )
    assert category.name == "Смартфоны"
    assert len(category.products) == 3
    assert category.description.startswith("Смартфоны, как средство")


def test_category_count():
    """
    Тестирует подсчет количества категорий.
    """
    start_count = Category.category_count
    Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [],
    )
    assert Category.category_count == start_count + 1
