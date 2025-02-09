from Day15_menu_resources import MENU, resources
COINS = {"quarters": 25, "dimes": 10, "nickles": 5, "pennies": 1}

def get_unit(ingredient):
    if ingredient == "Water" or ingredient == "Milk":
        return "", "ml"
    elif ingredient == "Coffee":
        return "", "g"
    else:
        return "$", ""

def is_enough_resource(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient]<MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry there is not enough water. ({resources[ingredient]} available vs {MENU[drink]["ingredients"][ingredient]} required)")
            return False
    return True

def is_enough_money(drink):
    print(f"Please insert coins (cost: ${MENU[drink]["cost"]}):")
    money_inserted = 0
    for coin in COINS:
        money_inserted += COINS[coin] * int(input(f"How many {coin}?: "))
    money_inserted = round(money_inserted/100, 2)
    if money_inserted < MENU[drink]["cost"]:
        print("Sorry that is not enough money."
              f"(You inserted ${money_inserted} but it costs ${MENU[drink]["cost"]}.)\n"
              "Your money was refunded.")
        return False
    if money_inserted > MENU[drink]["cost"]:
        print(f"Here is ${round(money_inserted - MENU[drink]["cost"], 2)} in change.")
    resources["money"] +=  MENU[drink]["cost"]
    return True

def deduct_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]

while True:
    
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off":
        print("shutting off the machine...OFF")
        break
    elif command == "report":
        for resource in resources:
            dollar, unit = get_unit(resource.capitalize())
            print(f"{resource.capitalize()}: {dollar}{resources[resource]}{unit}")
    elif command in ["espresso", "latte", "cappuccino"]:
        if not is_enough_resource(command): continue
        if not is_enough_money(command): continue
        deduct_resources(command)
        print(f"Here is your {command}. Enjoy!☕")
    else:
        print("Not a valid command, please try again.")