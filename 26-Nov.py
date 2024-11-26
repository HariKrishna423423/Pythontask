#1)Python Program to count occurrence of a given characters in string. 

n =str(input("enter your string1 :"))

count =n.count("s")

print(count)

#2)Python Program to check if two Strings are Anagram. 

n1 = str(input("Enter the first string2: "))
n2 = str(input("Enter the second string2: "))

if (sorted(n1) == sorted(n2)):
    print("n1 and n2 are anagrams")
else:
    print("n1 and n2 are not anagrams")

#3)Python program to check a String is palindrome or not.
            
n =str(input("enter the string3 :"))

if (n == n[::-1]):      #Reversing a String

    print("n is a palindrome.")
else:
    print("n is not a palindrome.")

#4)Python program to replace the string space with a given character. 
n =str(input("enter the string4 :"))

s = n.replace(" ","n")

print(s)


#5)Python program to replace the string space with a given character using replace() method. 
n = str(input("enter your string5 :"))

p = n.replace(" ","p")  

print(p)

#6)Python program to convert lowercase char to uppercase of string.


n = str(input("enter your string6 :"))

k = n.upper()

print(k)

#7)Python program to convert lowercase vowel to uppercase in string. 


n = str(input("Enter a string7: "))

n = n.replace('a', 'A') 
n = n.replace('e', 'E') 
n = n.replace('i', 'I') 
n = n.replace('o', 'O') 
n = n.replace('u', 'U')

print(n) 

# 8)Python program to separate characters in a given string
 

n = str(input("Enter a string8 : "))

k = ' '.join(n)
print(k)

# 9)Python program to remove blank space from string 
n = str(input("Enter a string9 : "))

k = n.replace(" ", "")

print(k)

# 10)Python program to concatenate two strings using join() method
k1 = str(input("Enter the string10 :"))
k2 = str(input("Enter the string10 :"))

r = ' '.join([k1,k2])

print(r)

# 11)Python program to concatenate two strings without using join() method

s1 = str(input("Enter the string11 :"))
s2 = str(input("Enter the string11 :")) 
s3 = s1+s2
print(s3)

# 12)Python program to remove repeated character from string

s = str(input("Enter string12 :"))
p = ""
for char in s:
    if char not in p:
        p = p+char
print(p)

# 13)Python program to check given character is vowel or consonant

n = str (input("Enter the char :"))
if (n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
    print("vowel")
else:
    print("consonant") 
# 14)Python program to check given character is digit or not

x= "123456"
print(x.isdigit()) 
# 15)Python program to delete vowels in a given string

n = str (input("Enter the string15 :"))
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
k = ''

for char in n:
  if char not in vowels:
      k = k+char
print(k)

# 16)Python program to count the Occurrence Of Vowels & Consonants in a String

n = str (input("Enter the string16 :"))
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
count = sum(n.count(vowels) for vowels in vowels)
count1 = sum(n.count(consonants) for consonants in consonants)
print(count)
print (count1)

# 17)Python program to print the highest frequency character in a String

def highest_frequency_char(input_string):
    frequency = {}

    for char in input_string:
        if char in frequency:
            frequency[char] += 1
    else:
            frequency[char] = 1

    max_freq_char = max(frequency, key=frequency.get)
    max_freq = frequency[max_freq_char]

    return max_freq_char, max_freq

input_string = input("Enter a string17: ")
char, freq = highest_frequency_char(input_string)
print(f"The highest frequency character is '{char}' with {freq} occurrences.")


# 18)Python program to Replace First Occurrence Of Vowel With ‘-‘ in String

n1 = input("Enter the source string18: ")
vowels ='aeiouAEIOU'
for i in n1:
        if i in vowels:
            n1 = n1.replace(i, '-', 1)  # Replace first occurrence of vowel
            break  # Exit the loop after replacing the first vowel
print(n1)

# 19)Python program to count alphabets, digits and special characters 
def count_characters(input_string):
    alphabets = digits = special_characters = 0
    for char in input_string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_characters += 1

    return alphabets, digits, special_characters
input_string = input("Enter a string19 :")
alphabets, digits, special_characters = count_characters(input_string)
print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_characters}")
# 20)Python program to check given character is digit or not using isdigit() method 

n1 = input("Enter a character2: ")

if (n1.isdigit()):
    print(" n1 is a digit ")
else:
    print(" n1 is not a digit ")
# 21)Python program to calculate sum of integers in string 
n1 = input("Enter a string21: ")
sum1 = 0
for i in n1:
    
    if ord(i) >= 48 and ord(i) <= 57:

        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))

# 22)Python program to print all non repeating character in string 
s = str(input("Enter a string22 :"))
p = ""
for char in s:
    if char not in p:
        p = p+char
print(p)
# 23)Python program to copy one string to another string
 
n1 = input("Enter the source string23: ")

n2 = n1

print(n1)
print(n2)


