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
    for i in range(len(order_list)):
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


import re


def get_phone_number(m):
    while True:
        phone_number = input("Please enter your phone number (xxx-xxx-xxxx): (+64) ")
        if validate_phone_number(phone_number):
            return phone_number
        else:
            print("Invalid phone number. Please enter a valid phone number.")


def validate_phone_number(phone_number):
    # Define a simple pattern for a valid phone number (e.g., xxx-xxx-xxxx)
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return pattern.match(phone_number)


def get_details(ll):
    # have to get it so that if they press g again after entering details it prints what has already been done and if
    # they want to edit it also the phone number validation and the printing of the details after getting them
    # loop and deleting and checking everything
    # more validation
    print("Getting customer details")
    print(customer_details)

    users_option = get_option("(P)ickup or (D)ilivery? ")
    customer_details['Delivery Type'] = users_option

    user_name = get_string("Please enter customer name: ")
    customer_details['Name'] = user_name

    user_number = get_phone_number("")
    customer_details['Phone Number'] = user_number

    if users_option == "D":
        print("Getting delivery information")
        address_1 = get_string("Please enter address line 1: ")
        customer_details['Address Line One'] = address_1
        address_2 = get_string("Please enter address line 2: ")
        customer_details['Address Line Two'] = address_2
        print("Delivery order")
    elif users_option == "P":
        print("Pickup order")
    else:
        print("ERROR - returning to main menu")

    print(customer_details)
    correct_info = get_option("If these details are correct enter C and if they are incorrect please enter I: ")
    if correct_info == 'C':
        print("Info saved")
        print(customer_details)
    elif correct_info == 'I':
        print("Deleting all info please enter details again")
        customer_details['Delivery Type'] = ""
        customer_details['Name'] = ""
        customer_details['Phone Number'] = "'"
        customer_details['Address Line One'] = ""
        customer_details['Address Line Two'] = ""
        print(customer_details)
    else:
        print("ERROR")


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
            get_details(customer_details)
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

    customer_details = {
        "Delivery Type": "",
        "Name": "",
        "Phone Number": "",
        "Address Line One": "",
        "Address Line Two": ""
    }

    main()
