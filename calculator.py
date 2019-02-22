class Calculator:
    def multiply(x,y):return x*y
    def divide(x,y):return x/y
    def add(x,y): return x+y
    def substract(x,y): return x-y
    def power(x,y): return x**y
    def root(x): return x**(1/2)
class LinearEq:
    def slope(x,y,b):
	return:(y-b)/x
    def x(m,y,b):
	return:(y-b)/m
    def y(m,x,b)
	return:m*x+b
    def b(m,x,y):
	return: y-m*x

x=LinearEq.slope(10,20,3)
x    

class Person:
    def __init__(self, name):
        self.name = name
        self.surname = surname
        
 
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
 
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
 
        return age
x=Person.name('Dan')