import pickle

mylist = ['a','b','c','d']

with open('datafile.txt', 'wb') as fh:
    pickle.dump(mylist, fh)

with open('datafile.txt', 'rb') as fh:
    unpickledlist = pickle.load(fh)


print(unpickledlist)