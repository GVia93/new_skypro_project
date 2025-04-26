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
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")
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

    def middle_price(self) -> float:
        """
        Подсчитывает средний ценник всех товаров.
        Если товаров нет возвращает 0.0
        """
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0.0

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


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
