# Bus ticket booking system

""" Admin
1) Add a new Bus
2) Check available Bus
3) Can check bus info

User
1) Check available buses
2) Can check bus info
3) Can reserve seat """

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Bus:
    def __init__(self, coach, driver, arrival, departure, from_des, to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ['Empty' for i in range(20)]

class Unique:
    total_bus = 5
    total_bus_list = []
    
    def add_bus(self):
        bus_no = int(input('Enter Bus no: '))

        flag = 1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print('Bus already added')
                flag = 0
                break
        if flag:
            bus_driver = input('Enter Bus driver name: ')
            bus_arrival = input('Enter Bus arrival time: ')
            bus_departure = input('Enter Bus departure time: ')
            bus_from = input('Enter Bus start from: ')
            bus_to = input('Enter Bus destination: ')
            self.new_bus = Bus(bus_no, bus_driver, bus_arrival, bus_departure, bus_from, bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print('Bus added successfully')

class Counter(Unique):
    def __init__(self):
        super().__init__()
    
    user_lst = []

    def reservation(self):
        bus_no = int (input('Enter Bus no: '))

        for w in self.total_bus_list:
            if bus_no == w['coach']:
                passenger = input('Enter your name: ')
                seat_no = int(input('Enter Seat no: '))
                if seat_no > 20:
                    print('Invalid Seat Number')
                elif w['seat'][seat_no - 1] != 'Empty':
                    print('Seat Already Booked')
                else:
                    w['seat'][seat_no - 1] = passenger
                    print("Successfully Booked")
            else:
                print('No Bus Available')
        # for bus in self.total_bus_list:
        #     print(bus['seat'])

    def show_reservation(self):
        bus_no = int(input('Enter the coach number: '))
        for bus in self.total_bus_list:
            if bus_no == bus['coach']:
                print('*'*50)
                print()
                print(f"{' '*10}{'#'*10} BUS INFO {'#'*10}")
                print(f"Coach Number: {bus_no}\t\t\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t\t To: {bus['to']}")
                print()

                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end = "\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}", end = "\t")
                        a += 1
                    print()
                print('*'*50)

    def get_users(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        self.new_user = User(name, password)
        self.user_lst.append(vars(self.new_user))

    def available_buses(self):
        if len(self.total_bus_list) == 0:
            print("No Bus Available")
        else:
            print("*"*50)
            for bus in self.total_bus_list:
                print()
                print(f"{' '*10}{'#'*10} BUS {bus['coach']} INFO {'#'*10}")
                print(f"Coach Number: {bus['coach']} \t\t\t Driver: {bus['driver']}")
                print(f"Arrival: {bus['arrival']} \t\t\t Departure: {bus['departure']}")
                print(f"From: {bus['from_des']} \t\t\t To: {bus['to']}")
            print("*"*50)

while True:
    company = Unique()
    b = Counter()
    print("1. Create an account\n2. Login to your account\n3.Exit")

    user_input = int(input("Enter your choice: "))
    if user_input == 3:
        break
    elif user_input == 1:
        b.create_account()
    elif user_input == 2:
        name = input("Enter your username: ")
        password = input("Enter your password: ")

        flag = 0
        isAdmin = False

        if name == "admin" and password == "123":
            isAdmin = True
        if isAdmin == False:
            for user in b.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"\n{' '*10}Welcome to Unique Bus Ticket Booking System")
                    print("1. Available Buses \n2. Show bus info \n3. Reservation \n4. Exit")
                    x = int(input("Enter your choice: "))
                    if x == 4:
                        break
                    elif x == 1:
                        b.available_buses()
                    elif x == 2:
                        b.show_reservation()
                    elif x == 3:
                        b.reservation()
            else:
                print("Invalid User")
        else:
            while True:
                print(f"{' '*10}Hello Admin, Welcome to Bus Ticket Booking System")
                print("1. Add Buses \n2. Available Buses \n3. Show bus info \n4. Exit")
                x = int(input("Enter your choice: "))
                if x == 4:
                    break
                elif x == 1:
                    b.add_bus()
                elif x == 2:
                    b.available_buses()
                elif x == 3:
                    b.show_reservation()








    

# ena = Bus(2, 'Rahim', '12PM', '12:30PM', 'DHK', 'CTG')
# vars diye print korar fole sob instance key & value hoye dictionary hoye print hoise
# print(vars(ena))
# company = Unique()
# company.add_bus()
# c = Counter()
# c.reservation()