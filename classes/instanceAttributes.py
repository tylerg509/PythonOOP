import random

class MyClass(object):
    def dothis(self):
        print('doing this')
        self.rand_val = random.randint(1,10)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)

#instnace attributes = state
#instance can accesss variables defined in the class
#instance can get and set values in itself
#values change according to what happens to the object so we call the values state