a = int('12345')
print(a)
n = 0
while a > 0:
    z = a % 10
    a = a // 10
    n = n * 10
    n = n + z
    print (n)

