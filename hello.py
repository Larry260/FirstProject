print("Hello, again.")
# function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# test the function
print("Factorial of 5 is:", factorial(5))
# return the largest number in a list
def largest_number(lst):
    if len(lst) == 0:
        return None
    else:
        max_num = lst[0]
        for num in lst:
            if num > max_num:
                max_num = num
        return max_num
# test the function
numbers = [3, 17, 5, 7, 2, -23, 8]
print("Largest number in the list is:", largest_number(numbers))
