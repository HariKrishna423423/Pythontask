# 1)Write a program to create a set.
set = {1,2,3,1,4,5,6,7,False,"krishna",True,11,}
print(type(set))
print(set)
 
# 2)Write a python program to iterate over sets.
set = {1,2,3,"hari",False,9,8,7}
if "hari" in set:
    print("hari is present in the set")
else:
    print("hari is not present in the set")
 
 
# 3)Write a Python program to add member to a set.
set = {1,2,3,"vara",True,7,5,6}
set.add(4)
print(set)
 
# 4)Write a Python program to remove a member from a set.
set = {1,2,3,"vara",True,7,5,6}
set.remove(1)
print(set)
 
# 5)Write a Python program to remove item from a given set.
set = {1,2,3,"vara",True,7,5,6}
set.remove(2)
print(set)
set.discard("vara")
print(set)
# 6)Write a python program to create a intersection of set ?
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.intersection(set_2))
print(type(set_1))
print(type(set_2))
 
# 7)Write a python program to createa unionof set ?'
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.union(set_2))
 
# 8)Write a python program to create set differance ?
set_1 = {1,2,3,4,5,6}
set_2 = {9,8,7,1,2,3,4,5,6}
print(set_1.difference(set_2))
 
# 9)Write a Python program to remove items 10, 20, 30 from the following set at once.?
set = {1,2,3,4,5,6,7,8,9,10,20,30}
set.discard(10)
set.discard(20)
set.discard(30)
print(set)
 
 
# 10)Check if two sets have any elements in common. If yes, display the common elements?
set_1 = {1,2,3,4,5,6}
set_2 = {1,2,3,4,5,6,10,11}
print(set_1.intersection(set_2))
 
# 11)Update set1 by adding items from set2, except common items?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.update(set2 - set1)
print(set1)

# 12)Remove items from set1 that are not common to both set1 and set2?
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.intersection_update(set2)
print(set1)
 
                                     
# 13)Write a python program to  add a key to a dictionary ?
dict = {
    "date":17,
    "time":4
}
dict['day'] = "tuesday"
print(dict)

# 14)Write a python program to check weather the given value is present in the dictionary or not ?
dict = {
    "name":"hari",
    "age": 22,
    "city":"hyd"
}
if "name" in dict:
    print("yes")
    if "age" in dict:
        print("yes")
# 15)Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

n1 = {x: x**2 for x in range(1, 16)}

print(n1)

# 16)Write a python program to create a dictionary from the string ?

n1 = "hello world"

char1 = {}

for char in n1:

    if char in char1:
       char1[char] += 1
    else:
       char1[char] = 1

print(char1)

# 17)Write a python program to combine two dictionaries by adding values of common keys ?

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 10, 'd': 15}

combined_dict = {}

for key in dict1:
    combined_dict[key] = dict1.get(key, 0)

for key in dict2:
    combined_dict[key] = combined_dict.get(key, 0) + dict2.get(key, 0)

print(combined_dict)
 
# 18)Write a python program to merge two python dictionaries ?
dict_1 = {
    "name":"hari",
    "name2":"krishna"
 }
dict_2 = {
    "name3": "vara",
 
    "name4": "prasad"
 
}
dict_3 = dict_1 | (dict_2)
print(dict_3)