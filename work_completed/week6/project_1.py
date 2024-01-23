verse_1 = 'Katie Casey was baseball mad, Had the fever and had it bad.'
chorus = 'Take me out to the ball game, Take me out with the crowd'
verse_2 = 'Katie Casey saw all the games, Knew the players by their first names.'

song = []

song.append(verse_1)
song.append(chorus)
song.append(verse_2)
song.append(chorus)

for element in song:
    if element == verse_1:
        print(element)
    elif element == chorus:
        print(element)
        print(element)
    elif element == verse_2:
        print(element)
    elif element == chorus:
        print(element)
        print(element)