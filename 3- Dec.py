# python program

s = "do what you want"

print(s[::-1])

words = s.split()
words[1:] = [word[::-1] for word in words[1:]]
s1 = " ".join(words)
print(s1)


s2 = " ".join(s.split()[::-1])
print(s2)