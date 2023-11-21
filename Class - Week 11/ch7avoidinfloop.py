# Avoiding infinite loops

# Every while loop needs a way to stop running so it won't continue to run forever.

# For example, this counting loop should count from 1 to 5.
# but if you accidentally omit the line x += 1, the loop will run forever.

x = 1
while x <= 5:
    print(x)
    x += 1

# if the "x += 1" was not there it would run forever.
# printing and endless series of 1s.

# Every programmer accidentally writes an infinite while loop from time to time,
# especially when a program's loops have subtle exit conditions.
# If your program gets stuck in an infinite loop, 
# pres CTRL-C or just close the terminal window displaying your program's output.

# To avoid writing infinite loops, test every while loop and make sure
# the loop stops when you expect it to. If you want your program to end
# when the user enters a certain input value, run the program and enter that value.
# If the program doesn't end, scrutinize the wa yyour program handles the values
# that should cause the loop to exit.
# Make sure at lesat one part of the program can make the loop's condition False 
# or cause it to reach a break statement.


