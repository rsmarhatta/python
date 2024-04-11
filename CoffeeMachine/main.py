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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machineoff= False

# TODO print all the resources available

def printReport():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    return print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}")

# TODO check if resources are avialble for the drink requested
def checkResources(drinkchosen,enoughmoney):
    """Check if there are enough resource available for the drink requested."""
    menudrink = MENU[drinkchosen]

    waterAvail = resources['water']
    milkAvail = resources['milk']
    coffeeAvail = resources['coffee']


    # if menudrink["cost"] > money:
    #     print(f"Sorry not enough money to buy {drinkchosen}")
    #     return False
    if menudrink["ingredients"]["water"] > waterAvail:
        print("Not Enough water")
        return False
    elif drinkchosen != 'espresso' and menudrink["ingredients"]["milk"] > milkAvail:
        print("Not Enough milk")
        return False
    elif menudrink["ingredients"]["coffee"] > coffeeAvail:
        print("Not Enough coffee")
        return False
    else:
        #everything is available so subtract it
        if(enoughmoney):
            if(menudrink["ingredients"].get("milk",-1) > -1 ):
                resources['water'] -= menudrink["ingredients"]["water"]
                resources['milk'] -= menudrink["ingredients"]["milk"]
                resources['coffee'] -= menudrink["ingredients"]["coffee"]
            else:
                resources['water'] -= menudrink["ingredients"]["water"]
                resources['coffee'] -= menudrink["ingredients"]["coffee"]

        return True

def calculateMoney(quarter,dime,nickel,penny):
    total = (0.25*quarter) + (0.1*dime)+ (0.05*nickel)+(0.01*penny)
    return total

def calculateChange(userPay,drinkordered):
    drinkmoney = MENU[drinkordered]["cost"]
    global money
    if(userPay > drinkmoney):
        change = (userPay - drinkmoney)
        print(f"Here is ${change} in change.\nEnjoy your {drinkordered}☕💕")
        money -= change
        checkResources(drinkordered, True)
    elif(drinkmoney > userPay):
        money -= (userPay)
        print(f"Sorry not enough money to buy {drinkordered} 😓. Money refunded 🪙")
    else:
        print(f"Here is your {drinkordered}☕ Enjoy! 😊")
        checkResources(drinkordered, True)

while not machineoff:
# TODO: prompt user
    userDesire = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if userDesire == 'report':
        printReport()
    elif userDesire == 'off':
        machineoff=True

    # printReport()
    # print(f"User desire = {userDesire}")
    # print(checkResources(userDesire))
    #printReport()
    else:
        #printReport()
    #menudrink = MENU[userDesire]
    #if we have enough resources ask for money
        if checkResources(userDesire,False):
            print("Please insert coins.")
            quarter = int(input("How many quarters? "))
            dime = int(input("How many dimes? "))
            nickel = int(input("How many nickels? "))
            penny = int(input("How many pennies? "))
            userPay = calculateMoney(quarter,dime,nickel,penny)
            money += userPay
            #print(f"Money is = {money}")
            calculateChange(userPay,userDesire)


#printReport()






