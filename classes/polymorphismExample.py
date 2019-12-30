class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self,food):
        print('{0} eats {1}'.format(self.name,food))
class Dog(Animal):
    def fetch(self,thing):
        print ('{0} goes after the {1}'.format(self.name, thing))
    def show_affection(self):
        print ('{0} wags tail'.format(self.name))
class Cat(Animal):
    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))
    def show_affection(self):
        print('{0} purrs'.format(self.name))

for a in (Dog('Rover'),Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()

#polymorphism in python just means defining the same methods within classes that share the same parent class
#here dog and cat are both inheriting animal. the code is polymorphic because show affection is defined in dog and cat
#and dog and cat share the same parent class

#ducking = we dont care what type of animal we have. we can call show afffection on any type of animal
#the interface contract we define says that show affect will be available for each animal