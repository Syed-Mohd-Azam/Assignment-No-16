# Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6).
tuple1=(1,2,3,4,5,6)
l=list()
for e in tuple1:
    if e==4 or e==5:
        l.append(e)
print(tuple(l))