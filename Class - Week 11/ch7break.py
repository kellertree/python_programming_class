# The 'break' command ends a loop when it is encountered.
# Other words 'break' causes python to exit the loop.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."


while True:
    city = input(prompt)

    if city == 'quit':
        break # program ends
    else:
        print("I'd love to go to " + city.title() + "!")