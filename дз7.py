in_list = [12, 0, 3, 0, 4, 10, 8]
out_list = []
x = 0
y = 0
while y < len(in_list):
    a = in_list[y]
    if a != 0:
        out_list.insert(x, a)
        x += 1
    y += 1
while x < len(in_list):
    out_list.insert(x, 0)
    x += 1
print(out_list)
