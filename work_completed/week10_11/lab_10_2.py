# Exercise 8-1

# first, we create a function defnition with def and display_message():.
# second, we write the body of our function (the code)
def display_message():
    print("In chapter 8, I am learning about functions.")
    
# third call the function
display_message()

# Exercise 8-2

# first, we create a function definition with def and favorite_book()
# we set up the function definition so that it accepts one parameter
# the parameter in this function is 'title'.
def favorite_book(title):
    """Displays favorite book."""
    # We use the parameter title as this is where we 
    # pass our argument too. 
    # The argument is our favorite book.
    print("My favorite book is " + title.title() + "!")
    
favorite_book("Python Crash Course")
