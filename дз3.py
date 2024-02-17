a = int('12345')
print(a)

first_number = a % 10
a = a // 10
second_number = a % 10
a = a // 10
third_number = a % 10
a = a // 10
fourth_number = a % 10
a = a // 10
fifth_number = a % 10

print(first_number,second_number,third_number,fourth_number,fifth_number)