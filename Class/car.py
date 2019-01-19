class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        return str(self.year) + ' ' + self.make + ' ' + self.model
    
    def read_odometer(self):
        print('self.odometer_reading = ' + str(self.odometer_reading))
    
    def fill_gas_tank(self):
        print('油加满')