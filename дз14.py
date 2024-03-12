num = int(input())
p = 1
while num > 0:
    d = num % 10
    num = num // 10
    p *= d
    if num == 0:
      #print(p)
      if p <= 9:
        break
      num = p
      p = 1


print(p)