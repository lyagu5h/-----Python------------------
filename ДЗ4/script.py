class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self) -> str:
        return f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}"
    
    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self.stock = quantity
        else:
            raise ValueError("Invalid quantity")

class Order:
    def __init__(self) -> None:
        self.products: dict = {}
    
    def add_product(self, product: Product, quantity: int) -> None:
        if product.stock >= quantity:
            product.update_stock(product.stock - quantity)
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity        
        else:
            raise ValueError("Not enough stock")

    def remove_product(self, product: Product, quantity: int) -> None:
        if product in self.products:
            if self.products[product] >= quantity:
                self.products[product] -= quantity
                if self.products[product] == 0:
                    del self.products[product]
                product.update_stock(product.stock + quantity)
            else:
                raise ValueError("Not enough products in order")

    def calculate_total(self) -> float:
        return sum(product.price * quantity for product, quantity in self.products.items())

    def return_product(self, product: Product, quantity: int) -> None:

        if product in self.products and self.products[product] >= quantity:
            self.products[product] -= quantity
            product.update_stock(product.stock + quantity)
            if self.products[product] == 0:
                del self.products[product]
        else:
            raise ValueError("Product not in order")

class Store:
    def __init__(self) -> None:
        self.products: list = []
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)
        
    def list_products(self) -> None:
        for product in self.products:
            print(product)
            
    def create_order(self) -> Order:
        return Order()

store = Store()

# Создаем товары
product1 = Product("Ноутбук", 1000, 5) # создаем экземпляр класса Product с названием "Ноутбук", ценой 1000 и остатком на складе 5
product2 = Product("Смартфон", 500, 10) #создаём экземпляр класса Product с названием "Смартфон", ценой 500 и остатком на складе 10

# Добавляем товары в магазин
store.add_product(product1) #добавляем первый товар в магазин
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




