#instance are bound methods
# get_val(self,newval) self indicates it is a instance method

class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self): #instnace method
        return self.val

    @classmethod #class method passes class instead of instance
    def get_count(cls):
        return InstanceCounter.count #count is a class attribute

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print ("val of obj: %s" % (obj.get_val())) ##initalized value of 5,13,etc
    print("count: %s" % (obj.get_count())) #we do not need to work with the instance always 3

print (InstanceCounter.get_count()) #can use class itself to call the method