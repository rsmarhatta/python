from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
my_menu = Menu()
money = 0
off = False
while not off:
    userDesire = input("What would you like? (espresso/latte/cappuccino): ")
    if userDesire == 'off':
        off = True
    elif userDesire == 'report':
        coffee_maker.report()
        money_machine.report()
    elif (my_menu.find_drink(userDesire)) and coffee_maker.is_resource_sufficient(my_menu.find_drink(userDesire)):

        if money_machine.make_payment(my_menu.find_drink(userDesire).cost):

            coffee_maker.make_coffee(my_menu.find_drink(userDesire))
