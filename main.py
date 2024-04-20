#Дополнительное задание:
#Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети
# имеет свои особенности, но также существуют общие характеристики, такие как адрес,
# название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет
# использовать для создания различных магазинов.

#Шаги:
#1. Создай класс Store:
#-Атрибуты класса:
#name: название магазина.
#address: адрес магазина.
#items: словарь, где ключ - название товара, а значение - его цена.
# Например, {'apples': 0.5, 'bananas': 0.75}.

#Методы класса:
#__init__ - конструктор, который инициализирует название и адрес, а также пустой
# словарь дляitems`.
#-  метод для добавления товара в ассортимент.
#метод для удаления товара из ассортимента.
#метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#метод для обновления цены товара.

#2. Создай несколько объектов класса Store:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый
# из них несколько товаров.

#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
# обнови цену, убери товар и запрашивай цену.
#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с
# реализацией задания.

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

    def info(self):
        print(f"Наименование магазина - {self.name}")
        print(f"адрес магазина - {self.address}")
        print(f"продукция - {self.items}")


store1 = Store(name="Десяточка", address="Москва, ул. Академика Королева, 12")
store2 = Store(name="Техника", address="Санкт-Петербург, ул. Глинянная, 1")
store3 = Store(name="Все для дачи", address="Ростов на Дону, ул. Речная, 5")

store1.add_item("яблоки", 180)
store1.add_item("молоко", 75)
store1.add_item("гречка", 140)
store1.add_item("печенье", 98)
store2.add_item("Пылесос", 15999)
store2.add_item("утюг", 2900)
store2.add_item("миксер", 6999)
store2.add_item("мультиварка", 25000)
store3.add_item("газонокосилка", 38999)
store3.add_item("шланг садовый", 1999)
store3.add_item("грабли", 2500)
store3.add_item("тачка", 6999)

store1.add_item("картошка", 199)
store1.add_item("масло", 240)
store1.update_price("яблоки", 165)
removed_price = store1.get_price("молоко")
store1.remove_item("молоко")
new_price_apples = store1.get_price("яблоки")
new_price_oranges = store1.get_price("картошка")
nonexistent_price = store1.get_price("молоко")

store1.info()
