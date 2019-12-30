
import random 

#initalize through parent class contsturctor and then through the child class constructor
class Animal(object):
    def __init__(self, name):
        self.name = name
        
class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name) #first thing is we call super - get super class of dog and pass the dog instance to whatever method we say
        self.breed = random.choice(['shih tzu', 'beagle', 'corgi'])
    def fetch(self,thing):
        print ('% goes after the %s' % (self.name, thing))

d = Dog('rover')

print(d.name)
print(d.breed)

#we call animal.init with the dog instance

# get super class of dog 
#we could to animal.init with the dog object
#its better to do it as we did 
#we can now rearrachge class hierarchy  so that dog inherits from another classs first and we prefer to call that constructor instead
#we can change the animal class name
#usimg super in this case allows us to keep things modular
#use general init functionality (animal has name) with more specific init functionality (dog breed)
#we want dog to have name and we want dog to set its own breed


#__init__ is like another other method it can be inherited
#if a class does not have __init__ constructor python will check its parent class to see if it can find one
#as soon as it finds one python calls it and stops looking
#we can use super() function to call methods in the parent class
#we may want to initalize in the parent as well as our own classs