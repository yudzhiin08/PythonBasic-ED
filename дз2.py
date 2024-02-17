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
first_number1 = aaa % 10
second_number1 = aa % 10
third_number1 = a % 10
fourth_number1 = number1 %10

print(first_number1)
print(second_number1)
print(third_number1)
print(fourth_number1)


