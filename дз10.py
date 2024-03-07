import keyword
import string

sss = "-> True"
a = "t_e9st"
if a.isdigit() or not a.islower() or a in keyword.kwlist or a[0].isdigit() or ' ' in a:
    sss = "-> False"
else:
    for sp in a:
        if sp in string.punctuation and sp != '_':
            sss = "-> False"
            break
print(a, sss)
