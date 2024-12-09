#1.Write a function that takes a tuple and an index as inputs and returns the element at the given index. Handle the case where the index is out of bounds.

def n(input_tuple, index):
    try:
        return input_tuple[index]
    except IndexError:
        return "Index is out of bounds"

n1 = (10, 20, 30, 40)

print(n(n1, 2))  
print(n(n1, 5))

#2.Write a function to concatenate two tuples into one.

def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = concatenate_tuples(tuple1, tuple2)

print(tuple3)

#3.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.

def count_occurrences(input_tuple, value):
    return input_tuple.count(value)

k = (9, 5, 6, 9, 8, 9, 7)

k1 = count_occurrences(k, 9)

print(k1) 

#4.Write a function that calculates the length of a tuple without using the built-in `len()` function.

s = (1, 2, 3, 4, 5)
count = 0
for char in s:
        count += 1

print(count)

#5.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.

def reverse_tuple(input_tuple):
    return input_tuple[::-1]

s = (1, 2, 3, 4, 5)

s1 = reverse_tuple(s)

print(s1) 

#6.Write a function to concatenate two tuples into one.

def concatenate_tuples(tuple1, tuple2):
    return (*tuple1, *tuple2)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple3 = concatenate_tuples(tuple1, tuple2)

print(tuple3)

#7.Write a function that takes a tuple and a value as inputs and returns the number of times the value appears in the tuple.

def count_occurrences(input_tuple, value):
    count = 0
    for item in input_tuple:
        if item == value:
            count += 1
    return count

k2 = (1, 2, 1, 1, 4, 1, 3)

k3 = count_occurrences(k2, 1)

print(k3)
#8.Write a function that calculates the length of a tuple without using the built-in `len()` function.

def tuple_length(input_tuple):
    count = 0
    iterator = iter(input_tuple)
    while True:
        try:
            next(iterator)
            count += 1
        except StopIteration:
            break
    return count

m = (1, 2, 3, 4, 5)

m1 = tuple_length(m)

print(m1)

#9.Write a function that takes a tuple as input and returns a new tuple with the elements in reverse order.

def reverse_tuple(input_tuple):
    return tuple(reversed(input_tuple))

s2 = (1, 2, 3, 4, 5)

s3 = reverse_tuple(s2)

print(s3)

#10.Write a function that checks if a given element exists in a tuple. Return `True` if it exists, otherwise return `False`.

def element_exists(input_tuple, element):
    return element in input_tuple

my_tuple = (1, 2, 3, 4, 5)

print(element_exists(my_tuple, 3))  
print(element_exists(my_tuple, 6))

#11.Write a function that takes two tuples and returns a tuple containing the common elements.

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

r = common_elements(tuple1, tuple2)

print(r)

#12.Write a function to unpack nested tuples and flatten them into a single tuple.  
     #Example:  
    #Input: `((1, 2), (3, 4), 5)`  
    #Output: `(1, 2, 3, 4, 5)`

def flatten_tuple(input_tuple):
    result = ()
    for item in input_tuple:
        if isinstance(item, tuple):  
            result += flatten_tuple(item)
        else:
            result += (item,) 
    return result

k = ((1, 2), (3, 4), 5)

k1 = flatten_tuple(k)

print(k1) 