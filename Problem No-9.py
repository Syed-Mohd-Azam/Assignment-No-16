# Write a python program to print the value 20 from given nested tuple tuple1 = ("Python", [10, 20, 30], (2, 4, 16)).
tuple1=("Python",[10,20,30],(2,4,16))
for e in tuple1[1]:
    if e==20:
        print(e)
        break
    else:
        continue
else:
    print("20 not found!")