import pickle

class MyClass(object):
    def __init__(self,init_val):
        self.val= init_val
    def increment(self):
        self.val +=1

cc = MyClass(5)
cc.increment()
cc.increment()

with open('d.txt', 'wb') as fh:
    pickle.dump(cc, fh)

with open('d.txt', 'rb') as fh:
    unpickled_cc = pickle.load(fh)


print(unpickled_cc)
print(unpickled_cc.val)

#PICKLE DOES NOT STORE CODE
#when you unpickle the class must be available 
#does not store classes, modules or funcitons but can refer to them