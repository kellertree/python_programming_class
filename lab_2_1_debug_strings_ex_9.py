word1 = ' Caminante, '
word2 = ' no '
word3 = ' hay '
word4 = ' camino, '
word5 = ' se '
word6 = ' hace '
word7 = ' camino '
word8 = ' al '
word9 = ' andar '
word10 = ' — '
word11 = ' Antonio '
word12 = ' Machado '
quote = word1.lstrip() + word2.lstrip() + word3.lstrip() + word4.lstrip() + word5.lstrip() + word6.lstrip() + word7.lstrip() + word8.lstrip() + word9.lstrip() + word10.lstrip() + word11.lstrip() + word12.strip()
print(quote)
# Was expecting: Caminante, no hay camino, se hace camino al andar — Antonio Machado

# English translation: Walker, there is no path, you make it as you walk.

# The SyntaxError was that word9 was not an existing variable. Changed variable 'word' to 'word9' to correct.
# The second error was that the .strip() method was being used which removed whitespace from both sides of the output. Updated .strip() to .lstrip().
