
def correct_sentence(text):
    if not text.endswith("."):
        text = text + "."
    return text.capitalize()

test = input("Test string ")

print(correct_sentence(test))

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings, Friends") == "Greetings, friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')