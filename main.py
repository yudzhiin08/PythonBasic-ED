
number = 1234
print(number // 1000)

print(number % 10)



first_number = number % 10
number = number // 10
second_number = number % 10
print(second_number, first_number)

x = 100
digit = 7254
left, right = divmod(digit, x)
print(left, right)
left, right = divmod(digit, 1)
print(left, right)
left, right = divmod(digit, 1000)
print(left, right)