#3-1. Names: This code prints out each name in the names list individually by index value. Accessing each element one at a time.
names = ['Aria', 'Jewels', 'Mark', 'Scott', 'Rhett', 'Sonnet', 'Ridge']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

#3-2. Greetings: The code below prints a greeting message for each name in the list.
print(f'Hi {names[0]}! How are you doing today?')
print(f'Hi {names[1]}! How are you doing today?')
print(f'Hi {names[2]}! How are you doing today?')
print(f'Hi {names[3]}! How are you doing today?')
print(f'Hi {names[4]}! How are you doing today?')
print(f'Hi {names[5]}! How are you doing today?')
print(f'Hi {names[6]}! How are you doing today?')

#3-3. Your Own List: Favorite mode of transportation and various statements.
favorite_transport = ['Jeep Longitude', 'Tesla Model S', 'electric boat', 'electric Jeep', 'helicopter']
print(f"My favorite vehicle would be a {favorite_transport[0]}.") 
print(f"If I had a {favorite_transport[1]} it would reduce my impact on climate change.")
print(f"I would like to own an {favorite_transport[2]} with a range of 1000 miles.")
print(f"If I had a {favorite_transport[-1]} I could explore natural environments far from civilization.")
print(f"I would prefer an {favorite_transport[-2]} over a {favorite_transport[1]}.")

# 3-4. Guest List: Make a list that includes at least three people you'd like to meet.
# Then use your list to print am essage to each person, inviting them to dinner.
guest_list = ['Remi', 'Andrew', 'Steven']
print(guest_list)

print('Hello ' + guest_list[0] + '! Would you like to get dinner some time?')
print('Hello ' + guest_list[1] + '! Would you like to get dinner some time?')
print('Hello ' + guest_list[2] + '! Would you like to get dinner some time?')

# 3-5. Changing Guest List: It turns out one of your guests can't make the dinner so you need to invite someone else.
# Use the list to send out a new set of invitations.
guest_list = ['remi', 'andrew', 'steven']

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title()  + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight? \n')

# 3-6. More Guests: You just found a bigger dinner table. Invite three more guests.
guest_list = ['remi', 'andrew', 'steven']

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title()  + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight? \n')
print('It turns out that ' + guest_list.pop(1).title() + ' will not be able to make it.\n')

guest_list.insert(1, 'emmie') # Inserts Emmie into index 1.

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight?\n')

print('Just a quick update team I managed to find a bigger table.\n')

guest_list.insert(3, 'colin')
guest_list.insert(4, 'leah')
guest_list.append('aria')

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[3].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[-2].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[-1].title() + '! Would you like to get dinner tonight?')

# 3-7. Shrinking Guest List: The table won't arrive in time for the dinner, and you have space for only tow guest.
guest_list = ['remi', 'andrew', 'steven']

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title()  + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight? \n')
print('It turns out that ' + guest_list.pop(1).title() + ' will not be able to make it.\n')

guest_list.insert(1, 'emmie') # Inserts Emmie into index 1.

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight?\n')

print('Just a quick update team I managed to find a bigger table.\n')

guest_list.insert(3, 'colin')
guest_list.insert(4, 'leah')
guest_list.append('aria')

print('Hello ' + guest_list[0].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[1].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[2].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[3].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[-2].title() + '! Would you like to get dinner tonight?')
print('Hello ' + guest_list[-1].title() + '! Would you like to get dinner tonight?\n')

print('I am only able to invite two people for dinner.\n')

