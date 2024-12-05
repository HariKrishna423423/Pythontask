# 1)Write a Python program to create a list of 5 integers and print the sum of all elements in the list.

s = [9,8,7,6,5]

s1 =sum(s)
print(s1)
# 2)Create a list of strings containing the names of 5 fruits. Access and print the second and fourth elements using indexing.
 
fruits = ["apple","kiwi","pineapple","goa","orange"]

print(fruits[2])

print(fruits[4])

# 3)Create a list of numbers from 1 to 10. Use slicing to print the first three numbers, the last three numbers, and every second number in the list.

l = [1,2,3,4,5,6,7,8,9,10]

print(l[:3])

print(l[-3:])

print(l[3:10:2])

# 4)Write a Python program that initializes a list with some numbers and:
# 5)Adds a new number to the list using the append() method.
# 6)Inserts a number at the second position using insert().
# 7)Extends the list with another list of numbers.
# 8)Remove all occurrences of the number 3 from a list of integers.

m =[1,2,4,5]

m.append([6,7])
print(m)

m.insert(2,3)
print(m)

m.extend([8,9])
print(m)

m.remove(3)
print(m)


# 9)Write a Python program to remove the last element of a list using pop() and print the updated list.

k = [9,8,7,6,5,4,3,2,1]
j = k.pop(4)
print(k)

# 10)Write a Python program to sort a list of 10 random integers in ascending and descending order using sort() and reverse().

n1 = [21,15,18,3,8,5,28,88,45,20]

n1.reverse()
print(n1)

n1.sort()
print(n1)

n1.sort()
print(n1[::-1])


# 11)Create a list of strings and reverse the order of elements using both reverse() and slicing [::-1]. Compare the results.

n2 = [10,20,30,40,50]

n2.reverse()
print(n2)

n2[::-1]
print(n2)


# 12)Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list.


r = [1, 2, 3, 4, 5]

print(r)

r1 = r

r.append(6)

print(r1)

r2 = r.copy()

r2.append(7)

print(r2)

# 13)Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not.

a = [1, 2, 3, 4, 5,6,7,8]

print(a)

b = a

a.append(6)

print(b)

c = a.copy()

c.append(7)

print(c)

# 14)Create two lists of numbers, and use the + operator to concatenate them. Then, use the * operator to repeat the elements of one list 3 times.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3 = list1+list2
print(list3)

print(list1*3)

# 15)Given a list of numbers, write a Python program to create a new list where each element is doubled (i.e., each element is multiplied by 2).
numbers = [1, 2, 3, 4, 5]

numbers1 = [x * 2 for x in numbers]

print(numbers)
print(numbers1)

# 16)Write a Python program to check if a specific element (e.g., 5) exists in a given list using the in operator. If it exists, print its position; otherwise, print "Element not found."
    #Given a list of student names, check if "John" and "Sara" are in the list using the in operator.

numbers = [9,8,7,6,5]

if 5 in numbers:
    print(numbers.index(5))
else:
    print("Element 5 not found.")

students = ["hari", "krishna", "John", "Sara", "prasad"]

if "John" in students:
    print("John is in the student list.")
else:
    print("John is not in the student list.")

if "Sara" in students:
    print("Sara is in the student list.")
else:
    print("Sara is not in the student list.")

# 17)Write a Python program to create a 3x3 matrix (nested list) and print the matrix. Then, access and print the element at row 2, column 3.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("3x3 Matrix:")

for row in matrix:
    print(row)

element = matrix[1][2]
print("\nElement at row 2, column 3:", element)

# 18)Create a nested list representing a list of students' names and their respective grades. Write a Python program to print each student's name along with their grade.

s1 = [["hari", 85],["krishna", 92],["vara", 78],["prasad", 88],["ravi", 91]]

for student in s1:
    name, grade = student  
    print(student)
# 19)Create a list of numbers from 1 to 20. Write a Python program to generate two separate lists:
#One containing only the even numbers.
#Another containing only the odd numbers.

n1 = list(range(1, 21))

even = [num for num in n1 if num % 2 == 0]

odd = [num for num in n1 if num % 2 != 0]

print(even)
print(odd)

# 20)Write a Python program that reads a list of integers and returns a new list containing only the unique elements (i.e., removing duplicates).
   #Given a list of tuples representing (name, age), sort the list by age in ascending order.

numbers = [1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8]

unique_elements = list(set(numbers))

print(numbers)
print(unique_elements)




