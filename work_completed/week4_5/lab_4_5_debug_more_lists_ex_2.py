# The following is not a run-time error, but a logical error. The program runs without an error but
# the user is expecting to see test subjects 10 through 20, like so:
#
# The test subject number is 10.
# The test subject number is 11.
# The test subject number is 12.
#            ...
# The test subject number is 20.
#
# Fix the program to display the correct output.

for test_subject in range(10,21):
    print(f'The test subject number is {test_subject}.')

# Corrected by switching element zero in range() function to 10.
# Corrected by switching 20 to 21 to account for the one-off-effect.
