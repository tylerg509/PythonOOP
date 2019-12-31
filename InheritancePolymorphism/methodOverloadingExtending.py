
import abc

#classes that enherit can take functionality of getsetparent or modify and implment their own get set methods
#show doc is the only required method
class GetSetParent(metaclass=abc.ABCMeta):
    def __init__(self,value):
        self.val = 0
    def set_val(self,value):
        self.val = value
    def get_val(self):
        return self.val
    
    @abc.abstractmethod
    def showdoc(self):
        return #abstract class dont do anyhthing they just return at the end

#inherit from getsetparent
class GetSetInt(GetSetParent):
    def set_val(self, value):
        #if value is not int set to 0
        if not isinstance(value, int):
            value = 0
        #look for super class and pass value to set val
        #called specializing 
        super(GetSetInt, self).set_val(value)
    def showdoc(self):
        print('getsetint object ({0}), only accepts '
            'int values'.format(id(self)))

#store values in list to get a history
#polymorphic and #specialization
#override every method of getsetparent
class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self,value):
        self.vallist.append(value)
    def showdoc(self):
        print('getsetlist object, len {0} stores'
            'history of values set'.format(len(self.vallist)))


x = GetSetInt(3)
x.set_val(5)
print(x.get_val())
x.showdoc()


gsl = GetSetList()
gsl.set_val(10)
gsl.set_val(20)
print(gsl.get_val())
print(gsl.get_vals())
gsl.showdoc()

#ways to implement a parent classs
#inherit: use parent class defined method
#override/overload: provide childs own version of a metehod
#extend: do work in addition to parents method
#provide: implement abstract method that parent requires