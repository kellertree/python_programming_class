# Federico and Dewi grew up together and would play video games and ski together.

federico_hobbies = ['video games', 'skiing']
dewi_hobbies = federico_hobbies[:]

print(f'Their common hobbies are {federico_hobbies} and {dewi_hobbies}.')

# Dewi also likes to collect coins.
dewi_hobbies.append('numismatics')

# Federico thinks collecting stamps is where it's at. He also likes to zip-line.
federico_hobbies.append('collecting stamps')
federico_hobbies.append('zip-lining')

print(f"Federico's hobbies are {federico_hobbies}.")
print(f"Dewi's hobbies are {dewi_hobbies}.")

# Expected to see:
# Federico's hobbies are ['video games', 'skiing', 'collecting stamps', 'zip-lining'].
# Dewi's hobbies are ['video games', 'skiing', 'numismatics'].
# Fix the program.

# The issue was federico's hobbies were stored in the dewi_hobbies variable.
# The proper way to copy a list would be to use an open ended slice [:].
# If we use an open ended slice then changes made to federico_hobbies won't affect dewi_hobbie
