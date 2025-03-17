# ex5.py - A function to calculate the factorial of a number using a while loop

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Prompt user for a number
num = int(input("Enter a number to calculate its factorial: "))

# Calculate factorial and print the result
fact = factorial(num)
print(f"The factorial of {num} is {fact}")
