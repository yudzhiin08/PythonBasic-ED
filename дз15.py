
d = int(input())
if d >= 0 and d < 8640000:
    sec = d % 60
    d = d // 60
    minute = d % 60
    d = d // 60
    hour = d % 24
    d = d // 24
    dd = d % 10
    if dd == 1:
        s = "день"
    elif dd in [2, 3, 4]:
        s = "дня"
    else:
        s = "днiв"

    print(f'{d} {s} {hour:02}:{minute:02}:{sec:02}')
else:
    print("Error")

