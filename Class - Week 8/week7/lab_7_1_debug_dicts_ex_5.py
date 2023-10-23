# DEBUG OPTION 1 of 2 (OPTION 2 IS BETTER: It is a more organized and structured way to represent the data.)
#
us_coins = ['dime', 'penny', 'nickel', 'quarter']
latvian_coins = ['5 latu', '10 latu', '20 latu', '50 latu', '100 latu']
nigerian_coins = ['1 Naira', '2 Naira', '50 Kobo']

travelers_coins = []
# Why isn't the following working? Adding lists and lists have the append method.
# travelers_coins was set to an empty dictionary but we cannot append to dictonaries.
travelers_coins.append(us_coins)
travelers_coins.append(latvian_coins)
travelers_coins.append(nigerian_coins)

print(travelers_coins)


# That didn't work. Maybe we need the key?
# We are working with lists so a key won't work in this scenario.
# We could instead change the currency variables into dictionaries though if we wanted to.
#

# DEBUG OPTION 2 of 2
us_coins = {
    'coins': ['dime', 'penny', 'nickel', 'quarter']
    }

latvian_coins = {
    'coins': ['5 latu', '10 latu', '20 latu', '50 latu', '100 latu']
    }

nigerian_coins = {
    'coins': ['1 Naira', '2 Naira', '50 Kobo']
    }

travelers_coins = []

travelers_coins.append(us_coins)
travelers_coins.append(latvian_coins)
travelers_coins.append(nigerian_coins)

print(travelers_coins)

# travelers_coins.append('US Coins', us_coins)
# travelers_coins.append('Latvian Coins', latvian_coins)
# travelers_coins.append('Nigerian Coins', nigerian_coins)