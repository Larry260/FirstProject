# analyze a list of numbers and print summary statistics

def analyze_numbers(numbers):    
    if len(numbers) == 0:
        print("No numbers to analyze.")
        return
    
    print(f"Original list of numbers: {numbers}")

    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    # list even numbers from list
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")

# test the function
numbers = [3, 17, 5, 7, 2, -23, 8]
analyze_numbers(numbers)
