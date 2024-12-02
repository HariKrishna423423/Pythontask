#Python program to check given character is digit or not  without using isdigit() method
n1 = input("Enter a character: ")

if ord(n1) >= 48 and ord(n1) <= 57:   
 print("n1 is a digit")            
else:
   print("n1 is not a digit")      

#Python program to Replace last Occurrence Of Vowel With ‘-‘ in String.
n1 = input("Enter the source string1: ")
vowels ='aeiouAEIOU'
for i in n1:
        if i in vowels:
            n1 = n1[::-1].replace(i,'-', 1)[::-1] # Replace first occurrence of vowel
            break  # Exit the loop after replacing the first vowel
print(n1)
#python program to find index values of a mid charector
n2 = "praveen"
#n2 = str(input("enter the string: "))
print(n2[3:4])
print(len(n2)//2)

n3 = "learning"

print(n3[4:5])
print(len(n2)//2)
