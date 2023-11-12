#TODO 6. Write a Python script that reads a JSON file, "contacts.json," containing contact information (name, email, phone).

import json

json_file = "H09-Ex06_json_input.json"

with open(json_file, 'r') as file:
    json_data = json.load(file)
    for row in json_data:
        print(f"Name: {row['name']}, Email: {row['email']}, Phone: {row['phone']}")



# Условието изглежда непълно...