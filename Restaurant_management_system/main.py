from Menu import Pizza, Burger, Drinks, Menu
from Restaurant import Restaurant
from Users import Chef, Customer, Server, Manager
from Order import Order

def main():
    menu = Menu()

    # add pizza to the menu
    pizza_1 = Pizza('Shutki Pizza', 6000, 'large', ['Shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('Alur bhorta Pizza', 4000, 'large', ['potato', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('Daal Pizza', 5000, 'large', ['Daal', 'onion'])
    menu.add_menu_item('pizza', pizza_3)
    
    # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('Beef burger', 2000, 'chicken', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 200, True)
    menu.add_menu_item('drinks', coke)
    coffee = Drinks('Espresso', 500, False)
    menu.add_menu_item('drinks', coffee)

    # show Menu
    menu.show_menu()

    restaurant = Restaurant('Sai Baba Restaurant', 2000, menu)
    
    # add manager to the restaurant
    manager = Manager('Kala Chan Manager', 875, 'kala@chan.com', 'kaliganj', 1000, 'Jan 1 2020', 'core')
    restaurant.add_employee('manager', manager)

    chef = Chef('Rustom Baburchi', 7865, 'chupa@rustom.com', 'rustom nagar', 1500, 'Feb 1 2020', 'chef', 'All Item')
    restaurant.add_employee('chef', chef)
    server = Server('Chotu', 876, 'chotu@email.com', 'Sai baba', 200, 'Feb 1 2020', 'Server')
    restaurant.add_employee('server', server)

    # show employee
    restaurant.show_employees()

    # customer_1 placing an order
    customer_1 = Customer('Sakib', 20000, 3425, 'sakib@khan.com', 'bababa')
    order_1 = Order(customer_1, [pizza_3, pizza_1, coke, coffee])
    # customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer_1 paying for order_1
    restaurant.receive_payment(order_1, 50000, customer_1)
    print('Revenue and Balanace after first customer', restaurant.revenue, restaurant.balance)

    customer_2 = Customer('rohim', 100000, 3425, 'rohim@khan.com', 'mamama')
    order_2 = Order(customer_2, [pizza_2, burger_1, coke])
    # customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    # customer_2 paying for order_2
    restaurant.receive_payment(order_2, 60000, customer_2)
    print('Revenue and Balanace after Second customer', restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('After rent', restaurant.revenue, restaurant.balance, restaurant.expense)

    # pay salary
    restaurant.pay_salary(chef)
    print('After salary', restaurant.revenue, restaurant.balance, restaurant.expense)

# a way to call the main but we can easily call main()
if __name__ == '__main__':
    main()