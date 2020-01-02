#composition example
#objects we work with are decoupled
import random
from io import StringIO
class WriteMyStuff(object): #does not matter what object is sent to the class
    def __init__(self,writer):
        self.writer = writer
    def write(self):
        write_text = 'this is a nice message'
        self.writer.write(write_text) #does not check type - assumes it can call write on the object

#write my stuff is 
#we can make internal changes as long as we can call write

fh = open('text.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO()
w2=WriteMyStuff(sioh)
w2.write()

print('file object: ', open('text.txt', 'r').read())
print('StringIO object: ', sioh.getvalue())