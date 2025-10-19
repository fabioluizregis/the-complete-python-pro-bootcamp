""" This project meant to simulate a simple coffee machine. """
from coffee_libs import current_resources
from coffee_libs import recipes

continue_woking = True

while continue_woking:

    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        continue_woking = False
    elif order == "report":
        print()
        print("Machine resources: ")
        print(f"    Water: {current_resources.machine_resource_itens["water"]} ml")
        print(f"    Milk: {current_resources.machine_resource_itens["milk"]} ml")
        print(f"    Coffee: {current_resources.machine_resource_itens["coffee"]} g")
        print(f"    Money: $ {current_resources.machine_resource_money["money"]}")
        print()
    else:
        current_resources.check_resources(order)
        if current_resources.check_sufficient_money(order):
            print(f"Enjoy your {order}!")
        

