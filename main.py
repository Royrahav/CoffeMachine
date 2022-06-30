import menu_and_resources as mr

money_amount = 0


def calculate_price(money_map):
    amount = 0
    for x in money_map:
        amount += money_map[x][0] * money_map[x][1]
    return amount


def process_coins():
    money_map = {
        "quarters": [int(input("How many quarters ($0.25)? ")), 0.25],
        "dimes": [int(input("How many dimes ($0.1)? ")), 0.1],
        "nickles": [int(input("How many nickles? ($0.05)")), 0.05],
        "pennies": [int(input("How many pennies? ($0.01)")), 0.01]
    }
    amount = calculate_price(money_map)
    return amount


def check_resources(drink):
    ingredients = mr.MENU[drink]["ingredients"]
    for x in mr.resources:
        if x in ingredients:
            if mr.resources[x] < ingredients[x]:
                print(f"Sorry there is not enough {x}.")
                return False
    return True


def report():
    measurement = ""
    for x in mr.resources:
        if x.lower() == "water" or x.lower() == "milk":
            measurement = "ml"
        elif x.lower() == "coffee":
            measurement = "g"
        print(f"{x}: {mr.resources[x]}{measurement}")
    print(f"Money: ${money_amount}")
    return True


def turn_off():
    print("Bye!")
    return False


def calculate_change_and_price(drink):
    global money_amount
    cost = mr.MENU[drink]["cost"]
    print(f"{drink} costs &{cost}. How would you like to pay?")
    inserted_coins_value = process_coins()
    change = 0
    if inserted_coins_value < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif inserted_coins_value > cost:
        change = inserted_coins_value - cost
    money_amount += inserted_coins_value - change
    if change:
        print(f"Here is ${round(change, 2)} dollars in change.")
    return True


def validate_drink(drink):
    if not check_resources(drink):
        return False
    if not calculate_change_and_price(drink):
        return False
    return True


def is_drink(drink):
    if drink in mr.MENU:
        return True
    return False


def update_ingredients(drink):
    ingredients = mr.MENU[drink]["ingredients"]
    for x in ingredients:
        mr.resources[x] -= ingredients[x]


def machine_on():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if is_drink(choice):
        if validate_drink(choice):
            update_ingredients(choice)
            print(f"“Here is your {choice}. Enjoy!")
            return True

    else:
        if choice == "off":
            return turn_off()
        elif choice == "report":
            return report()
        else:
            print("Oops... We don't have that one yet!")
    return True


while machine_on():
    pass
