class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print('battery_size = ' + str(self.battery_size))


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        return str(self.year) + ' ' + self.make + ' ' + self.model
    
    def read_odometer(self):
        print('self.odometer_reading = ' + self.odometer_reading)
    
    def fill_gas_tank(self):
        print('油加满')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()
    
    def describe_battery(self):
        print('This Car has a ' + str(self.battery_size) + '-KWh battery.')
    
    def fill_gas_tank(self):
        print('我不需要油，我要电')


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# Battery().describe_battery()