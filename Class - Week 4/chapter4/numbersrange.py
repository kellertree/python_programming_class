# Using the range() Function
# Notice how when you run this 1 to 5 it doesn't print 5.
# Although this code looks like it should print the numbers from 1 to 5,
# It doesn't print the number 5.
# This is another result of the off-by-one behavior you'll see often in programming languages.
# The range() function causes Python to start counting at the first value
# you give i, and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains the end value,
# which would have been 5 in this case.
# To print the number 1 to 5, you would use range(1, 6).
for value in range(1,5):
    print(value)

print("\nThis line is just a seperator.\n")
# This time the output starts at 1 and ends at 5. One-off-nature of code.
for value in range(1, 6):
    print(value)

# If your output is different than what you expect when you're using 
# range() try adjusting your end value by 1.

# Using range() to Make a List of Numbers

numbers = list(range(1,6))
print(numbers)