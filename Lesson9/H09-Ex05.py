#TODO 5. Design a program that reads a JSON file containing a list of products with names and prices.
# Calculate the total cost of all products and display it.

import json

json_file = "H09-Ex05_json_input.json"
total_price = 0.0

with open(json_file, 'r') as file:
    json_data = json.load(file)
    for row in json_data:
        total_price = total_price+float(row["Price"])

print("The total price of all products from the list is:", total_price)