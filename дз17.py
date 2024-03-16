
def correct_sentence(text):
    if not text.endswith("."):
        text = text + "."
    return text.capitalize()

test = input("Test string ")

print(correct_sentence(test))