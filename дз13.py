import string
print(string.ascii_letters)
s = string.ascii_letters
i = input(" ")
a, b = i.split('-')
print(s[s.index(a):s.index(b)+1])