# Exercise 5-8

# 5-8
usernames = ['admin', 'kate', 'eric', 'john', 'tim']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")

# Exercise 5-9

# 5-9. No Users:
usernames = []


if username == 'admin':
    print("Hello admin, would you like to see a status report?")
if usernames == []:
    print("We need to find some users!")
else:
    print(f"Hello {username.title()}, thank you for logging in again.")

# Exercise 5-10

# 5-10
current_users = ['John', 'Jacob', 'jingle', 'heimer', 'SCHMIT']

new_users = ['JOHN', 'Jacob', 'Ellen', 'Katie', 'ARI']

for user in new_users:
    if user.lower() in [user.lower() for user in current_users]:
        print("That username has already been used, please enter a new username.")
    else:
        print("That username is available.")