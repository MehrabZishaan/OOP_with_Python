class Person:
    id_counter = 100
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.user_id = Person.generate_id()

    @classmethod
    def generate_id(self):
        id = self.id_counter
        self.id_counter += 1
        return id

    def __repr__(self):
        return f"Email: {self.email} \nUser_id: {self.user_id}"

class Store:
    def __init__(self):
        self.total_products = {}

    def add_product(self, seller_id, product):
        # print(seller_id)
        productDict = vars(product)
        if seller_id not in self.total_products:
            self.total_products[seller_id] = []

            seller_info = {}
            seller_info["total_sell_product"] = 0
            seller_info["total_sell_amount"] = 0
            seller_info["total_profit_amount"] = 0

            self.total_products[seller_id].append(seller_info)

        self.total_products[seller_id].append(productDict)


class Owner(Person):
    def __init__(self, email, password):
        self.total_sell_products = 0
        self.total_sell_amount = 0
        self.total_profit_amount = 0
        super().__init__(email, password)

    def shop_info(self, store):
        all_seller_id = store.total_products.keys()
        for seller_id in all_seller_id:
            sell_info = store.total_products[seller_id][0]
            # print(sell_info)
            self.total_sell_products += sell_info["total_sell_product"]
            self.total_sell_amount += sell_info["total_sell_amount"]
            self.total_profit_amount += sell_info["total_profit_amount"]

        sell_info = {
            "Total_sell_products": self.total_sell_products,
            "Total_sell_amount": self.total_sell_amount,
            "Total_profit_amount": self.total_profit_amount
        }
        return sell_info

class Seller(Person):
    def __init__(self, email, password):
        super().__init__(email, password)

    def add_product(self, store, product_name, product_price, product_quantity):
        product = Product(product_name, product_price, product_quantity)
        store.add_product(self.user_id, product)

class Product:
    def __init__(self, name, price, quantity):
        self.name = name;
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product name: {self.name} || Product price: {self.price} || Product Quantity: {self.quantity}"

    def sell_info(self, store):
        print(store.total_products[self.user_id][0])



class Customer(Person):
    def __init__(self, email, password):
        self.total_buy_amount = 0
        self.total_buy_products = 0
        super().__init__(email, password)

    def show_products(self,store):
        # print(store.total_products)
        all_seller_keys = store.total_products.keys()
        for seller_id in all_seller_keys:
            print("Seller_id: ", seller_id)
            print("=================================================")
            for index in range(1, len(store.total_products[seller_id])):
                product = store.total_products[seller_id][index]
                print("Name: ", product["name"], "Price: ", product["price"], "Quantity: ", product["quantity"])

    def buy_products(self, store, seller_id, product_name, quantity):
        for index in range(1, len(store.total_products[seller_id])):
            product = store.total_products[seller_id][index]
            if product["name"] == product_name:
                if quantity <= product["quantity"]:
                    product["quantity"] -= quantity
                    self.total_buy_products += quantity
                    self.total_buy_amount += quantity * product["price"]

                    seller = store.total_products[seller_id][0]
                    seller["total_sell_product"] += quantity
                    seller["total_sell_amount"] += quantity * product["price"]
                    seller["total_profit_amount"] += (quantity * product["price"])/10

                else:
                    print("Insufficient product quantity")

            else:
                print("No product found as", product_name )

store = Store()

seller1 = Seller("seller1@g.com", 1234)
seller2 = Seller("seller2@g.com", 1235)
seller3 = Seller("seller3@g.com", 1245)

seller1.add_product(store, "iphone10", 150, 10)
seller1.add_product(store, "iphone11", 200, 11)

seller2.add_product(store, "iphone12", 100, 20)
seller2.add_product(store, "iphone13", 150, 13)

seller3.add_product(store, "iphone9", 200, 9)
seller3.add_product(store, "iphone14", 250, 14)

print(store.total_products)

customer1 = Customer("customer1@g.com", 3456)
print(customer1.total_buy_amount, customer1.total_buy_products)
customer1.show_products(store)

customer1.buy_products(store, 100, "iphone10", 4)
customer1.buy_products(store, 101, "iphone13", 5)
customer1.buy_products(store, 102, "iphone14", 7)

customer1.show_products(store)
print(store.total_products)
print(customer1.total_buy_amount, customer1.total_buy_products)

seller1.sell_info(store)

owner = Owner("owner@admin.com", 7890)

print(owner.shop_info(store))