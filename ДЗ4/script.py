class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock
    
    def __hash__(self) -> int:
        return hash((self._name, self._price, self._stock))
    
    def __eq__(self, other: object) -> int:
        if not isinstance(other, Product):
            return False
        return self._name == other._name and self._price == other._price and self._stock == other._stock

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._stock = quantity
    


class Store:
    def __init__(self, products: list['Product'] | None = None) -> None:
        self._products = products or []

    def __hash__(self) -> int:
        return hash(self._products)

    @property
    def products(self) -> list['Product']:
        return self._products

    def list_products(self) -> None:
        for product in self._products:
            print(product.name, product.price, product.stock)

    def add_product(self, product: 'Product') -> None:
        self._products.append(product)

    def create_order(self) -> 'Order':
        return Order(self)

class Order:
    def __init__(self, store: 'Store') -> None:
        self._products: dict[Product, int] = {}
        self._store = store

    def __hash__(self) -> int:
        return hash(self._products)
    
    @property
    def products(self) -> dict[Product, int]:
        return self._products
    
    @property
    def store(self) -> 'Store': 
        return self._store

    def add_product(self, product: Product, quantity: int) -> None:
        if product in self._store.products:
            if quantity < 0:
                raise ValueError("Количество не может быть отрицательным")
            if quantity > product.stock:
                raise ValueError("Недостаточно товара на складе")
            product.update_stock(product.stock - quantity)
            if product not in self._products:
                self._products[product] = quantity
            else:
                self._products[product] += quantity
        else:
            raise ValueError("Такого продукта нет в магазине")
        
    def calculate_total(self) -> float:
        total = 0
        for product, quantity in self._products.items():
            total += product.price * quantity
        return total
    
    def remove_product(self, product: Product, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        if product in self._products and self._products[product] >= quantity:
            product.update_stock(product.stock + quantity)
            self._products[product] -= quantity
            if self._products[product] == 0:
                del self._products[product]
    
    def return_product(self, product: Product) -> None:
        if product in self._products:
            product.update_stock(product.stock + self._products[product])
            del self._products[product]


store = Store()
# Создаем товары
product1 = Product("Ноутбук", 1000, 5) # создаем экземпляр класса Product с названием "Ноутбук", ценой 1000 и остатком на складе 5
product2 = Product("Смартфон", 500, 10) #создаём экземпляр класса Product с названием "Смартфон", ценой 500 и остатком на складе 10

# store = Store(products=[product1]) #создаем экземпляр класса Store с списком продуктов
# Добавляем товары в магазин
store.add_product(product1) #добавляем второй товар в магазин
store.add_product(product2) #добавляем второй товар в магазин

# Список всех товаров
store.list_products() #выводим список всех товаров

# Создаем заказ
order = store.create_order() #создаем экземпляр класса Order

# Добавляем товары в заказ
order.add_product(product1, 2)
order.add_product(product2, 3)

# Выводим общую стоимость заказа
total = order.calculate_total()
print(f"Общая стоимость заказа: {total}")

# Проверяем остатки на складе после заказа
store.list_products()




