import sys

profit = 0

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO 1. Prompt user
def whatCoffee():
    print("Hello, what would you like? (espresso/latte/cappuccino)")


# TODO 3. Print report
def printResources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print("Water: " + str(water) + 'ml')
    print("Milk: " + str(milk) + 'ml')
    print("Coffee: " + str(coffee) + 'g')

    if "money" in resources:
        money = resources["money"]
        print("Money: $" + str(money))


def checkIfSufficentResources(order_ingredients):
    """Returns True when sufficient amount of resources in dict"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True



def processCoins():
    """Returns the total amount of coins inserted """
    print("Please insert coins.")
    amount = int(input("how many quarters? ")) * 0.25
    amount += int(input("how many dimes? ")) * 0.10
    amount += int(input("how many nickles? ")) * 0.05
    amount += int(input("how many pennies? ")) * 0.01
    return amount


def checkTransaction(moneyReceived, drinkCost):
    """ Returns true when the payment is accepted. """
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drinkCost
        return True
    else:
        print("Sorry thats not enough money. Money refunded")
        return False


def dispenseCoffee(drinkName, orderIngredients):
    """Deduct requred ingredients from machine"""
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here is your {drinkName}  ☕. Enjoy")


whatCoffee()

is_on = True
while is_on:
    response = input()
    if response == "off":
        is_on = False
        sys.exit("Machine is off")
    elif response == "report":
        printResources()
    else:
        drink = MENU[response]
        if checkIfSufficentResources(drink["ingredients"]):
            payment = processCoins()
            if checkTransaction(payment, drink["cost"]):
                dispenseCoffee(response, drink["ingredients"])
