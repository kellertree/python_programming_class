# Adding a flag to parrot.py
# flags act as a signal to a program.
# When a program should run only when many conditions are true.
# For example, in a game you may need to keep
# Monsters at bay, your soldiers fed, and a flow of currency going.
# You can use a flag to signal if one of these conditions become unmet.

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

# active will be our flag.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# First we set the variable active to True so the program starts in an active state.
# Doing so makes the while statement simpler because no comparison is made in the while statement itself;
# the logic is taken care of in other parts of the program.
# As long as the active variable remains True, the loop will continue running.
# In the if statement if the user enters 'quit' active gets set to False and the while loop stops.
# The active flag is outside of the while loop and by setting up
# The if statement to change active to false if a condition is met.
# We can use this for complicated programs that have multiping terminating conditions.
# Without having the while loop run even if certain conditions are not met overall.


