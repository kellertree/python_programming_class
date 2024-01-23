# Exercise 9-1

class Restaurant():
    """A restaurant model."""
    
    def __init__(identifier, restaurant_name, cuisine_type):
        """Initializes resturaunt name and cuisine."""
        identifier.restaurant_name = restaurant_name
        identifier.cuisine_type = cuisine_type
        
    def describe_restaurant(identifier):
        """Displays restaurant name and cuisine specialty."""
        print(f"The restaurant is named {identifier.restaurant_name.title()}.")
        print(f"They specialize in {identifier.cuisine_type.title()} cuisine.\n")
    
    def open_restaurant(identifier):
        """Displays open message."""
        print(f"{identifier.restaurant_name.title()} is open for business.")

# Creates an instance for restaurant.
restaurant = Restaurant('la baguette', 'french')

# prints out two individual lines for each attribute in class.
print(f"The name of the restaurant is {restaurant.restaurant_name.title()}.")
print(f"They specialize in {restaurant.cuisine_type.title()} cuisine.\n")

# Calls both methods in restaurant.
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Exercise 9-2

# Creates 3 instances from class for restaurants.
# Calls the describe_restaurant() method for each restaurant.

restaurantOne = Restaurant('samurai sushi', 'japanese')
restaurantTwo = Restaurant('thai kingdom', 'thai')
restaurantThree = Restaurant('der rathskeller', 'german')

restaurantOne.describe_restaurant()
restaurantTwo.describe_restaurant()
restaurantThree.describe_restaurant()

# Exercise 9-3

class Users():
    """User model."""
    
    def __init__(user, first_name, last_name, location, age):
        """Initializes user attributes."""
        user.first_name = first_name
        user.last_name = last_name
        user.location = location
        user.age = age
        
    def describe_user(user):
        """Describes user."""
        print(f"This users first and last name is {user.first_name.title()} {user.last_name.title()}.")
        print(f"{user.first_name.title()} lives in {user.location.title()}.")
        print(f"This individual is {user.age} years old.\n")
        
    def greet_user(user):
        """Displays a greeting message."""
        print(f"Greetings to you {user.first_name.title()}! I hope your day is going well.\n")
    
userOne = Users('bilbo', 'baggins', 'the shire', '129')
userTwo = Users('frodo', 'baggins', 'the shire', '33')
userThree = Users('gandalf', 'mithrandir', 'middle earth', '54,962')
userFour = Users('aragon', 'elessar', 'rivendell', '89')

patrons = [userOne, userTwo, userThree, userFour]

for patron in patrons:
    patron.describe_user()
    patron.greet_user()  

