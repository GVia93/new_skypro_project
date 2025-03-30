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
    assert len(category.product_list) == 3
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


def test_add_product(products):
    """
    Тестирует добавление продукта в категорию.
    """
    category = Category("Смартфоны", "Описание", products)
    new_product = Product("test", "test", 12345.0, 3)
    category.add_product(new_product)
    assert new_product in category.product_list
    assert category.product_count == 4


def test_new_product():
    """
    Тестирует создание продукта с использованием класса-метода new_product.
    """
    data = {"name": "test", "description": "test", "price": 12345.0, "quantity": 3}
    product = Product.new_product(data)
    assert product.name == "test"
    assert product.description == "test"
    assert product.price == 12345.0
    assert product.quantity == 3


def test_category_products_output(products):
    """
    Тестирует вывод списка продуктов категории.
    """
    category = Category("Смартфоны", "Описание", products)
    output = category.products
    for product in products:
        assert product.name in output
        assert str(product.price) in output
        assert str(product.quantity) in output


def test_product_price_setter():
    """
    Тестирует setter для price с проверкой валидации.
    """
    product = Product("test", "test", 12345.0, 3)
    product.price = 500.0
    assert product.price == 500.0
    product.price = 0
    assert product.price == 500.0
    product.price = -100


def test_add_product_invalid():
    """
    Тест добавления не корректного объекта.
    """
    category = Category(
        "test",
        "test",
        [],
    )
    with pytest.raises(TypeError, match="Не корректный объект"):
        category.add_product("test")
