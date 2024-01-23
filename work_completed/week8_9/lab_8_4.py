# Exercise 7-8

# First we create a list of various sandwhiches
# We also create an empty list for finished_sandwiches.
sandwich_orders = ['peanut butter and jelly', 'blt', 'philly cheese steak']
finished_sandwiches = []

# Loops through the list of sandwich orders
# Printing a message for each order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich == 'blt':
        print("I made you a " + current_sandwich.upper() + " sandwich.")
    else:
        print("I made you a " + current_sandwich.title() + " sandwich.")
    
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been finished.\n")
for finished_sandwich in finished_sandwiches:
    if finished_sandwich == 'blt':
        print(finished_sandwich.upper())

    else:
        print(finished_sandwich.title())

# Exercise 7-9

# First we create a list of various sandwhiches
# We also create an empty list for finished_sandwiches.
sandwich_orders = ['pastrami', 'pastrami', 'pastrami', 'peanut butter and jelly', 'blt', 'philly cheese steak']
finished_sandwiches = []

print("\nNOTICE: The deli has run out of pastrami!\n")

# For each pass through the loop pastrami is removed until it is all gone.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loops through the list of sandwich orders
# Printing a message for each order
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()


    if current_sandwich == 'blt':
        print("I made you a " + current_sandwich.upper() + " sandwich.")
    else:
        print("I made you a " + current_sandwich.title() + " sandwich.")
    
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches.
print("\nThe following sandwiches have been finished.\n")
for finished_sandwich in finished_sandwiches:
    if finished_sandwich == 'blt':
        print(finished_sandwich.upper())

    else:
        print(finished_sandwich.title())
