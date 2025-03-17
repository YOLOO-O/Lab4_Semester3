# ex7.py - A program to print student names with the last name "Evans" and allow the user to add a name

# List of student names
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Print each name followed by "Evans"
for name in studentNames:
    print(f"{name} Evans")

# Ask the user to add another name
new_name = input("\nEnter another name to add to the list: ")

# Add the new name to the list and reprint the names with last name "Evans"
studentNames.append(new_name)

# Print updated list
print("\nUpdated student names with last name Evans:")
for name in studentNames:
    print(f"{name} Evans")
