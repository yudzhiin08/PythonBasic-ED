number = int('1234')
print(int(number))

first_number = number % 10
number = number // 10
second_number = number % 10
number = number // 10
third_number = number % 10
number = number // 10
fourth_number = number % 10
print(fourth_number)
print(third_number)
print(second_number)
print(first_number)

# Второй способ
number1 = int('1234')
print(int(number1))
a = number1 //10
aa = a // 10
aaa = aa //10
first_number = aaa % 10
second_number= aa % 10
third_number= a % 10
fourth_number= number1 %10

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)


