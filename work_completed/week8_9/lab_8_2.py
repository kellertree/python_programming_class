# Exercise 7-1

# Must run an debug in order to work in VS code terminal. Highlighting and pressing enter wont work.
vehicle = input("What kind of rental car would you like?: ")
print(f"let me see if I can find you a {vehicle}.")


# Exercise 7-2

# Must run an debug in order to work in VS code terminal. Highlighting and pressing enter wont work.
message = int(input("How many people are in your dinner group?: "))

if message > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")

# Exercise 7-3
# Must run an debug in order to work in VS code terminal. Highlighting and pressing enter wont work.
number = int(input("Enter a number to see if it is a multiple of 10 or not.: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")