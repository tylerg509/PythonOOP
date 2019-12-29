
class MyClass(object):
    var = 10

this_obj = MyClass()

print (this_obj)

that_obj = MyClass()

print(that_obj)

print (this_obj.var)
print (that_obj.var)

#an instance of a class knows what class its from
#variables defined in the class are available to the instance