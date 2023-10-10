# For every magician in the list of magicians, print the magician's name.
# We defin list at 1, and at 2 we define a for loop.
# This line tells Python to pull a name from the list magicians, and store it in the variable magician.
# At 3 we tell python to print the name that was just stored in magician.
# Python then repeats lines 2 and 3, once for each name in the list.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Doing more with a for loop. Print a message to each magician, telling them that they performed a great trick:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# You can write as many lines of code as you like in the for loop.
# Every indented line following the line for magician in magicians is considered inside the loop.
# Each indented line is executed once for each value in the list.
# Therefore, you can do as much work as you like with each value in the list.

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!") # Since it is not indented it only prints once.

magicians = ['alice', 'david', 'carlina']
for magician in magicians:
    print(magician)


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

