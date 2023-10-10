# IF ELSE statements

height = 6.5
age = 35
isProgessionalBasketballer = False
rimHeight = 10

# temp = (height > 6/25) or isProfessionalBasketballer
# print(tempt)

if (((height > 6.25) and (age < 30))) or (((height > 4.5) and (age < 40)) or (rimHeight == 8)):
   print('you can probably dunk a besketball.')
else:
    print('You probably cannot dunk a basketball.')

name = 'Cary'
great_gamers = ['Jaedong', 'Jonathan Wendel', 'Moon']
if 'Moon' in great_gamers:
    print('You are a great gamer!')



good_gamers = ['Flash', 'Patrik Lindberg', 'Daigo']

if name in great_gamers:
    print('You are a great gamer!')
elif name in good_gamers:
    print('You are a very good gamer!')
else:
    print('You might be okay at video games.')