# Each time we pop the list removes the index requested, therefore the index placement changes each time you pop(). 
# That is why there is -1, -1, -1, -1 in the guestlist.pop(). Each time we remove someone that value is gone and the list is shorter.
# Python runs top down so each time you pop the index value for the element shifts to whatever is next inline.
print(f'I am sorry that I cannot invite you to dinner tonight {guest_list.pop(-1).title()}.')
print(f'I am sorry that I cannot invite you to dinner tonight {guest_list.pop(-1).title()}.')
print(f'I am sorry that I cannot invite you to dinner tonight {guest_list.pop(-1).title()}.')
print(f'I am sorry that I cannot invite you to dinner tonight {guest_list.pop(-1).title()}.\n')
print(f'Hey {guest_list[0].title()} you are still invited for dinner.')
print(f'Hey {guest_list[1].title()} you are still invited for dinner.')

# When we run the del statement we are del the value that is at the given index.  

del guest_list[0]
del guest_list[0] # Since we deleted the value/element in 0 whatever was in index 1 drops down to index 0.

print(guest_list)

#3.8. Seeing the World: Think of five places in the world you'd like to visit.
places_to_visit = ['Japan', 'Scotland', 'Sequoia National Park', 'Olympic National Park', 'Iceland']
print(places_to_visit)

# Prints out a temporary sorted list in alphabetical order.
print(sorted(places_to_visit))

# Prints out the list in original order.
print(places_to_visit)

# Prints out the list in a tempory reverse alphabetically sorted order.
print(sorted(places_to_visit, reverse=True))

# Prints out the list to show it's orignial order has not changed.
print(places_to_visit)

# Uses the sort() method to change the list so it is stored in alphabetical order.
places_to_visit.sort()
print(places_to_visit)

# Uses sort(rever=True) method to change the list so it is stored in reverse alphabetical order.
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3-9. Dinner Guests: Uses len() function to determine how many people are invited to dinner.
guest_list = ['remi', 'andrew', 'steven']
numberofguests = len(guest_list)
print(f"I invited {numberofguests} guests to dinner.")

# 3-10. Every Function: 
study_topics = ['null', 'python programming', 'structured query language', 'databases', 'data analytics', 'data science'] # Creates a list to be referenced.
print(study_topics)

study_topics.reverse() # .reverse() reverses the order of the list permanently you can also use it to switch back.
print(study_topics)

study_topics.sort(reverse=True) # .sort(reverse=True) permanently reorders the list reverse alphabetically.
print(study_topics)

print(sorted(study_topics)) # sorted(study(list)) temporarily produces a sorted list without changing the lists value.
print(study_topics)

study_topics.sort() # .sort() permanently reorders the list alphabetically.
print(study_topics)

print(sorted(study_topics, reverse=True)) # sorted(study(list, reveser=True)) temporarily produces a reverse alphabetically sorted list without changing the lists value.

print(study_topics)

study_topics.remove('null') # .remove() scans the list and removes the label given.

print(study_topics)

print('Since we are still testing functions I will reinsert null.\n')

study_topics.insert(0, 'null') # Inserts 'null' at index 0.

print(study_topics)

del study_topics[0] # Deletes the value at index 0, in this case null.

print(study_topics)

study_topics.append('null') # Attaches the value 'null' to the end of the list.

print(study_topics)

study_topics[-1] # Selects and prints the last value in the list.

last_value = study_topics[-1] # Creates the variable with the label at index -1, which is null.
print(f'\nThe last value is {last_value}.')

print(f'\nSince the last value in our list is {last_value}.')
print(f'It is important we remove the null value from our list with pop.')
print(f'By using the .pop() function we can use null one time after its removal.')
print(f"\nWe remove {study_topics.pop(-1).title()} from our study topic list.\n")

print(study_topics)

number_of_topics = len(study_topics)

print(f"\nThere are now {number_of_topics} in my list.\n")
print(f"It is my goal to study {study_topics[0].title()} and find work in the tech industry.")
print(f"It is my goal to study {study_topics[1].title()} and find work in the tech industry.")
print(f"It is my goal to study {study_topics[2].title()} and find work in the tech industry.")
print(f"It is my goal to study {study_topics[3].title()} and find work in the tech industry.")
print(f"It is my goal to study {study_topics[4].title()} and find work in the tech industry.")





