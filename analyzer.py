# analyze a list of numbers and print summary statistics

def analyze_numbers(numbers):    
    if len(numbers) == 0:
        print("No numbers to analyze.")
        return

    sorted_numbers = sorted(numbers)
    print(f"Original list of numbers: {numbers}")
    print(f"Sorted numbers (smallest to largest): {sorted_numbers}")

    total = sum(sorted_numbers)
    count = len(sorted_numbers)
    average = total / count
    minimum = sorted_numbers[0]
    maximum = sorted_numbers[-1]
    
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    # list even numbers from list
    even_numbers = [num for num in sorted_numbers if num % 2 == 0]
    print(f"Even numbers: {even_numbers}")

# ask the user for a list of numbers separated by commas
user_input = input("Enter a list of numbers separated by commas (e.g. 3, 17, 5): ")
try:
    numbers = [float(x.strip()) for x in user_input.split(",") if x.strip() != ""]
except ValueError:
    print("Invalid input. Please enter only numbers separated by commas.")
else:
    analyze_numbers(numbers)

# fallback demo data if run in non-interactive contexts or for quick testing
if __name__ == "__main__" and not numbers:
    demo_numbers = [3, 17, 5, 7, 2, -23, 8]
    analyze_numbers(demo_numbers)