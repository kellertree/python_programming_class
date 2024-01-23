# create an empty list for outfits.
outfits = []

# creates a list for a top and bottom for days of the week.
monday_outfit = ['flannel button-up', 'bluejeans']
tuesday_outfit = ['hawaiian shirt', 'shorts']
wednesday_outfit = ['blue button-up', 'gray dresspants']

# add the monday_outfit, tuesday_outfit, wednesday_outfit to the outfits list.
outfits.insert(0, monday_outfit)
outfits.insert(1, tuesday_outfit)
outfits.insert(2, wednesday_outfit)

print(f"The outfits for the next 3 days are: {outfits}.")

print(f"Monday's outfit is {outfits[0]}.")
print(f"Tuesday's outfit is {outfits[1]}.")
print(f"Wednesday's outfit is {outfits[2]}.")
print(f"Tuesday's shirt is a {outfits[1][0]}.")
print(f"Wednesday's pants are {outfits[2][1]}.")