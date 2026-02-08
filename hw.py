# Python program to calculate the product of all numbers in a tuple

# Sample tuple
numbers = (1, 6, 2, 3)

# Initialize product variable
product = 1

# Loop through each number in the tuple and multiply
for num in numbers:
    product *= num   # same as product = product * num

# Display the result
print("The product of all numbers in the tuple is:", product)
