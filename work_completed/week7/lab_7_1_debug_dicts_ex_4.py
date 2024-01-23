dinos = {
    'velociraptor': 6, 
    'triceratops': 9.6, 
    'pterodactyl': 3.3
    }

for dino_name, dino_size in dinos.items():
    print(f'The {dino_name} measures {dino_size} feet.')
# The dinosaurs ate giant growth serum. Change the sizes.
dinos['velociraptor'] = 600
dinos['triceratops'] = 960
dinos['pterodactyl'] = 330

print()
print('After taking the giant growth serum:')
for dino_name, dino_size in dinos.items():
    print(f'The {dino_name} measures {dino_size} feet.')

# After taking the giant growth serum:
# The velociraptor measures 600 feet.
# The triceratops measures 960 feet.
# The pterodactyl measures 330 feet.
