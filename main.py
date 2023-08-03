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
            print(f"#{item['quantity']} {item['item']} - ${item['total_price']}")
            total_amount += item['total_price']
        print(f"Total: ${total_amount:.2f}")


def get_index():
    print("Your order")
    for i in range(0, len(order_list)):
        for item in order_list:
            print(f"{i}: #{item['quantity']} {item['item']}")


def add_item_to_order():
    reveiw_sandwich(sandwich_list)
    print("-" * 100)
    choice = get_key("Enter the item number to add to your order (1-9), enter 0 to cancel: ", 0, 9)
    if choice in sandwich_list:
        item = sandwich_list[choice]
        quantity = get_integer("Enter the quantity you want to order: ", 0, 20)
        item = sandwich_list[choice]['name']
        price = sandwich_list[choice]['price']
        total_price = price * quantity
        order_list.append({"item": item, "quantity": quantity, "total_price": total_price})
        print(f"{quantity} {item}(s) added to your order.")
    else:
        print("ERROR/canceled function... Returning to main menu")
        return None


def start_new_order():
    global order_list
    order_list = []
    print('Previous order deleted and new order started.')


def edit_order():
    if len(order_list) == 0:
        print("Your order is empty.")
        return None

    get_index()
    choice = get_option("Would you like to (E)dit the quantity, (D)elete an item, or (C)ancel this function: ")
    if choice == "C":
        print("Returning to main menu/Canceling this function")
        return None
    choice_num = get_integer("Enter the index number you would like to edit/delete: ", 0, len(order_list) - 1)
    if choice == "E":
        for item in order_list:
            print(f"You have # {item['quantity']} of {item['item']}")
            new_value = get_integer("What would you like to change the quantity to: ", 0, 20)
            order_list[choice_num]['quantity'] = new_value
            print("Order Successfully updated")
    elif choice == "D":
        print("Order updated")
        order_list.pop(choice_num)
    else:
        print("Unrecognised entry, please try again")
        return None


def get_phone_number(m):
    user_input = input(m)
    return user_input


def get_details():
    print("Get customer details")
    users_option = get_option("(P)ickup or (D)ilivery? ")
    if users_option == "D":
        print("Get full information")
        user_name = get_string("Please enter customer name: ")
        address_1 = get_string("Please enter address line 1: ")
        address_2 = get_string("Please enter address line 2: ")
        user_number = get_phone_number("Please enter phone number (NZ/international mobile/land-line): ")
        print("The phone number you have entered is {}".format(user_number))
        # how to print the phone number like --- --- ----- above
        confirm_number = get_option("Please confirm Y/N: -> ")
        if confirm_number == "Y":
            print("Phone Number accepted")
            print("The current customer details are as loaded: ")
            print("Name      : {}".format(user_name))
            print("Address_1 : {}".format(address_1))
            print("Address_2 : {}".format(address_2))
            print("Phone     : {}".format(user_number))
            print("-" * 100)
            confirm_details = get_option("Would you like to confirm your information Y/N: -> ")
            if confirm_details == "Y":
                print("-" * 100)
                print("Order details updated")
            elif confirm_details == "N":
                print("Returning to main menu")
                return None
            else:
                print("ERROR - returning to main menu")
        elif confirm_number == "N":
            print("Phone Number not confirmed - returning to main menu")
    elif users_option == "P":
        print("Get full information")
        user_name = get_string("Please enter your name: ")
        user_number = get_string("Please enter your phone number ")
        confirm_info = get_option("Enter 'E' if your details: {}, {}, are correct: ".format(user_name, user_number))
    else:
        print("ERROR - returning to main menu")


def main():
    menu_list = [
        ["P", "Print menu"],
        ["R", "Review order"],
        ["A", "Add Item to order"],
        ["S", "Delet order and start anew order"],
        ["E", "Edit order"],
        ["G", "Get details"],
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
        elif user_choice == "S":
            start_new_order()
        elif user_choice == "E":
            edit_order()
        elif user_choice == "G":
            get_details()
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry, please enter a presented letter")
    print("Thank you, the program has ended")


if __name__ == "__main__":
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
    main()
