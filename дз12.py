import string
import re

text='Hello, world!'
#my_string = text.title().replace(' ', '')
my_string = text.title()
my_string = re.sub(r'\W', '', my_string)
if len(my_string)>140:
    my_string = my_string[0:140]
my_string = "#" + my_string
print(my_string)
