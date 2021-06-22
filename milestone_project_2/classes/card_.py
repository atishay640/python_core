'''
A Card from the deck

'''

class Card:
    def __init__(self, name, points,color,category ):
        self.name = name
        self.points = points
        self.color = color
        self.category = category

    def __str__(self):
        result = ' name = {}, points = {}, color = {}, category = {}'.format(self.name,self.points,self.color,self.category)
        return result





