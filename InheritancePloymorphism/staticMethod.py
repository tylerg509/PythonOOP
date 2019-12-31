#instance are bound methods
# get_val(self,newval) self indicates it is a instance method

class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = self.fitlerint(val)
        InstanceCounter.count += 1

#utility method that is not a class or instance method. self is not passed and instance is not being passed
#static method does not require instance
#static method belongs in class becuse class uses it
    @staticmethod 
    def fitlerint(value):
        if not isinstance(value,int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('sdf')


print(a.val)
print(b.val)
print(c.val)