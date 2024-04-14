list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(list1 + list2)

for i in list2:
    list1.append(i)

print(list1)