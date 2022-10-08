# Write a python program to check if all items in the tuple are the same.
t1=(12,12,43,56)
t2=(10,10,10,10)
item1,item2=t1[0],t2[0]
for e in t1:
    if e==item1:
        continue
    else:
        print("All items in tuple 1 are not same.")
        break
else:
    print("All items in tuple1 are same.")
for e in t2:
    if e==item2:
        continue
    else:
        print("All items in tuple2 are not same.")
        break
else:
    print("All items in tuple2 are same.")