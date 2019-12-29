class Joe(object):
    def callme(self):
        print('calling callme method with instance')
        print('print self now')
        print(self) #instance is passed as first argument


thisjoe = Joe()


#thisjoe.callme does not contain an argument visibly
#however if you take self out of callme you will get an error = callme takes 0 positional arguments but 1 was given
#when you call a method on an instance the instance is passed to the method as the first argument
thisjoe.callme()

print(thisjoe) #note that print self and print thisjoe returns the same instance in the command line. #call me as a method passes the instance

#a method on an instance passes instance as the first argument to the method. within the method the first argument should be self