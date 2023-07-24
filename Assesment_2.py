def get_integer(n):
    user_input = int(input(n))
    return user_input


def get_string(n):
    user_input = input(n)
    return user_input


def reveiw_sandwich(l):
    for x in l:
        output = "{:<10} -- {:>4}".format(x[0], x[1])
        print(output)
    return None


def print_list_index(l):
    for i in range(0, len(l)):
        print("{} : {}".format(i, l[i]))
        # prints list with index numbers
    print("-" * 100)


order = []


def reveiw_order():
    if len(order) == 0:
        print("Your order is empty.")
    else:
        print("Your order:")
        total = 0
        for item in order:
            print(f"{item['name']}: ${item['price']}")
            total += item['price']
        print(f"Total: ${total}")


def main():
    sandwich_list = [
        ["Turkey and Brie sandwich", 15.99],
        ["Thai beef sandwich", 16.00],
        ["Garlic Aioli BLT sandwich", 14.90],
        ["Italian Beef sandwich", 16.90],
        ["Philadelphia Roast Pork sandwich", 16.90],
        ["Mediterranean veggie and haloumi sandwich", 16.00],
        ["Chicken, pear, spinach and celery sandwich", 14.90],
        ["Chicken, brie and cranberry sandwich", 15.99],
        ["Tuna melt with green goddess peas sandwich", 14.90]
    ]


    menu_list = [
        ["P", "Print menu"],
        ["R", "Review order"],
        ["Q", "Quit"]
    ]

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{}: {}".format(x[0], x[1])
            print(output)
        user_choice = get_string("Please select an option: -> ")
        if user_choice == "P":
            reveiw_sandwich(sandwich_list)
        elif user_choice == "R":
            reveiw_order()
        elif user_choice == "Q":
            run_program = False
        else:
            print("Unrecognised entry")
    print("Thank you, the program has ended")


if __name__ == "__main__":
    main()
