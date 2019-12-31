#abstract classs is a kind of model for other classes to be defined
# it is not designed to construct instance but can be subclassed by regular classes

#abstract classes can definate an interface or methods that must be implemented by its subclass

import abc 

#python two implements abstract classes differently! in 2 you pass object as arugment and define __metaclass = abc.ABCMeta as the first variable
class GetterSetter(metaclass=abc.ABCMeta): #set the contract that must be implemented by other classes

    @abc.abstractmethod
    def set_val(self, input):
        return

    @abc.abstractmethod
    def get_val(self):
        return

class MyClass(GetterSetter): #here we implement the contract
    def set_val(self, input): #if you change set_val to set_valz we would error out 
        self.val = input
    def get_val(self):
        return self.val

x = MyClass()
print(x)

#x2=GetterSetter() #you cannot implement an abstract class throws error
#print(x2)