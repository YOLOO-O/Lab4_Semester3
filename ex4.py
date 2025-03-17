# ex4.py - A program to inform users about discounts based on their age

# Prompt user for their age
age = int(input("Enter your age: "))

# Check age and inform about discounts
if age <= 19:
    print("You qualify for student discounts!")
elif 20 <= age <= 54:
    print("You qualify for no age discounts.")
else:
    print("You can receive senior discounts!")
