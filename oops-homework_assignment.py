# line
# P (x1,y1) and Q(x2,y2)
# cylinder

import math

class TheLine:

    def __init__(self,P , Q):
        self.P = P
        self.Q = Q

    def distance(self):
        y1 = self.P[1]
        x1 = self.P[0]

        y2 = self.Q[1]
        x2 = self.Q[0]

        return math.sqrt((x2-x1)**2 + (y2-y1)**2)



    def slope(self):
        y1 = self.P[1]
        x1 = self.P[0]

        y2 = self.Q[1]
        x2 = self.Q[0]

        return ((y2-y1)/(x2-x1))



aline = TheLine((3,2),(8,10))

print(aline.distance())
print(aline.slope())


class Cylinder:
    pie = 3.14
    def __init__(self , height = 1 , radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        return (self.pie * ((self.radius)**2 )* self.height)

    def surface_area(self):
        return  (2 * self.pie * (self.radius)* self.height) + 2*(self.pie * ((self.radius)**2 ))


tank = Cylinder( 2 ,3)
print(tank.volume())
print(tank.surface_area())

