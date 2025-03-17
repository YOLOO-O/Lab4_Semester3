# ex6.py - A function to calculate the factorial of a number using a for loop

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Prompt user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial and print the result
fact = factorial(num)
print(f"The factorial of {num} is {fact}")
