#TODO 9. Provide an example XML file, "inventory.xml," that represents a list of products in a store.
# Write a Python program to read this XML file and print the names and prices of all products.

import xml.etree.ElementTree as ET

xml_file = "H09-Ex09_xml_input.xml"

parse_xml = ET.parse(xml_file)
xml_data = parse_xml.getroot()

for product in xml_data.findall('Product'):
    name = product.find('Name').text
    price = product.find('Price').text
    print(f"Name: {name}, Price: {price}")