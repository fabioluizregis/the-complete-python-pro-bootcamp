from coffee_libs import current_resources
from coffee_libs import recipes

def select_machine_option(users_selection):
    if users_selection == "expresso":
        print("expresso")
        print(recipes.machine_recipes["expresso"])
    elif users_selection == "latte":
        print("latte")
    elif users_selection == "cappuccino":
        print("cappuccino")
    elif users_selection == "report":
        print()
        print("Machine resources: ")
        print(f"  Water:  {current_resources.machine_resources['water']} ml")
        print(f"  Milk:   {current_resources.machine_resources['milk']} ml")
        print(f"  Coffee: {current_resources.machine_resources['coffee']} g")
        print(f"  Money:  $ {current_resources.machine_resources['money']}")
        print()
    else:
        print("option not available!")