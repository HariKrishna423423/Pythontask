#python program to print integers list of divisible with 7 but not with 5 from 100 to 200.

s = []

for number in range(100,200):
    if number % 7 == 0 and number % 5 != 0:
        s.append(number)
print(s)

#python program to add multiple in elements to the list.

h = [1, 2, 3]

elements_to_add = [4, 5, 6]
for element in elements_to_add:
    h.append(element)

print(h)
