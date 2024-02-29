while True:
    a = float(input('Please enter first number: '))
    b = float(input('Please enter second number: '))
    s = input('Please enter action: ')
    if s == '+':
       print('Your result is', (a + b))
    elif s == '-':
       print('Your result is', (a - b))
    elif s == '*':
        print('Your result is', (a * b))
    elif s == '/':
      if b != 0:
        print('Your result is', (a / b))
      else:
         print('You can`t divide by 0')
    n = input('Do you want to perform another calculation? ')
    if n == 'yes':
        continue
    elif n == 'no':
          break

