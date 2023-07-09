# shop management

class Product:
    def __init__(self, name, price, quantity):
        self.product_name = name
        self.product_price = price
        self.product_quantity = quantity

class Store:
    def __init__(self):
        self.__products_price = {} # name ar price rakhbo ei dictioanary te
        self.__products_quantity = {} # name ar quantity rakhbo ei dictionary te
        self.__profit = 0

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.__products_price[product.product_name] = product.product_price
        self.__products_quantity[product.product_name] = product.product_quantity

    def buy_product(self, name, quantity):
        if name in self.__products_price:
            if self.__products_quantity[name] >= quantity:
                print(f'In stock {name}')

                # 5% profit calculation korlam
                profit = 5 * self.__products_price[name] * quantity / 100
                self.__profit += profit
                print(f'Profit after selling {name} x {quantity}: {profit}')
                
                # after selling deduct the stock
                self.__products_quantity[name] = self.__products_quantity[name] - quantity
                print(f'Now available {name}: {self.__products_quantity[name]}')
                
            else:
                print(f'Not enough stock {name}')
        else:
            print(f'Not in stock {name}')

    def show_products(self):
        print('All products price', self.__products_price)
        print('All products quantity', self.__products_quantity)

    def show_profit(self):
        print(f'Total profit = {self.__profit}')

class Shop(Store):
    def __init__(self, name):
        self.shop_name = name
        super().__init__()

shop1 = Shop('GADGET & GEAR')
shop1.add_product('iphoneX', 80000, 12)
shop1.add_product("Samsung S9", 70000, 22)

shop1.show_products()
shop1.buy_product('iphoneX', 2)
shop1.show_products()
shop1.buy_product('Samsung S9', 5)
shop1.show_profit()