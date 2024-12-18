
# 1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

def greet(name):

    print(f"Hello, {name}!")

greet("Alice")

# 2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.

def add_numbers(a,b):
    return a+b 
a = add_numbers(6,6)
b = add_numbers(20,30)
print (a)
print(b)

# 3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(number):

    return number % 2 == 0
k1 = is_even(4) 
k2 = is_even(7)  

print(k1)  
print(k2)

# 4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
def factorial(n):
    result = 1
    
    for i in range(1, n + 1):
        result *= i
        
    return result

result1 = factorial(5)

print(result1)
# 5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.

def find_max(a, b, c):
    
    return max(a, b, c)

print(find_max(3, 5, 7))  
print(find_max(10, 2, 8)) 
print(find_max(-1, -5, -3)) 
print(find_max(0, 0, 0))

# 6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels(s):
    count = 0
    for char in s:
        if char in 'aeiou':
            count +=1
            return count
        print(count_vowels("Hari Krishna"))

# 7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(2)) 
print(is_prime(3))   
print(is_prime(4))   
print(is_prime(17))  
print(is_prime(25))  
print(is_prime(1))   
print(is_prime(29))

# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(n):
    
    if n == 1:
        return 1

    else:
        return n + recursive_sum(n - 1)


print(recursive_sum(5))  
print(recursive_sum(10)) 
print(recursive_sum(1))

# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operator"

print(calculator(5, 3, "+"))  
print(calculator(5, 3, "-")) 
print(calculator(5, 3, "*"))  
print(calculator(5, 3, "/"))  
print(calculator(5, 0, "/"))  
print(calculator(5, 3, "^")) 

# 10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.

def find_common_elements(list1, list2):
    
    return list(set(list1) & set(list2))
print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])) 
print(find_common_elements([1, 2, 3], [4, 5, 6]))        
print(find_common_elements([1, 2, 2, 3], [2, 2, 4, 5]))  
print(find_common_elements([], [1, 2, 3])) 

# 11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string(n):
    return n[::-1]
print(reverse_string("hari"))
# 12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.

def sort_dict_by_value(d):
    
    return sorted(d.items(), key=lambda x: x[1])
    
print(sort_dict_by_value({'a': 3, 'b': 1, 'c': 2})) 

print(sort_dict_by_value({'x': 10, 'y': 30, 'z': 20})) 

print(sort_dict_by_value({'apple': 5, 'banana': 2, 'cherry': 8}))