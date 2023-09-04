import re


def get_integer(m, lower, upper):
    # getting a number from the user - validation
    getting_integer = True
    while getting_integer is True:
        try:
            user_input = int(input(m))
        except ValueError:
            print("Please enter an integer")
            # if they enter anything but a number
            continue
        if user_input > upper or user_input < lower:
            print("Please enter a valid value")
            # if they enter too many or not enough/not valid enough number/s
        else:
            return user_input


def get_string(m):
    user_input = input(m)
    return user_input


def get_key(m, l, u):
    key = get_integer(m, l, u)
    # had to add this because there was an error with getting an integer validation
    return str(key)


def get_option(m):
    # validation for when user has to enter one letter
    get_letter = True
    while get_letter is True:
        user_input = input(m).upper().strip()
        # changes all letters to uppercase and takes away the spaces (strip)
        if len(user_input) != 1:
            print("One character needed")
            # if the user enters multiple characters
        elif user_input.isdigit():
            print("I need a letter please try again")
            # if they enter a number
        else:
            return user_input


def reveiw_sandwich(l):
    # prints the sandwich list to user
    print("Menu:")
    for key, item in sandwich_list.items():
        print(f"{key}: {item['name']}: ${item['price']}")


def reveiw_order():
    # prints the order list to user to see what they have in their order
    if len(order_list) == 0:
        # if they have added nothing to their order
        print("Your order is empty.")
    else:
        print("Your order:")
        total_amount = 0
        for item in order_list:
            print(f"#{item['quantity']} {item['item']} - ${item['total_price']}")
            # prints the quality and the item of what they have chosen and the price of that
            # then it calculates the total price and prints it ot the user
            total_amount += item['total_price']
        if customer_details['Delivery Type'] == "D":
            total_amount += 3
            print(" +$3 for delivery")
        print(f"Total: ${total_amount:.2f}")


def get_index():
    print("Your order")
    for i in range(len(order_list)):
        for item in order_list:
            # prints the users order list with indexes for the editing order function
            print(f"{i}: #{item['quantity']} {item['item']}")


def add_item_to_order():
    reveiw_sandwich(sandwich_list)
    # function of adding a sandwich to order list and prints out the sandwich menu to choose from
    print("-" * 100)
    choice = get_key("Enter the item number to add to your order (1-9), enter 0 to cancel: ", 0, 9)
    if choice in sandwich_list:
        item = sandwich_list[choice]
        quantity = get_integer("Enter the quantity you want to order: ", 0, 20)
        # ask for the quantity of the item the user wants to order
        item = sandwich_list[choice]['name']
        price = sandwich_list[choice]['price']
        total_price = price * quantity
        # adding it to the order list (reveiw order) with the quality and the total price
        order_list.append({"item": item, "quantity": quantity, "total_price": total_price})
        print(f"{quantity} {item}(s) added to your order.")
    else:
        print("ERROR/canceled function... Returning to main menu")
        # incase an error occurs
        return None


def start_new_order():
    # funtion to delete and start a new order
    global order_list
    order_list = []
    print('Previous order deleted and new order started.')


def edit_order():
    if len(order_list) == 0:
        print("Your order is empty.")
        return None

    # function to edit the order )either deleting an item or changing the quantity

    get_index()
    choice = get_option("Would you like to (E)dit the quantity, (D)elete an item, or (C)ancel this function: ")
    # adding the C to cancel this function incase the user made a mistake

    if choice == "C":
        print("Returning to main menu/Canceling this function")
        return None
    choice_num = get_integer("Enter the index number you would like to edit/delete: ", 0, len(order_list) - 1)
    if choice == "E":
        # editing the quantity of an item of the order
        for item in order_list:
            print(f"You have # {item['quantity']} of {item['item']}")
            new_value = get_integer("What would you like to change the quantity to: ", 0, 20)
            item_price = item['total_price'] / item['quantity']
            order_list[choice_num]['quantity'] = new_value
            order_list[choice_num]['total_price'] = new_value * item_price
            print("Order Successfully updated")
    elif choice == "D":
        print("Order updated")
        # deleting an item in order list
        order_list.pop(choice_num)
    else:
        print("Unrecognised entry, please try again")
        return None


def get_phone_number(m):
    # Getting the phone number in customer details
    while True:
        phone_number = input("Please enter your phone number (xxx-xxx-xxxx): (+64) ")
        # put xxx-xxx-xxxx to show user the way they must enter the phone number otherwise it will not work
        if validate_phone_number(phone_number):
            return phone_number
        else:
            print("Invalid phone number. Please enter a valid phone number.")


def validate_phone_number(phone_number):
    # Define a simple pattern for a valid phone number (e.g., xxx-xxx-xxxx)
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return pattern.match(phone_number)


# validation of phone number

