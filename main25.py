def bmi(height, weight):
    return weight / (height / 100) ** 2

class Person:
    name = None
    height = None
    weight = None
    def return_bmi(self):
        return self.weight / ( self.height / 100) ** 2
p1 = Person()
p1.name = "Elwing"
p1.height = 175
p1.weight = 75
print(p1.name, p1.return_bmi())

p2 = Person()
p2.name = "Bob"
p2.height = 180
p2.weight = 80
print(p2.name, p2.return_bmi())