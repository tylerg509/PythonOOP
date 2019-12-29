class MyNum(object):
    def __init__(self):
        print('call init')
        self.val = 0
    def increment(self):
        self.val = self.val +1



dd= MyNum()
dd.increment()
dd.increment()
print(dd.val)

# __ is a private class in python
#this makes it so that init is called by default every time mynum is called

#initalize object means setting its attributes or other prep work when required creating a new instance


class MyNum2(object):
    def __init__(self, value): #every init has self as the first argument
        print('call 2nd init')
        self.val = value
    def increment(self):
        self.val = self.val +1


dd2= MyNum2(5)
dd2.increment()
dd2.increment()
print(dd.val)

#using class we dont call method directly we construct a new instance init is called intailly so we can pass arguments


class MyNum3(object):
    def __init__(self, value): #every init has self as the first argument
        print('call 3rd init')
        try: #encapsulation = we use a gate
            value = int(value)
        except ValueError:
            value = 0
        self.val= value
    def increment(self):
        self.val = self.val +1


dd2= MyNum3('tyler!')
dd2.increment()
dd2.increment()
print(dd.val)

#if we pass a string to the init method we will get a typeerror = encapsulation says we shold validate first
#init is important so we can enforce encapsulation before we allow methods to be run
#init allows opportunity to initalize attributes in the instance at the time of construction
# self argument is the first apperace of the instance
# __init__ is a keyword variable = must be named init