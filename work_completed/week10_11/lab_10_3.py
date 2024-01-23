# Exercise 8-3

def make_shirt(shirt_size, shirt_text):
    """Summarizes the shirt size, and message printed on the shirt."""
    print("For " + shirt_size + " sized shirts the text should be '" + shirt_text + "'.")
    
make_shirt("medium", "I <3 Python") 
make_shirt(shirt_size="medium", shirt_text="I <3 Python")

# Exercise 8-4

def make_shirt(shirt_size="large", shirt_text="I love Python"):
    """Summarizes the shirt size, and message printed on the shirt."""
    print("For " + shirt_size + " sized shirts the text should be '" + shirt_text + "'.")

make_shirt()
make_shirt(shirt_size="medium")
make_shirt(shirt_size="small", shirt_text="I love data.")
