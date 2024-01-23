# Exercise 5-3

# 5-3. Alien Colors #1:

# V1 produces a succesful output because alien_color == 'green'.
alien_color = 'green'

if alien_color == 'green':
    points = 5
print(f"Congratulations! You just earned {points} points!")

# 5-3. ALien Colors Output Fail
# V2 intentionally produces no output because alien_color != 'green'.

alien_color = 'red'

if alien_color == 'green':
    points = 5
    print(f"Congratulations! You just earned 5 points!")

# Exercise 5-4
# 5-4. Alien Colors #2:
# V1 Runs if block
alien_color = 'green'

if alien_color == 'green':
    points = 5
    print(f"The player just earned {points} points for shooting a green alien.")
else:
    points = 10
    print(f"The player just earned {points} points!")

# 5-4. Alien Colors #2:
# V2 Runs else block
alien_color = 'red'

if alien_color == 'green':
    points = 5
    print(f"The player just earned {points} points for shooting a green alien.")
else:
    points = 10
    print(f"The player just earned {points} points!")

# Exercise 5-5

# 5-5.  
# V1
alien_color = 'green'

if alien_color == 'green':
    points = 5
    print(f"The player just earned {points} points for shooting a green alien.")
elif alien_color == 'red':
    points = 15
    print(f"The player just earned {points} points for hitting a red alien!")
else:
    points = 10
    print(f"The player just earned {points} points for hitting a yellow alien!")

#5-5. 
# V2
alien_color = 'yellow'

if alien_color == 'green':
    points = 5
    print(f"The player just earned {points} points for shooting a green alien.")
elif alien_color == 'red':
    points = 15
    print(f"The player just earned {points} points for hitting a red alien!")
else:
    points = 10
    print(f"The player just earned {points} points for hitting a yellow alien!")

# 5-5 
# V3
alien_color = 'red'

if alien_color == 'green':
    points = 5
    print(f"The player just earned {points} points for shooting a green alien.")
elif alien_color == 'red':
    points = 15
    print(f"The player just earned {points} points for hitting a red alien!")
else:
    points = 10
    print(f"The player just earned {points} points for hitting a yellow alien!")