# find()
s = "Hello, welcome to Python programming."
print(len(s))
print(s.find("Python"))

ss = "ravi kumar"
print(len(ss))
print(ss.find("ravi"))
print(ss.find("kumar"))

sss = "rajesh roy"
print(len(sss))
print(sss.find("ravi"))
print(sss.find("r"))
print(sss.rfind("o"))

#index
k = "Hello, welcome to Python programming."
print(len(k))
print(k.index("gram"))
print(k.rindex("g"))
print(k.index("h"))
print(k[-6])

n =str(input("enter your name :"))
print(len(n))
print(n[4])
print(n.rfind("K"))

#spilt()

text = "Hello world! Welcome to Python."
words = text.split()
print(words)

text1 = "apple,orange,banana,grape"
fruits = text1.split(",")
print(fruits)

text2 = "Line 1\nLine 2\nLine 3"
lines = text2.split("\n")
print(lines)

text3 = "apple,,orange,,banana"
fruits = text3.split(",")
print(fruits)

#Joins() 

words = ['Hello', 'world', 'Python']
result = ' '.join(words)
print(result)

fruits = ['apple', 'orange', 'banana', 'grape']
result = ', '.join(fruits)
print(result)


#upper(): 
text4 = "hello world"
result = text4.upper()
print(result)


# lower()
text5 = "HELLO WORLD"
result = text5.lower()
print(result)

# title()
text6 = "hello world from python"
result = text6.title()
print(result)

#capitalize()
text = "hello WORLD"
result = text.capitalize()
print(result)

#swapcase()
text = "Hello World"
result = text.swapcase()
print(result)

#isalpha()
char = 'a'
print(char.isalpha())                 
char1 = '1'
print(char1.isalpha())                

#isdigit():
char2 = '5'
print(char2.isdigit())              
char3 = 'a'
print(char3.isdigit())              
 
#isspace(): 
char4 = ' '
print(char4.isspace())  
char5 = 'a'
print(char5.isspace())  

#isalnum(): 
char6 = 'a'
print(char6.isalnum())             
char7 = '5'
print(char7.isalnum())             
char8 = '@'
print(char8.isalnum())            

#isupper(): 
char9 = 'A'
print(char9.isupper())             
char0 = 'a'
print(char0.isupper())            

#islower(): 
char11 = 'a'
print(char11.islower())                 
char12 = 'A'
print(char12.islower())              

#istitle():
text8 = "hello world"
result = text8.title()
print(result)

#iscapitalize():
text9 = "pYTHON"
result = text9.capitalize()
print(result)
