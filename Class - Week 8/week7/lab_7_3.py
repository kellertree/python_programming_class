# Exercise 6-4

programming_words = {
    'string': 'A string is a series of characters.',
    'list': 'A list is an ordered collection of items',
    'whitespace': 'Whitespace refers to any nonprinting character, such as spaces, tabs, and end-f-line symbols.',
    'dictionary': 'A dictionary is an unordered collection of key-value pairs.',
    'index': 'The position of an item or element in a list.',
    'index error': 'An index error in Python that is raised when you attempt to access an element in a sequence using an index that is outside the valid range of indices for that sequence.',
    'type error': 'A type error in Python that occurs when an operation or function is applied to an object of an inappropriate data type.',
    'syntax error': 'A syntax error in Python is an error that occurs when the code violates the rules of the Python programing langauge, often due to incorrect syntax or grammar, preventing the program from being parsed or executed',
    'debugging': 'Debugging is the process of identifying and fixing errors, defects, in computer programs, software and harware systems.',
    'loop': 'A loop in programming is a control structure that allows a set of instructions to be executed repeatedly, either for a specificed number of iterations or until a specific condition is met.',
    }

# I already used a loop for 6-3. So I just added sorted() to display the list alphabetically.
 
for word, definition in sorted(programming_words.items()):
    print(f"{word}: {definition}")


# Exercise 6-5

major_rivers = {
    'mississippi river': 'usa',
    'glomma river': 'norway',
    'kemijoki river': 'finland',
    }

# loop 1, print a sentence about each river.
for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# loop 2, print the name of each river included in the dictionary.
for river in major_rivers.keys():
    print(f"River name: {river.title()}")
    
# Loop 3, print the name of each country included in the dictionary.
for country in major_rivers.values():
    if country == 'usa':
        print(f"Coutnry name: {country.upper()}")
    else: 
        print(f"Country name: {country.title()}")

