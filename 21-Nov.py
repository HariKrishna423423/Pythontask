name = 'harik'
print (type(name))

name1 = "krishna"
print (name1)

name2 = """vara"""
print(name2)

#index accessing

text = "krishna"
print (text[5])

print (text[-6])

#slicing
name3 = "harikrishnavaraprasad423423"
print(name3[5:12])

print(name3[12:5])    # it moves forward,not backward

print (name3[3:-7])

print (name[-3:12])

print(name3[-12:-3])

print(name3[-3:-12])   # it moves forward,not backward

print (name3[3:])   #remove first 3 characters to the starting

print (name3[:3])   # from the first 3 characters to the starting

print (name3[-3:])   #from the 3rd last characters to the end

print (name3[:-3])   #remove last 3 characters to the end

#string length

name4 = "srinivas"
  
print (len(name4))

#Membership Checking in String

name5 = "Python programming"

print("py" in name5) #because it's lowercase, and "Python" starts with uppercase 'P')

print("Py" in name5)

print("co" in name5)

print('code' not in name5)     

print("Pro" not in name5)  #because it's uppercase, and "programming" starts with lowercase 'P')

"k" in 'krishna'
"K" not in "krishna"

#strip()
username = " vara prasad "
k = username.strip()
print (k)

k1 = username.rstrip()
print (k1)

k2 = username.lstrip()
print(k2)

k3 = username.upper()
print(k3)

k4 = username.lower()
print(k4)

#Replace

krishna = " hari krishna prasad "

p = krishna.replace(" ","")          #remove spaces
print(p)

p1 = krishna.replace("prasad","vara")           #replace last word
print (p1)

p2 = krishna.replace("krishna","prasad")      # replace middle word
print(p2)

p3 = krishna.replace("krishna","")         #remove word and space
print(p3)

p4 = krishna.replace("krishna","      ")    # remove word and add spacess
print(p4)




s= "welcome to world of python"
print(len(s))
ss = s.split()
print(len(ss))
print(ss)
