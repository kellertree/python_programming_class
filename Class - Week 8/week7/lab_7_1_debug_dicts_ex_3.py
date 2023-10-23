dinos = {
	'velociraptor': 6, 
	'triceratops': 9.6, 
	'pterodactyl': 3.3,
	}
# Replace "range(len(dinos))" with a method call. You may, and probably want to, rename "counter".
# The output should be:
#	Dinosaur measures 6 feet.
#	Dinosaur measures 9.6 feet.
#	Dinosaur measures 3.3 feet.
for dino, measure in dinos.items():
	print(f'Dinosaur measures {measure} feet.')

