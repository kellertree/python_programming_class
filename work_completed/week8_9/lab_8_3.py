# Exercise 7-4

prompt = "Please enter the topping you would like to have:"
prompt += "\nEnter 'quit' when you are finished."

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I will add the {topping} to your pizza.")

# Exercise 7-5

prompt = "Enter 'quit' to exit loop.\nHow old are you? "

age = ""

active = True
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        if int(age) < 3:
            print("Your movie ticket is free.")
        elif 3 <= int(age) <= 12:
            print("Your movie ticket cost is $10.")
        elif int(age) > 12:
            print("Your movie ticket cost is $15.")

# Exercise 7-7

# Prints an infinite loop. "To infinity and beyond!"
x = 'infinity'

while x == 'infinity':
    print(f"To {x} and beyond!")
