from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MachineOn = True
drinks = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while MachineOn:
    command = input(f"What drink you want ({drinks.get_items()})?: ")
    if command == "off":
        MachineOn = False
        continue
    elif command == "report":
        coffee_machine.report()
        money_machine.report()
    elif command in drinks.get_items():
        drink = drinks.find_drink(command)
        if not coffee_machine.is_resource_sufficient(drink): continue
        if not money_machine.make_payment(drink.cost): continue
        coffee_machine.make_coffee(drink)
    else:
        print("That is not a valid drink. Try again.")


print("machine turning off...OFF")