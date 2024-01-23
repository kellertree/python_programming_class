# The High Jump

last_year_personal_record = '6 feet, 2 inches'
current_personal_record = '6 feet, 2.5 inches'
goal = '6 feet, 3 inches'
# todays_jump = last_year_personal_record (a)
# todays_jump = current_personal_record (b)
todays_jump = goal #(c)
# todays_jump = '5 feet, 3 inches' (d)

# a.
if todays_jump == last_year_personal_record:
    print('Good job! That was as good a jump as your jumps last year!')
# b.         
elif todays_jump == current_personal_record:
          print('Awesome! You tied your record!')
# c.
elif todays_jump == goal:
                print("You did it! Way to go!")
                
# d. 
elif todays_jump != (last_year_personal_record or current_personal_record or goal):
                print("Tomorrow is another day.")
        
# The code prints out the first statement under (a)
# The code prints out the second statement under (b)
# The code prints out the third statement under (c)
# The code prints out the fourth statement under (d)