
numbers = [1, 2, 2, 1, 5, 1]

def find_unique_numbers(numbers):
     for unique_numbers in numbers:
        if numbers.count(unique_numbers) == 1:
            break
        else:
           unique_numbers = "None"

     return unique_numbers

print(find_unique_numbers(numbers))

