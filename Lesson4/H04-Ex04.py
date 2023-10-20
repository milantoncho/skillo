# Problem 4: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary
# variable. Every customer has unique id as a key. Define functions to add items to the cart,
# remove items, calculate the total price, and display the contents of the cart. Allow the user to
# interact with the cart by adding and removing items.

# to do:
# - hide the password input
# - Exit with Esc instead of with 0
# - BG only or ENG only messages
# - Ability to add a book multiple times

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
    10:{"Фантом": 20.00},
    11:{"Черната кутия": 12.00}
}

registered_users = {
    10: {"Barak Obama": "usatoday"},
    23: {"Michael Jordan": "mj23"},
    44: {"Anton Danchev": "lh44"},
    11: {"Dear Guest": "g"}
}

user_carts = {
    10: {},
    23: {},
    44: {},
    11: {}
}
user_id=0

def list_of_items(items_dictionary):
    print("Това е списъкът ни с продукти:\n"
          "(За вход, като гост изплозвайте User ID: 11 и парола: g)\n")
    for item_id, item_details in book_for_sale.items():
        item_title, item_price = list(item_details.items())[0] #това е малко на магия... малко неясно...
        print(f"Книга: {item_title:<44} Цена: {item_price:<8.2f} Book ID: {item_id} ")
    print()

def credentials_verification(users_dictionary):
    global user_id
    i = 3
    while i > 0:
        input_user_id = int(input("\nBъведете вашето потребителко ID и парола (или 0 за изход):\n\nUser Id: "))
        if input_user_id == 0:
            print("Излизане...")
            return
        else:
            input_password = input("Password: ")
        if input_user_id in users_dictionary and input_password == users_dictionary[input_user_id][next(iter(users_dictionary[input_user_id].keys()))]:
            print(f"Welcome, {next(iter(users_dictionary[input_user_id].keys()))}!")
            user_id = input_user_id
            return
        else:
            print("Incorrect credentials")
            i = i-1
            print("Remaining retries:", i)
    print("Излизане...")

def adding_to_the_shopping_cart():
    while True:
        book_id = int(input("\nBook ID: "))
        if book_id == 0:
            print ("Изход...")
            print ("Сума за плащане: {:.2f}".format(sum(user_carts[user_id].values())), "lv.")
            break
        elif book_id not in book_for_sale.keys():
            print ("No such ID")
        else:
            user_carts[user_id].update(book_for_sale[book_id])
            print ("Cart content:")
            added_to_the_shopping_cart(user_id)

def added_to_the_shopping_cart(some_user_id):
    for item, price in user_carts[some_user_id].items():
        print (f"Книга: {item:<44} Цена: {price:<4.2f} лв.")
    print ("="*67)
    print("Total price: {:50.2f}".format(sum(user_carts[user_id].values())), "lv.\n")


list_of_items(book_for_sale)

print("Ако желаете да добавите продукти към кошницата си")

credentials_verification(registered_users)

print ("Изберете ID на книга, за да я добавите в кошницата си (или 0 за край)")

adding_to_the_shopping_cart()

print("\nCart items:")

added_to_the_shopping_cart(user_id)


