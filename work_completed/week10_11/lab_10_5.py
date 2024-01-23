# Exercise 8-9

magicians = ['zip', 'zander', 'huckle', 'hawk']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


show_magicians(magicians)

# Exercise 8-10

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for magician in range(len(magicians)):
        magicians[magician] = magicians[magician] + " the Great"

magicians = ['zip', 'zander', 'huckle', 'hawk']

make_great(magicians)

show_magicians(magicians)
