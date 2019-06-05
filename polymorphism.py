# Inheritance in python

class Person:
    def __init__(self,name,mob_no,address):
        self.name = name
        self.mob_no = mob_no
        self.address = address

    def eat(self):
        print('I eat food')


class Employee(Person):
    def __init__(self,name,mob_no,address,company_name):
        Person.__init__(self,name,mob_no,address)
        self.company_name = company_name

    def eat(self):
        print('I eat healthy and lit food')



class Student(Person):
    def __init__(self,name,mob_no,address,school):
        Person.__init__(self,name,mob_no,address)
        self.school = school

    def eat(self):
        print('I eat spicy and junk food')




person = Person("Atishay Sharma" , 8899779988 , 'Indore')
student = Student("Rahul Rai",4565656665 , "Indore",school='NDPS')
employee = Employee("Priyanka" , 898989889 ,"Mhow", company_name='GWL')

for human in [person,student,employee]:
    human.eat()


