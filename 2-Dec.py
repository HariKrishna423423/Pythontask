# 1)Python programing create a list without using eval function.

l = input("Enter the list: ")

l1 = [int(item) for item in l.split()]

print(l[0])

print(type(l))

print(type(l1))

print(type(l1[1]))

# 2)python program to print integers list of divisible with 7 but not with 5 from 100 to 200.

s = []

for number in range(100,200):
    if number % 7 == 0 and number % 5 != 0:
        s.append(number)
print(s)

# 3)python program to add multiple in elements to the list.

h = [1, 2, 3]

elements_to_add = [4, 5, 6]
for element in elements_to_add:
    h.append(element)

print(h)