def get_details(l):
    # have to get it so that if they press g again after entering details it prints what has already been done and if
    # they want to edit it also printing of the details after getting them
    # loop and deleting and checking everything
    # more validation
    global customer_details
    print("Getting customer details")
    if customer_details['Name'] != "":
        print(customer_details)
        # if customer has already entered their details in customer details
        print("You have already entered your details - ")
        again = get_option("Please enter A if you would like to start again and Q if these are correct: ")
        if again == 'A':
            print("Customer details have been reset")
            # if they want to start again, re set the dictionary
            customer_details = dict.fromkeys(customer_details, "")
            return again
        elif again == 'Q':
            # if they want to go back to main menu so the info is correct
            print("Customer details are staying the same - returning to main menu")
            return None
        else:
            print("ERROR - retuning to main menu")
            return None

    users_option = get_option("(P)ickup or (D)ilivery? ")
    customer_details['Delivery Type'] = users_option

    user_name = get_string("Please enter customer name: ")
    customer_details['Name'] = user_name

    user_number = get_phone_number("")
    customer_details['Phone Number'] = user_number

    if users_option == "D":
        # if the user chooses the dilivery option
        print("Getting delivery information")
        address_1 = get_string("Please enter address line 1: ")
        customer_details['Address Line One'] = address_1
        address_2 = get_string("Please enter address line 2: ")
        customer_details['Address Line Two'] = address_2
        print("Delivery order")
    elif users_option == "P":
        # if they choose pickup option
        print("Pickup order")
    else:
        print("ERROR - returning to main menu")

    print(customer_details)
    correct_info = get_option("If these details are correct enter C and if they are incorrect please enter I: ")
    # checking if the information the user entered is correct and going form there based on their answer
    if correct_info == 'C':
        print("Info saved")
        print(customer_details)
    elif correct_info == 'I':
        print("Deleting all info please enter details again")
        # clears all the info the user entered they can start again to enter the correct details
        customer_details = dict.fromkeys(customer_details, "")
        print(customer_details)
    else:
        print("ERROR")
        return None


def confirm_order():
    # function to confirm and execute the order
    print(customer_details)
    print(reveiw_order())
    confirm = get_option("If this information is correct please enter C and if they are incorrect please enter I: --> ")
    # once again asking the user if the info they have entered is correct
    if confirm == "C":
        print("Details confirmed")
        print("Confirmation for order needed. After confirmation cancellation is not an option")
        # informing the user that after they confirm there is no going back
        order_confirm = get_option("Please enter C to confirm or Q to go back to main menu: --> ")
        if order_confirm == "C":
            print("Confirmation accepted - you will be notified when the order is ready/on the way!")
            print("Thank you and enjoy your Sandwich(s)!!")
            # having fully confirmed order
            # need to stop program here
            return order_confirm
            # just goes back to main menu and user can quit the program from their or start their new order
        elif order_confirm == "Q":
            print("Returning to main menu")
            # if the info is not correct, or they do not wish to confirm order
            return None
        else:
            print("ERROR - returning to main menu")
            return None
    elif confirm == "I":
        print("Details incorrect - returning to main menu")
        return None
    else:
        print("ERROR - returning to main menu")
        return None


def main():
    global customer_details
    # menu list for the user to choose from
    menu_list = [
        ["P", "Print menu"],
        ["R", "Review order"],
        ["A", "Add Item to order"],
        ["S", "Delet order and start anew order"],
        ["E", "Edit order"],
        ["G", "Get details"],
        ["C", "Confirm Order and details"],
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
            # shows sandwich menu
            reveiw_sandwich(sandwich_list)
        elif user_choice == "R":
            # shows the order menu
            reveiw_order()
        elif user_choice == "A":
            # adding an item/sandwich to the order list
            add_item_to_order()
        elif user_choice == "S":
            # deleting and starting a new order
            start_new_order()
        elif user_choice == "E":
            # editing order - either edit the quantity or delete an item, option to cancel this function incase mistake
            edit_order()
        elif user_choice == "G":
            # getting the details (dilivery or pickup) and phone number and address and name
            get_details(customer_details)
        elif user_choice == "C":
            # confirming all details (customer info and order list0 user can confirm or cancel funtion, but
            # they would need to delete the info in different functions
            confirm = confirm_order()
            if confirm == "C":
                # clear the order list
                order_list.clear()
                # s et the dictionary back to empty state
                customer_details = dict.fromkeys(customer_details, "")
                print("Starting new order")
        elif user_choice == "Q":
            # ending program without confirming an order so everything becomes deleted
            run_program = False
        else:
            print("Unrecognised entry, please enter a presented letter")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    # list of different sandwiches with pricing
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
    # the list with the items the user has added to their order

    customer_details = {
        "Delivery Type": "",
        "Name": "",
        "Phone Number": "",
        "Address Line One": "",
        "Address Line Two": ""
    }
    # customer details list for the customer info function/ part of program

    main()
