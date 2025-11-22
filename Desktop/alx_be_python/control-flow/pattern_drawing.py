#!/usr/bin/env python3

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw pattern using while loop for rows
while row < size:
    # Draw columns using for loop
    for col in range(size):
        print("*", end="")
    print()  # Move to next line
    row += 1
