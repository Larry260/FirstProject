"""Number list analyzer.

Reads a list of numbers from stdin, computes summary statistics, and prints results.
- original list
- sorted list
- total, count, average, minimum, maximum
- even numbers

Usage:
    python analyzer.py

Input prompt example:
    Enter a list of numbers separated by commas (e.g. 3, 17, 5):
"""


def analyze_numbers(numbers):    
    """Analyze a list of numbers and print summary statistics."""
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

def get_numbers_from_input(prompt="Enter a list of numbers separated by commas (e.g. 3, 17, 5): "):
    user_input = input(prompt).strip()
    if not user_input:
        return []

    try:
        return [float(x.strip()) for x in user_input.split(",") if x.strip() != ""]
    except ValueError:
        print("Invalid input. Please enter only numbers separated by commas.")
        return []


def main():
    numbers = get_numbers_from_input()
    if not numbers:
        print("No valid input received. Using demo list instead.")
        numbers = [3, 17, 5, 7, 2, -23, 8]

    analyze_numbers(numbers)


if __name__ == "__main__":
    main()