class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print('%s is eating %s.' % (self.name,food))
class Dog(Animal):
    def fetch(self,thing):
        print ('% goes after the %s' % (self.name, thing))
class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string!' % (self.name))


r = Dog('rover')
f = Cat('fluffy')

r.eat('dog food')
f.swatstring()
r.eat('dog food')
f.eat('cat food')

#r.swatstring() #throws type error