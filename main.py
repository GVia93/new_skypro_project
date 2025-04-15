from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех товаров.
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Геттер для получения цены товара.
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """
        Сеттер для установки новой цены товара с валидацией.
        """
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other) -> float:
        pass


class InitLoggerMixin:
    """
    Миксин, логирующий создание объектов.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"{self.__class__.__name__} создан: {self.__repr__()}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.description!r}, {self.price!r}, {self.quantity!r})"


class Product(InitLoggerMixin, BaseProduct):
    """
    Класс товары.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Цена товара (приватный).
        quantity (int): Количество товара на складе.
        product_count (int): Счетчик созданных объектов Product.
    """

    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация экземпляра Product.
        """
        super().__init__(name, description, price, quantity)
        Product.product_count += 1

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создание нового продукта из словаря данных.

        data (dict): Словарь с данными товара.
        Product: Новый объект класса Product.
        """
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта с названием, ценой и количеством.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """
        Складывает общую стоимость двух продуктов (цена * количество каждого).
        """
        return self.price * self.quantity + other.price * other.quantity


class Category:
    """
    Класс категории товаров.

    Атрибуты:
        name (str): Название категории.
        description (str): Описание категории.
        __products (List[Product]): Список товаров в категории (приватный).
        category_count (int): Счетчик созданных объектов Category.
    """

    name: str
    description: str
    __products: list[Product]
    category_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        """
        Инициализация экземпляра Category.
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1

    @property
    def product_count(self) -> int:
        """
        Возвращает кол-во продуктов в категории.
        """
        return len(self.__products)

    def add_product(self, new_product: Product) -> None:
        """
        Добавляет новый продукт в категорию.
        """
        if not isinstance(new_product, Product):
            raise TypeError("Не корректный объект")
        self.__products.append(new_product)

    @property
    def products(self) -> str:
        """
        Возвращает строковое представление списка продуктов.
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def product_list(self) -> list[Product]:
        """
        Возвращает список объектов Product.
        """
        return self.__products

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории с названием и количеством.
        """
        return f"{self.name}, количество продуктов: {self.product_count} шт."


class Smartphone(Product):
    """Представляет товар категории Smartphone."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: float) -> float:
        """
        Складывает продукты класса Smartphone.
        """
        if type(other) is Smartphone:
            return self.price + other.price
        raise TypeError


class LawnGrass(Product):
    """Представляет товар категории LawnGrass."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: float) -> float:
        """
        Складывает продукты класса LawnGrass.
        """
        if type(other) is LawnGrass:
            return self.price + other.price
        raise TypeError


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
