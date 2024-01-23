# Exercise 4-1
# 4.1. Pizzas: Store 3 kinds of pizza in a list. 
# Then for loop to print the name of each pizza.
pizza_types = ['cheese', 'pepperoni', 'vegetable']
for pizza in pizza_types:
    print(pizza)

# Modify the for loop to print a sentence using the name of the pizza.
# Instead of printing just the name of hte pizza.
for pizza in pizza_types:
    print("I like " + pizza + " pizza.")
    
print("\nI really love pizza!")

# Exercise 4-2
# 4.2. Animals: Store animals with common characteristic in list.
# Use for loop to print out the name of each animal.
animals = ['python', 'cobra', 'cottonmouth']
for animal in animals:
    print(animal)

# Modify the program to print a statement about each animal.
for animal in animals:
    print(f'A {animal} in most cases lives outside.')

print("\nAll of these animals are snakes.")
