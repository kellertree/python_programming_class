# Before editing we had x and y. Although this works it makes more sense and is easier to read if the variables are labeled properly. 
# Changed x to dino and changed x and y to dino_name and dino_size.

dino = {
	'velociraptor': 6, 
	'triceratops': 9.6, 
	'pterodactyl': 3.3
	}
for dino_name, dino_size in dino.items():
	print(f'The {dino_name} measures {dino_size} feet.')
