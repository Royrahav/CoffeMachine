from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import menu_and_resources as mr

money_amount = 0
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def report():
    """ Gets info about ingredients status and profits inside the machine. """
    coffee_maker.report()
    money_machine.report()
    return True


def turn_off():
    """ Turns the machine off. """
    print("Bye!")
    return False


def calculate_change_and_price(drink):
    """
    Checks if entered coins are sufficient, returns False if not.
    Also, it calculates the change
    """
    global money_amount
    cost = mr.MENU[drink.name]["cost"]
    print(f"{drink.name} costs ${cost}. How would you like to pay?")
    return money_machine.make_payment(cost)


def validate_drink(drink):
    """
    Checks if selected drink has enough resources and user entered enough coins.
    Returns True if all conditions are met, and False if one of them isn't.
    """
    if not coffee_maker.is_resource_sufficient(drink):
        return False
    if not calculate_change_and_price(drink):
        return False
    return True


def is_drink(drink):
    """ Checks if the entered value is a drink, returns True, or another command, returns False. """
    return menu.find_drink(drink) is not None


def create_drink(choice):
    ingredients = mr.MENU[choice]["ingredients"]
    water = milk = coffee = cost = 0
    if "water" in ingredients:
        water = ingredients["water"]
    if "milk" in ingredients:
        milk = ingredients["milk"]
    if "coffee" in ingredients:
        coffee = ingredients["coffee"]
    if "cost" in ingredients:
        cost = ingredients["cost"]

    return MenuItem(choice, water, milk, coffee, cost)


def machine_on():
    """ Main machine operation func. """
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if is_drink(choice):
        drink = create_drink(choice)
        if validate_drink(drink):
            coffee_maker.make_coffee(drink)

    else:
        if choice == "off":
            return turn_off()
        elif choice == "report":
            return report()
        else:
            pass
    return True


while machine_on():
    pass
