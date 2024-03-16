import random
def common_elements():
    my_list1 = []
    my_list2 = []
    for a in range(random.randint(10, 100)):
        my_list1.append(random.randint(1,20)*3)
    for b in range(random.randint(10,100)):
        my_list2.append(random.randint(1,20)*5)
#    print(my_list1)
#    print(my_list2)
    return list(set(my_list1) & set(my_list2))

print(common_elements())
