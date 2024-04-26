my_list = [10, 20, 30, 40]
#index      0  1   2   4
print(my_list)

my_list.insert(1,15)
print(my_list)

list2 = [50, 60, 70]
my_list.extend(list2)
print(my_list)

del my_list[4]
print(my_list)

my_list.sort()
print(my_list)

index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)

