# Coffee machine project


###### Key points
# 3 hot flavors ( expresso, latter and capuccino)
# coins operate
# automatic cup dispenser
# counting cup selling

###### Analytic table
# water inlet
# coin slot
# coin acceptor
# lcd display
# drink 1
# drink 2
# drink 3
# +
# - 
# menu
# drink outlet
# waste water box




# coins
# Penny = 1 cent
# Nickel = 5 cents
# Dime = 10 cents
# quarter = 25 cents

# report to show resources left ( water, milk, coffee, money)
# check resource sufficient ()
# process coins ()
# check transaction successful()

# suficient resources and money = make the coffee and update resources

from coffee_libs import prompting

continue_working = True
while continue_working:
    user_option = input("What would you like? (expresso / latte / cappucino): ").lower()

    if user_option == "off":
        continue_working = False
        print("Turning off machine....")
        
    else:
        prompting.select_machine_option(user_option)