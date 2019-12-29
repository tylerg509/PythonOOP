
class YourClass(object):
    classy = 10

    def set_val(self):
        self.insty = 100


dd = YourClass()

dd.set_val()
print(dd.classy)
print(dd.insty)


#now we break encapsultion
class YourClass2(object):
    classy = 'class value'

dd = YourClass2()
print(dd.classy)
dd.classy = 'inst value!' # we set

print(dd.classy) ## we print and it shows inst value
del(dd.classy) ##now delete = remove the inst value
print(dd.classy) ##now print again and reveal that the class value remains

#this demonstrates that there is a lookup order = first in the instance and then in the classs

#variables defined i nthe class are class attributes
#when we read an attribute pyhon looks for it first in the instance and then in the class