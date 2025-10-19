from coffee_libs import recipes

machine_resource_itens = {
    'water': 300,
    'milk': 200,
    'coffee': 100
}

machine_resource_money = {
    'money': 0
}

def check_resources(order):
    have_enough_resources = True
    for item in machine_resource_itens:
        if machine_resource_itens[item] >= recipes.machine_recipes[order][item]:
            have_enough_resources = True
        else:
            print(f"Not enough resources for {machine_resource_itens[item]}")
            have_enough_resources = False
    return have_enough_resources

def check_sufficient_money(order):
    deposit = int(input("How many quarters are you going to insert?: ")) * 0.25
    deposit += int(input("How many dimes are you going to insert?: ")) * 0.10
    deposit += int(input("How many nickles are you going to insert?: ")) * 0.05
    deposit += int(input("How many pennies are you going to insert?: ")) * 0.01

    if deposit >= recipes.machine_recipes[order]["price"]:
        change =  round(deposit - recipes.machine_recipes[order]["price"], 2)
        print(f"You received a change of ${change}")

        machine_resource_money["money"] += round((deposit - change),2)
        for item in machine_resource_itens:
            machine_resource_itens[item] -= recipes.machine_recipes[order][item]
        return True
    else:
        print(f"{order} cost ${recipes.machine_recipes[order]["price"]}")
        print(f"Sorry, ${deposit} is not enough money. Money reofunded.")
        return False