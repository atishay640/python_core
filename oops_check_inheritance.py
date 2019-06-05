'''
Check inheritance
'''

class Car:
    def __init__(self,name,model_no , colour , segment , fuel_type , seating ):
        self.name = name
        self.model_no = model_no
        self.colour = colour
        self.segment = segment
        self.fuel_type = fuel_type
        self.seating = seating

    def start(self):
        print('Car Started')

    def get_name(self):
        print(self.name)


class SportCar(Car):
    def __init__(self,name,model_no , colour , segment , fuel_type , seating , air_quality_control , power_steering, power_window, navigation_system,usb_charger):
        Car.__init__(self,name,model_no , colour , segment , fuel_type , seating )
        self.air_quality_control = air_quality_control
        self.power_steering = power_steering
        self.power_window =power_window
        self.navigation_system = navigation_system
        self.usb_charger = usb_charger

    def start(self):
        print('SportCar Started')




maruti_swift = SportCar('Swift','ZDI-Plus','Blue','Hatchback','Diesel',5,False,True,True,True,False)
maruti_swift.get_name()
maruti_swift.start()

maruti_alto = Car('Alto','800','White','Entry-level','Petrol','4')

print(issubclass(Car,SportCar))
print(isinstance(maruti_swift,SportCar))
print(isinstance(maruti_swift,Car))

print(issubclass(SportCar,Car))
print(isinstance(maruti_alto,SportCar))
print(isinstance(maruti_alto,Car))







