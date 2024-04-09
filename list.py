numbers = [1,2,3,4,5]
#index     0 1 2 3 4
print(numbers[2])
print(numbers)
numbers[0]=25
print(numbers)

num2 = [8,9,10]

print(len(numbers))

numbers.insert(len(numbers),6)
numbers.append(7)
numbers.extend(num2)


print(numbers)

numbers.pop(5)

print(numbers)
del numbers[7]
print(numbers)

for item in numbers:
    print(item)






