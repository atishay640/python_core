# Inheritance in python

class Person:
    def __init__(self,name,mob_no,address):
        self.name = name
        self.mob_no = mob_no
        self.address = address


class Employee(Person):
    def __init__(self,name,mob_no,address,company_name):
        Person.__init__(self,name,mob_no,address)
        self.company_name = company_name



class Student(Person):
    def __init__(self):
        Person.__init__(self,name,mob_no,address)
        self.company_name = company_name


atishay = Employee(name='Atishay Sharma' , mob_no=9856895689 , address= '107 SunShine', company_name='GWL')
print(atishay.mob_no)
