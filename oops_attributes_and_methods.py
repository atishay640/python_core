# class in python



class Student:

    # self : is the object of Student class
    # roll_num, name : are method parameters
    def __init__(self,roll_num,name):

        # roll_no, name : are class attributes
        self.roll_no = roll_num
        self.name = name


# Test custom class student

atishay = Student(roll_num=101,name='Atishay Sharma')
print(atishay.name)
print(atishay.roll_no)
print('--------------------------------------------------------')

class Percentage:

    def __init__(self,number , percent):
        self.number = number
        self.percent = percent


    def calculate(self):
        return self.number*self.percent/100


five_percent_of_569 = Percentage(1659,5)
print(five_percent_of_569.calculate())

print('--------------------------------------------------------')

class MySets:
    def __init__(self,*args):
        self.num_list = args

    def mean(self):
        sum = 0
        for num in self.num_list:
            sum+=num
        return sum/len(self.num_list)

    def median(self):
        num_count = len(self.num_list)
        if num_count%2 == 0:
            m1 = int(num_count/2 - 1)
            m2 = int(num_count/2)
            return (self.num_list[m1],self.num_list[m2])

        elif num_count%2 == 1:
            return self.num_list[int(num_count/2)]


student_marks = MySets(1,2,3,4,5,6,7,8,9)
mean = student_marks.mean()
median = student_marks.median()
print(mean)
print(median)

