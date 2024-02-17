a = int('12345')
print("input",a)
n = 0
b=a
while a > 0:
    z = a % 10
    a = a // 10
    n = n * 10
    n = n + z
print ("output",n)