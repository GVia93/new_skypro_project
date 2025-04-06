import pytest

from main import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def category(products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products,
    )


def test_category_str(category):
    """
    Тестирует строковое представление объекта Category.
    """
    expected = "Смартфоны, количество продуктов: 3 шт."
    assert str(category) == expected


def test_product_str(products):
    """
    Тестирует строковое представление объекта Products.
    """
    expected = "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert str(products[1]) == expected


def test_product_add(products):
    """
    Тестирует оператор сложения для объектов Product.
    """
    result = products[1] + products[2]
    assert result == 2114000.0


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


def test_init_category(products, category):
    """
    Тестирует корректность инициализации объектов класса Category.
    """
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


def test_add_product(products, category):
    """
    Тестирует добавление продукта в категорию.
    """
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


def test_category_products_output(products, category):
    """
    Тестирует вывод списка продуктов категории.
    """
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


def test_add_product_invalid(category):
    """
    Тест добавления не корректного объекта.
    """
    with pytest.raises(TypeError, match="Не корректный объект"):
        category.add_product("test")


def test_smartphone_attribute():
    """ Тестирует корректность атрибутов класса Smartphone. """
    smartphone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawngrass_attribute():
    """ Тестирует корректность атрибутов класса LawnGrass. """
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0,
                      20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава для газона"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_invalid_sum():
    """
    Тестирует, что при сложении Smartphone и LawnGrass вызывается исключение TypeError.
    """
    smartphone1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = smartphone1 + grass1

def test_smartphone_addition_invalid():
    """
    Тестирует сложение Smartphone с другим типом вызывается TypeError.
    """
    smartphone1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    with pytest.raises(TypeError):
        _ = smartphone1 + "Not a product"


def test_lawngrass_addition_invalid():
    """
    Тестирует сложение LawnGrass с другим типом вызывается TypeError.
    """
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        _ = grass1 + "Not a product"
