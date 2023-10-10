dogs = ['collie', 'labrador', 'pug']
print(dogs)

dogs[1] = 'Shetland'

print(dogs)

dogs.insert(1, 'Labrador')

print(dogs)


dogs.pop(3)

dogs.append('Pug')

print(dogs)

del dogs[2]
print(dogs)

dogs.append('Shetland')
print(dogs)

dogs.append('Great Dane')
dogs.append('Terrier')
dogs.append('Dachshund')
dogs.append('Foxhound')

len(dogs)

# The length of dogs is 8

dogs.remove('Terrier')

len(dogs)

# The length of dogs is now 7

print(dogs)

dogs.sort()

dogs.sort(reverse=True)
print(dogs)

print(dogs[0])
print(dogs[-1])
len(dogs)
print(dogs)

print(dogs[6])

len(dogs)
print(dogs[6])


ungulates = ['domesticated goat', 'wild goat', 'zebra', 'rhino', 'killer whale']
counter = len(ungulates)
print(counter)
print(ungulates)

for ungulate in ungulates:
    print(f"Please don't pet the {ungulates}.")
    counter = counter - 1
    print(f'There are {counter} ungulates left.')
print("That's all the ungulates!")

ungulates.sort('hi', 'bye', True)











