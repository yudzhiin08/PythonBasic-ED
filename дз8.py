first_list = [12, 3, 4, 10, 8]
x = 0
calk = 0

while x < len(first_list):
    if (x % 2) == 0:
        calk += first_list[x]
    x += 1
calk *= first_list[x - 1]
print(calk)