# Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
tuple1,list,sort_list= (('a', 21),('b', 37),('c', 11), ('d',29)),[],[]
for e in tuple1:
    list.append(e[1])
s=sorted(list)
for e in s:
    for k in tuple1:
        if e==k[1]:
            sort_list.append(k)
            break
        else:
            continue
    continue
print(tuple(sort_list))  