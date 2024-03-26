import re
def is_palindrome(original):
    original = original.replace(" ","")
    original = re.sub(r'\W','',original)
    original = original.lower()
    for i in range(0, len(original)):
        if original[i] != original[len(original) - i - 1]:
            return False
    return True

Base = "deed"
print("Palindrome") if is_palindrome(Base) else print("Not Palindrome")

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")