answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

# The conditional test at 1 passes, because the value of answer (17) is not equal to 42. Because the test passes, the indented code block is executed.


# You can include various mathematical comparisons in your conditional statements as well,
# such as less than, less than or equal to, greater than, and greater than or equal to:

age = 19

age < 21
age <= 21
age > 21
age >= 21

age_0 = 22 # assigns age_0 with a value.
age_1 = 18 # assigns age_1 with a value.

age_0 >= 21 and age_1 >= 21 # Checks to see if conditions are met. 

if age_0 >= 21 and age_1 >= 21:
    print(f"The condition was met.")
else:
    print(f"The condition was not met.")