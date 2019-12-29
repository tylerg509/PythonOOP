
class InstanceCounter(object):
    count = 0

    def __init__(self,val):
        self.val = val
        InstanceCounter.count +=1 #count is a global variable so we need to use instancecounter.count to get the val
    def set_val(self,newval):
        self.val = newval
    def get_val(self):
        return self.val
    def get_count(self): #class data = counts the number of times initalized below
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print("val of obj: %s" % (obj.get_val())) #each instance has access to its own data
    print("count: %s" % (obj.get_count())) #each instance has access to the class data 
    print("count: %s" % (obj.count)) #this is the same as the previous but we access it through the instance instead of the class

d=InstanceCounter(1)
print(d.get_count())

e=InstanceCounter(1)
print(e.get_count())




print(InstanceCounter)
print(dir(InstanceCounter))