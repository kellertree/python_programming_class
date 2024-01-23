import random

# Other ideas for games are Lights Out, Mastermind, Simon, Blackjack


COLORS = ['RED', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE', 'PURPLE']


def code_breaker_make_guess():
    guess = []
    # response = input('Try to break the code: ')
    response = input('Enter the first letter of the code (r, g, b, o, y or p): ')
    guess.append(response.upper())
    response = input('Enter the second letter of the code: ')
    guess.append(response.upper())
    response = input('Enter the third letter of the code: ')
    guess.append(response.upper())
    response = input('Enter the fourth letter of the code: ')
    guess.append(response.upper())
    # debug code: print(f"in code_breaker_make_guess. Guess is {guess}.")
    return guess

# Following along with class video:
# In the following function we use a debugging method
# that enables us to check each step in a function to see if it ran.
# If it runs it will print out the statement, if not there is a bug 
# where it stops.
def take_turn(code_maker_colors, code_maker_abbreviations):
    print(code_maker_abbreviations)
    # debug code: print("You are in the take_turn function!")
    guess = code_breaker_make_guess()
    # debug code: print("Made it here 1.")
    exact_matches = []
    # debug code: print("Made it here 2")
    position = 0
    # debug code: print("Made it here 3")
    # debugg code: guess = ['ONE', 'TWO', 'THREE', 'FOUR']
    # debug code: print("Made it here 4")
    print(f"guess: {guess}, code_m_a: {code_maker_abbreviations}.")
    for guess_color, actual_color in zip(guess, code_maker_abbreviations):
        print(f'guess_color: {guess_color}, actual_color: {actual_color}.')
        if guess_color == actual_color:
            exact_matches.append(position)
        position += 1
    
    if len(exact_matches) == 4:
        return True

    misplaced_matches = []
    position = 0
    for guess_color in guess:
        if position not in exact_matches:
            misplaced_position = 0
            for misplaced_color in code_maker_abbreviations:
                if guess_color == misplaced_color:
                    if (misplaced_position not in exact_matches) and (misplaced_position not in misplaced_matches):
                        misplaced_matches.append(misplaced_position)
                        break
                misplaced_position += 1
        position += 1
    
    correct_color_correct_position = len(exact_matches)
    correct_color = len(misplaced_matches)

    print(f'You have {correct_color_correct_position} with the correct color and position and {correct_color} more that are the correct color.')
    
    return False


def get_abbreviations(code_maker_colors):
    code_maker_abbreviations = [color[0] for color in code_maker_colors]
    return code_maker_abbreviations


def main():
    response = 'n'
    while response.lower() != 'y':
        code_maker_colors = random.choices(COLORS, k = 4)
        # code_maker_colors = ['GREEN', 'GREEN', 'YELLOW', 'PURPLE']
        # code_maker_colors = ['GREEN', 'BLUE', 'BLUE', 'PURPLE']
        #print(code_maker_colors)
        code_maker_abbreviations = get_abbreviations(code_maker_colors)
        #print(code_maker_abbreviations)
        solved = False
        while not solved:
            #debug code: print(f'cmc: {code_maker_colors}, cma: {code_maker_abbreviations}.')
            solved = take_turn(code_maker_colors, code_maker_abbreviations)
        print(f'Yes! The answer is {code_maker_colors}.')
        response = input('Would you like to quit? (y/n) ')


if __name__ == '__main__':
    main()
