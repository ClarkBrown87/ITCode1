list1 = [1,2,3]
list2 = [3, -1, 2, -4, 5]

list1.extend(list2)
list1 = list(set(sorted(list1)))
print(sorted(list1))
