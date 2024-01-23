first_name = "booker"
middle_initial = 't.'
last_name = "washington"
full_name = f"{first_name} {middle_initial} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# LogicError solved. The middle_initial in the f-string was not properly formated. Parenthesis were used instead of brackets; this has been corrected.
# SyntaxError solved. A comma was being used to attach the method to the variable full_name instead of the standard dot.
