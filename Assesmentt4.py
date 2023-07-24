sandwich_list = {
    "1": {"name": "Turkey and Brie sandwich", "price": 15.99},
    "2": {"name": "Thai beef sandwich", "price": 16.95},
    "3": {"name": "Garlic Aioli BLT sandwich", "price": 14.99},
    "4": {"name": "Italian Beef sandwich", "price": 16.95},
    "5": {"name": "Philadelphia Roast Pork sandwich", "price": 16.99},
    "6": {"name": "Mediterranean veggie and haloumi sandwich", "price": 16.50},
    "7": {"name": "Chicken, pear, spinach and celery sandwich", "price": 14.95},
    "8": {"name": "Chicken, brie and cranberry sandwich", "price": 15.99},
    "9": {"name": "Tuna melt with green goddess peas sandwich", "price": 14.95}
}

order_list = []


def get_integer(n):
    user_input = int(input(n))
    return user_input


def get_string(n):
    user_input = input(n)
    return user_input


def reveiw_sandwich(l):
    print("Menu:")
    for key, item in sandwich_list.items():
        print(f"{key}. {item['name']}: ${item['price']}")


def reveiw_order():
    if len(order_list) == 0:
        print("Your order is empty.")
    else:
        print("Your order:")
        total = 0
        for item in order_list:
            print(f"{item['name']}: ${item['price']}")
            total += item['price']
        print(f"Total: ${total}")


def add_item_to_order():
    reveiw_sandwich(sandwich_list)
    print("-" * 100)
    choice = input("Enter the item number to add to your order (1-9): ")
    if choice in sandwich_list:
        item = sandwich_list[choice]
        quantity = int(input("Enter the quantity: "))
        # add in validation for quanitity 
        item["quantity"] = quantity
        order_list.append(item)
        print(f"{quantity} {item['name']}(s) added to your order.")
    else:
        print("Invalid choice. Please try again.")


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
        user_choice = get_string("Please select an option: -> ")
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
            print("Unrecognised entry")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    main()
