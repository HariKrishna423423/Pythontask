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

k = n.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U')

print(k) 

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

n= str(input("enter a string15 :"))
vowels = n.replace('a','').replace('A','').replace('e','').replace('E','').replace('i','').replace('I','').replace('o','').replace('O','').replace('u','').replace('U','')
print(vowels)

# 16)Python program to count the Occurrence Of Vowels & Consonants in a String

n = str (input("Enter the string16 :"))
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
count = sum(n.count(vowels) for vowels in vowels)
count1 = sum(n.count(consonants) for consonants in consonants)
print(count)
print (count1)

# 17)Python program to print the highest frequency character in a String

s = str(input("enter a char :"))
print(s.count("n"))
d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] =1
print(max(d.values()))
print(max(d, key=d.get))
hfe = max(d, key=d.get)
r = {hfe:d[hfe]}
print(r)

# 18)Python program to Replace First Occurrence Of Vowel With ‘-‘ in String

n1 = input("Enter the source string18: ")
vowels ='aeiouAEIOU'
for i in n1:
        if i in vowels:
            n1 = n1.replace(i, '-', 1) # Replace first occurrence of vowel
            break  # Exit the loop after replacing the first vowel
print(n1)

# 19)Python program to count alphabets, digits and special characters 
s = str(input("Enter a string19 :"))
dig = 0
chrc = 0
spch =0
for char in s :
    if char.isalpha() :
        chrc = chrc+1
    elif char.isdigit() :
        dig = dig+1
    else :
        spch = spch +1
 
print("charectors- ", chrc)
print("digits -", dig)
print("specialsymbals - ", spch)

# 20)Python program to check given character is digit or not using isdigit() method 

n1 = input("Enter a character2: ")

print(n1.isdigit())

# 21)Python program to calculate sum of integers in string 
n1 = input("Enter a string21: ")
count = 0
for char in n1:
    if char.isdigit():
        count = count + int(char)
    else :
        pass
print(count)

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
