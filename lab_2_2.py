# Exercise 2-3 Personal Message:
# The following code assigns the variable 'name' with the label 'Jim Raynor'. 
# Then we assign the variable 'message' with an f-string containing a message for whoevers name is assigned to 'name'. Then we print the message.

name = "Jim Raynor"
message = f"Good afternoon, {name} I have prepared the report you requested."
print(message)

# Exercise 2-4 Name Cases:
# The following code assigns the name variable with 'sarah kerrigan' and then prints out the the 'name' variable in lower, upper and title case.

name = "sarah kerrigan"
print(name.lower())
print(name.upper())
print(name.title())

# Exercise 2-5 Famouse Quote:
# The following code prints out a quote that I developed and live by.

quote = '"If you continue to do nothing, nothing will continue to be your result." - Keller Tree'
print(quote)

# Exercise 2-6 Famous Quote 2:
# The following code assigns the variable famous_person with "J.K. Rowling".

famous_person = "J.K. Rowling"
quote = f'"It does not do to dwell on dreams and forget to live." - {famous_person}'
print(quote)


# Exercise 2-7 Stripping Names:

# The following code uses a variable to represent someones name. It then uses "\t" to tab the string and "\n" to add a new line to the string.
# It then prints the person's name, so the whitespace around the name is displayed. Then it prints the name using each of the three stripping functions, lstrip(), rstrip() and strip().

name = ' Artanis Daelaam '
print(f'\t{name}\n')
print(f'\t{name.lstrip()}\n')
print(f'\t{name.rstrip()}\n')
print(f'\t{name.strip()}\n')
