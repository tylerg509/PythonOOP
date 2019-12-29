
class MyClass(object):
    def set_val(self,val):
        self.value = val
    def get_val(self):
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)
a.value = 'hello'

print(a.get_val())
print(b.get_val())


#encapsulation
#encapsulation refeers to the safe storage of data as attributes in an instance
#data should only be accessed throug instance methods
#data should be validated as correct depending on the requirements set in class methods
#data should be safe from changes by external processes 