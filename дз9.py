import random
in_list = []
out_list = []
for i in range(random.randint(3,10)):
    in_list.append(random.randint(1, 20))
print(in_list)
out_list.insert(0,in_list[0])
out_list.insert(1,in_list[2])
out_list.insert(3,in_list[len(in_list)-2])
print(out_list)