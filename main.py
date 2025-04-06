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
        if isinstance(other, Smartphone):
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
        if isinstance(other, LawnGrass):
            return self.price + other.price
        raise TypeError


if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")
