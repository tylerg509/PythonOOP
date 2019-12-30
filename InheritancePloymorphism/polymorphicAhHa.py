
var = 'hello'

print(len(var))
print(var.__len__())


#built in functions 
#when we use built in functions they translate to method calls on the object being passed
#len is a method of the string object

print(dir(var)) ##these are all the attributes (many are methods for the string object) available to strings


print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#len is also implemented for arrays dictionary etc
arr = [1,2,3]
print(len(arr))
print(arr.__len__())
print(dir(arr))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
dir({'a':1}) #len also implemented on dictionaries 

#len is polymorhpic
# plus sign is polymorphic
