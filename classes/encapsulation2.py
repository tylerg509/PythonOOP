
class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return 
        self.val = val
    def get_val(self):
        return self.val
    def increment_val(self):
        self.val = self.val +1


i = MyInteger()
i.val = 'hi'
print (i.increment_val())

#this throws an error
#if we would have called set val we would not throw error
# this method breaks encapsulation 

#encapsulation = require use of setval. This way we ensure integrity of data

#breaking encapsulation = setting value without setter method