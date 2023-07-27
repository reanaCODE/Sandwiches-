sandwich_list = {
    "1": {"quantity": "-", "name": "Turkey and Brie sandwich", "price": 15.99},
    "2": {"quantity": "-", "name": "Thai beef sandwich", "price": 16.95},
    "3": {"quantity": "-", "name": "Garlic Aioli BLT sandwich", "price": 14.99},
    "4": {"quantity": "-", "name": "Italian Beef sandwich", "price": 16.95},
    "5": {"quantity": "-", "name": "Philadelphia Roast Pork sandwich", "price": 16.99},
    "6": {"quantity": "-", "name": "Mediterranean veggie and haloumi sandwich", "price": 16.50},
    "7": {"quantity": "-", "name": "Chicken, pear, spinach and celery sandwich", "price": 14.95},
    "8": {"quantity": "-", "name": "Chicken, brie and cranberry sandwich", "price": 15.99},
    "9": {"quantity": "-", "name": "Tuna melt with green goddess peas sandwich", "price": 14.95}
}

order_list = []


def get_integer(m, lower, upper):
    getting_integer = True
    while getting_integer is True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please enter an integer")
            continue
        if user_input > upper or user_input < lower:
            print("Please enter a valid value")
        else:
            return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def get_key(m, l, u):
    key = get_integer(m, l, u)
    return str(key)


def get_option(m):
    get_letter = True
    while get_letter is True:
        user_input = input(m).upper().strip()
        if len(user_input) != 1:
            print("One character needed")
        elif user_input.isdigit():
            print("I need a letter please try again")
        else:
            return user_input


def reveiw_sandwich(l):
    print("Menu:")
    for key, item in sandwich_list.items():
        print(f"{key}: {item['name']}: ${item['price']}")


def reveiw_order():
    if len(order_list) == 0:
        print("Your order is empty.")
    else:
        print("Your order:")
        total_amount = 0
        for item in order_list:
            print(f"{item['quantity']} {item['item']} - ${item['total_price']}")
            total_amount += item['total_price']
        print(f"Total: ${total_amount:.2f}")


def add_item_to_order():
    reveiw_sandwich(sandwich_list)
    print("-" * 100)
    choice = get_key("Enter the item number to add to your order (1-9): ", 1, 9)
    if choice in sandwich_list:
        item = sandwich_list[choice]
        quantity = int(input("Enter the quantity you want to order: "))
        item = sandwich_list[choice]['name']
        price = sandwich_list[choice]['price']
        total_price = price * quantity
        order_list.append({"item": item, "quantity": quantity, "total_price": total_price})
        print(f"{quantity} {item}(s) added to your order.")
    else:
        print("Error, should have a correct key for the sandwich ")


def delet_order():
    reveiw_sandwich()


def main():
    menu_list = [
        ["P", "Print menu"],
        ["R", "Review order"],
        ["A", "Add Item to order"],
        ["Q", "Quit"]
    ]

    run_program = True
    while run_program:
        print("-" * 100)
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_option("Please select an option: -> ")
        print("-" * 100)
        if user_choice == "P":
            reveiw_sandwich(sandwich_list)
        elif user_choice == "R":
            reveiw_order()
        elif user_choice == "A":
            add_item_to_order()
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry, please enter a presented letter")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    main()
