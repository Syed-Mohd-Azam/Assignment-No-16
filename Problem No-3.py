# Write a python program to reverse the tuple.
t,l=("iNeuron","MySirG Education Services", "Syed Mohd Azam"),list()
length=len(t)-1
while(length>=0):
    l.append(t[length])
    length=length-1
print(tuple(l))