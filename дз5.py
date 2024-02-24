first_list = [1, ]
a = len(first_list)
if  a%2 == 0 :
    print(first_list[:a//2])
    print(first_list[a//2:])
else:
    print(first_list[:a//2+1])
    print(first_list[a//2+1:])

