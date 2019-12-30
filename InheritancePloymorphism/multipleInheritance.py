#hierarchy could be instance class parent class grandparent class and so on

#python uses depth first search in multiple inheritance

#structure of diagram
#class D goes to C and B
#class B goes to A

#structure of diagram
#class b inherits from a
#class d inherits from c
#class d inherits from b

#python will inherit the following way:
    #d inherits from b
    #b inherits from a
    #then
    #dd inherits from c

    #this is the method resolution order d-b-a-c
    #this means if classes implement the same method the method you are calling may be applied in an order other than what you expect

class A(object):
    def dothis(self):
        print('doing this in A')
class B(A):
    pass
class C(object):
    def dothis(self):
        print('doing this in C')
class D(B,C):
    pass

d_instance = D()
d_instance.dothis()

print(D.mro()) ##print the method resolution order = d-b-a-c


#things get complicated in a dimond inheritance structure
# class D inherits from B and A
# class B and C inherit from A
# this is ambiguous inheritance


#python removes ambiguous methods
#python removes earlier apperances of multiply reffered to classes
#d-b-a-c-a goes to d-b-c-a in the diamond shaped inheritance pattern

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
class A2(object):
    def dothis(self):
        print('doing this in a')
class B2(A2):
    pass
class C2(A2):
    def dothis(self):
        print('doing this in c')
class D2(B2,C2):
    pass
d_instance = D()
d_instance.dothis()
print(D.mro()) #mro is d-b-a-c in this diamond inheritance pattern
# the rule : if the same class appers in the mro the earlier methods of this class are removed