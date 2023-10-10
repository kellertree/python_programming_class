# The loop in the example below first checks if the current value
# of car is anything other than 'bmw'.
# Whenever the value is 'bmw', it's printed in uppercase instead of title case:

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'audi' # assigns value 'audit' to car.

# Below can be read as "Is the value 'audi' assigned to the variable car?"
car == 'audi' # Checks to see if the condition is met and produces True or False.

car.lower() == 'audi' # This just demonstrates that condition checking with == is not case sensitive.
# The lower function does not change the original value that was assigned to car.

