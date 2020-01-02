import yaml

mydict = {'a':1,'b':2, 'c':3}
mylist = [1,2,4,5,5]
mytuple = ('x','y','z')

loaded_yaml = yaml.dump(mydict, default_flow_style=False)
print(loaded_yaml)

print (yaml.dump(mylist, default_flow_style=False))

print(yaml.dump(mytuple, default_flow_style=False))


#yaml does not store code, classes functions etc