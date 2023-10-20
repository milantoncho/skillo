# Problem 4: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary
# variable. Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart. Allow the user to
# interact with the cart by adding and removing items.

# to do:
# TODO: hide the password input - seem to be pycharm setting ?
# TODO: Exit with Esc instead of with 0 - seem to be pycharm setting ?
# TODO: BG only or ENG only messages
# TODO: Ability to add a book multiple times - ??
# TODO: Proper input validation for the "next_action" function


book_for_sale = {
    1: {"Анна Каренина": 20.00},
    2: {"Война и мир": 29.90},
    3: {"1984": 17.80},
    4: {"100 години самота": 25.00},
    5: {"На Запдният фронт нищо ново": 22.00},
    6: {"Часовници от кости": 35.00},
    7: {"Убийствен джаз": 24.90},
    8: {"Карай плуга си през костите на мъртвите": 14.90},
    9: {"Съучастници": 22.50},
    10: {"Фантом": 20.00},
    11: {"Черната кутия": 12.00}
}

registered_users = {
    10: {"Barak Obama": "usatoday"},
    23: {"Michael Jordan": "mj23"},
    44: {"Anton Danchev": "lh44"},
    11: {"Dear Guest": ""}
}

user_carts = {
    10: {},
    23: {},
    44: {},
    11: {}
}
user_id = 0


def list_of_items(items_dictionary):
    print("Това е списъкът ни с продукти:\n")
    for item_id, item_details in book_for_sale.items():
        item_title, item_price = list(item_details.items())[0]  # това е малко на магия... малко неясно...
        print(f"Книга: {item_title:<44} Цена: {item_price:<8.2f} Book ID: {item_id} ")
    print()


def credentials_verification(users_dictionary):
    global user_id
    i = 3
    while i > 0:
        input_user_id = int(input("Bъведете вашето потребителко ID и парола (или 0 за изход)\n"
                                  "(За вход, като гост изплозвайте User ID: 11, без парола)\n\nUser Id: "))
        if input_user_id == 0:
            print("Излизане...")
            return
        else:
            input_password = input("Password: ")
        if input_user_id in users_dictionary and input_password == users_dictionary[input_user_id][
            next(iter(users_dictionary[input_user_id].keys()))]:
            print(f"Welcome, {next(iter(users_dictionary[input_user_id].keys()))}!")
            user_id = input_user_id
            return
        else:
            print("Incorrect credentials")
            i = i - 1
            print("Remaining retries:", i)
    print("Излизане...")


def adding_to_the_shopping_cart():
    while True:
        book_id = int(input("\nBook ID: "))
        if book_id == 0:
            print("Край на добавянето на продукти...")
            print("Сума за плащане: {:.2f}".format(sum(user_carts[user_id].values())), "lv.")
            next_action()
            break
        elif book_id not in book_for_sale.keys():
            print("No such ID")
        else:
            user_carts[user_id].update(book_for_sale[book_id])
            print("Cart content:")
            added_to_the_shopping_cart(user_id)


def added_to_the_shopping_cart(some_user_id):
    print("\nCart items:")
    for item, price in user_carts[some_user_id].items():
        print(f"Книга: {item:<44} Цена: {price:<4.2f} лв.")
    print("=" * 67)
    print("Total price: {:50.2f}".format(sum(user_carts[user_id].values())), "lv.\n")


def next_action():
    next_action = 1
    while next_action not in range(2, 5):
        next_action = int(input("\nWhat would you like to do next?\n"
                                "1 - review the shopping cart\n"
                                "2 - add new items to the shopping cart\n"
                                "3 - remove items from the shopping cart\n"
                                "4 - review the the products\n"
                                "5 - proceed to checkout\n"
                                "0 - exit\n"
                                "Your choice: "))
        if next_action == 1:
            added_to_the_shopping_cart(user_id)
        elif next_action == 2:
            adding_to_the_shopping_cart()
        elif next_action == 3:
            print("Removing...")
            removing_from_the_cart(user_id)
            return
        elif next_action == 4:
            list_of_items(book_for_sale)
            next_action = 0
        elif next_action == 5:
            print("Proceed to checkout...")
            return
        elif next_action == 0:
            print("Exiting...")
            return


def removing_from_the_cart(some_user_id):
    added_to_the_shopping_cart(user_id)
    item_to_remove = input("Item to remove: ")
    if item_to_remove in user_carts[user_id]:  # Check if the key exists in the dictionary
        del user_carts[user_id][item_to_remove]  # Remove the key-value pair with key 2
        added_to_the_shopping_cart(user_id)
    else:
        print("No such item")
    next_action()


list_of_items(book_for_sale)

print("Ако желаете да добавите продукти към кошницата си")

credentials_verification(registered_users)

print("Изберете ID на книга, за да я добавите в кошницата си (или 0 за край)")

adding_to_the_shopping_cart()
