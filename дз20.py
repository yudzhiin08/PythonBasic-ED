
numbers = [1, 2, 2, 1, 5, 1]

def find_unique_numbers(numbers):
     for unique_numbers in numbers:
        if numbers.count(unique_numbers) == 1:
            break
        else:
           unique_numbers = "None"

     return unique_numbers

print(find_unique_numbers(numbers))

assert find_unique_numbers([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_numbers([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_numbers([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")