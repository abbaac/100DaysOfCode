from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

resume = True
while resume:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "off":
        resume = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()

    else:
        order = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(order):
            if moneymachine.make_payment(order.cost):
                coffeemaker.make_coffee(order)

            