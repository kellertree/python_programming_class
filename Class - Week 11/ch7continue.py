# Rather than breaking out of a loop entirely without executing the rest of its code,
# you can use the continue statement to return to the beginning of the loop
# based on the result of a conditional test. 

# For example, consider a loop that counts from 1 to 10 but prints only
# the odd numbers in that range.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # The continue statement tells python to ignore the rest of the loop and return to the beginnig.
# In this case it stops at 2, then starts over with current_number = 2
# then it adds 1 and prints the result as long is it is an odd number "% 2 = 0".
# it iterates until each even number is encountered and then begins as long as current_number is less than 10.
    print(current_number)

