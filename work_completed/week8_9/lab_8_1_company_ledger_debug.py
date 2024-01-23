
# flags were out of order for while statements.
# checking had missing else statement. 
# the 'not' statement wasn't correct for the task.
accounts = {}

done_entering_savings = True
amounts = []
while done_entering_savings:
    result = input("What is the amount of the next transaction for the company savings account? (Enter 'd' for done if there are no more amounts for savings) ")
    if result.lower() == 'd':
        done_entering_savings = False
        accounts['Savings'] = amounts
    else:
        amounts.append(float(result))
 
done_entering_checking = True
amounts = []
while done_entering_checking:
    result = input("What is the amount of the next transaction for the company checking account? (Enter 'd' for done if there are no more amounts for checking) ")
    if result.lower() == 'd':
        done_entering_checking = False
        accounts['Checking'] = amounts
    else:
        amounts.append(float(result))

done_entering_credit_card = True
amounts = []
while done_entering_credit_card:
    result = input("What is the amount of the next transaction for the company credit card account? (Enter 'd' for done if there are no more amounts for credit cards) ")
    if result.lower() == 'd':
        done_entering_credit_card = False
        accounts['Credit'] = amounts
    else:
        amounts.append(float(result))
    
for account_name in accounts.keys():
    print(f'In {account_name}, the company has: ', end='')
    account_strs = []
    for amount in accounts[account_name]:
        account_strs.append(str(amount))
    account_amount = ', '.join(account_strs)
    print(f' {account_amount}.')

grand_total = 0

for account_name in accounts.keys():
    total = 0  # total needed to be outside of the second for loop.
    for amount in accounts[account_name]:
        total = total + amount
    # Added if else to calculate company's total assets properly.
    if account_name == 'Credit':
        grand_total = grand_total - total
    else:
        grand_total = grand_total + total
   
    # removed f from print statement below.
    # adjusted print indent.
    print(f'The total amount in {account_name} is {total}.') 

print(f"The company's total assets are {grand_total}.")
