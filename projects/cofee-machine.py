MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

# Another dictionary
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

def isMaterialSufficient(ordered_drink):
    requiredResources = ordered_drink['ingredients']
    for item in requiredResources:
        if requiredResources[item] > resources[item]:
            print(f"Sorry, There is not sufficient {item}")
            return False
    return True

def getPayment():
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

def isTransactionSuccessful(payment_received, cost):
    if payment_received < cost:
        print("Sorry that's not enough money. Money refunded.")
        return false
    else:
        change = payment_received - cost
        print(f"Here is ${change} in change.")
        resources['money'] += cost
        return True


def makeDrink(drink_items):
    for item in drink_items:
        resources[item] -= drink_items[item]
    
    
# User may enter: off, report, espresso, latte, cappuccino
# if off -> turn off the machine

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Cofee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        # if resources are sufficient
        if isMaterialSufficient(drink):
            payment = getPayment()
            if isTransactionSuccessful(payment, drink['cost']):
                makeDrink(drink['ingredients'])
                print(f"Here is your {choice} ☕️. Enjoy!")
