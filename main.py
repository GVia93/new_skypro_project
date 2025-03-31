class Product:
    """
    Класс товары.

    Атрибуты:
        name (str): Название товара.
        description (str): Описание товара.
        __price (float): Цена товара (приватный).
        quantity (int): Количество товара на складе.
        product_count (int): Счетчик созданных объектов Product.
    """

    name: str
    description: str
    __price: float
    quantity: int
    product_count: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Инициализация экземпляра Product.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.product_count += 1

    @classmethod
    def new_product(cls, data: dict) -> "Product":
        """
        Создание нового продукта из словаря данных.

        data (dict): Словарь с данными товара.
        Product: Новый объект класса Product.
        """
        return cls(name=data["name"], description=data["description"], price=data["price"], quantity=data["quantity"])

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

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта с названием, ценой и количеством.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> float:
        """
        Складывает общую стоимость двух продуктов (цена * количество каждого).
        """
        return self.__price * self.quantity + other.__price * other.quantity


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


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
