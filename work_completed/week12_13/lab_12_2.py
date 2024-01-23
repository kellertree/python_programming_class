# Exercise 9-4

class Restaurant():
    """A restaurant model."""
    
    def __init__(identifier, restaurant_name, cuisine_type):
        """Initializes resturaunt name and cuisine."""
        identifier.restaurant_name = restaurant_name
        identifier.cuisine_type = cuisine_type
        identifier.number_served = 0
        
    def describe_restaurant(identifier):
        """Displays restaurant name and cuisine specialty."""
        print(f"The restaurant is named {identifier.restaurant_name.title()}.")
        print(f"They specialize in {identifier.cuisine_type.title()} cuisine.\n")
        
    def set_number_served(identifier, number_served):
        """Updates the number of customers served."""
        identifier.number_served = number_served
        
    def increment_number_served(identifier, customers_served):
        """Adds each customer served to the number of customers served."""
        identifier.number_served += customers_served
    
    def open_restaurant(identifier):
        """Displays open message."""
        print(f"{identifier.restaurant_name.title()} is open for business.")

restaurant = Restaurant('falafel house', 'mediterranean')

print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} customers today.\n")

# Modifies number of customers servered by directly modifying value.
restaurant.number_served = 20
print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} customers today.\n")

# Modifies number of customers served through a method.
restaurant.set_number_served(25)
print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} customers today.\n")

# Adds to existing number of guests served.
restaurant.increment_number_served(5)
print(f"{restaurant.restaurant_name.title()} has served {restaurant.number_served} customers today.\n")

# Exercise 9-5

class Users():
    """User model."""
    
    def __init__(user, first_name, last_name, location, age):
        """Initializes user attributes."""
        user.first_name = first_name
        user.last_name = last_name
        user.location = location
        user.age = age
        user.login_attempts = 0
        
    def describe_user(user):
        """Describes user."""
        print(f"This users first and last name is {user.first_name.title()} {user.last_name.title()}.")
        print(f"{user.first_name.title()} lives in {user.location.title()}.")
        print(f"This individual is {user.age} years old.\n")
        
    def greet_user(user):
        """Displays a greeting message."""
        print(f"Greetings to you {user.first_name.title()}! I hope your day is going well.\n")
        
    def increment_login_attempts(user):
        """Increments login attempts by 1"""
        user.login_attempts += 1
        
    def reset_login_attempts(user):
        """Resets login attempts to zero."""
        user.login_attempts *= 0

# Creates an instance for a user.
userOne = Users('athena', 'pallas', 'mount olympus', 'immortal')

# While login attempts are less than 6.
# Increments login attempts by 1.

while userOne.login_attempts < 6:
    userOne.increment_login_attempts()
    print(f"User login attempts: {userOne.login_attempts}")   


# Prints current login attempt.
print(f"Current login attempt count: {userOne.login_attempts}.\n")

# Resets login attempts.
userOne.reset_login_attempts()

print(f"Current login attempt count: {userOne.login_attempts}.\n")