MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
    
def check_resources(drink_list):
    for i in drink_list:
        if drink_list[i] > resources[i]:
            return f"Sorry there is not enough {i}."
        else:
            return True
    
def pay(order):
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    cost = MENU[order]['cost']
    
    if total < cost:
        return "Sorry that's not enough money. Money refunded."
    else:
        if total > cost:
            change = total - cost
            print("Heres $" + '{:.2f}'.format(change) + " dollars in change")
        for i in MENU[order]["ingredients"]:
            resources[i] -= MENU[order]['ingredients'][i]  
        resources["money"] += cost  
        return  f"Here is your {order} ☕. Enjoy!"


def dispense():
    resume = True
    while resume:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            resume = False
        elif choice == "report":
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if check_resources(drink['ingredients']) == True:
                print(pay(choice))
            else:
                print(check_resources(drink))
        else:
            print("We don't have that.")





dispense() 


