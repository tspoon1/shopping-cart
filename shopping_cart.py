# shopping_cart.py
import os
from dotenv import load_dotenv
from datetime import datetime
#from pprint import pprint

load_dotenv()


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas","department": "produce", "aisle": "fruit", "price": 0.79, "price_per": "pound"}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

#adapted from prof-rossetti (intended for groceries exercise)
def to_usd(my_price):
    return f"${my_price:,.2f}"

#####################################################################
#  Initial message to the user  #
#####################################################################

print()
print("Hello! Welcome to Tim's Grocery Store!")
print()
print("-------------------------------------------")
print("The following items are available for purchase to today:")
print("-------------------------------------------")

shopping_list = []
shopping_list_price_adjuster = []
valid_ids = []

for p in products:

    #printing each product for each user to see
    print(" + " + str(p["id"]) + " " + p["name"] + " (" + to_usd(p["price"]) + ")")

    #gathering the vaid id values to use this for loop efficiently
    valid_ids.append(int(p["id"]))

print()
user_input = "" #using in order to not not copmare ints to strings when casting later on


####### Will execute until the user has inputted 'DONE' #######
print("Please type 'DONE' when you are ready to checkout!")
item_magnitude = 0

while user_input.upper() != "DONE":
    
    item_id = input("Please enter the product identifier number that you would like to purchase today: ")

    #will keep running until user enters valid id or DONE
    if item_id.upper() != "DONE":
        while int(item_id) not in valid_ids:
            item_id = input("I'm sorry! I don't think that product id is valid. Could you please try again? ")
            if item_id.upper() == "DONE":
                break

    #if the user entered DONE following a wrong id, this would break the loop
    if item_id.upper() != "DONE":
        shopping_list.append(int(item_id))

        #assigning magnitude to items
        for p in products:
            if int(item_id) == p["id"]:
                if p["price_per"] == "pound":
                    item_magnitude = input("Please specify the number of pounds: ")
                else:
                    item_magnitude = 1
                break
        
        shopping_list_price_adjuster.append(float(item_magnitude))



    user_input = item_id


####### Generating reciept output #######

# line 90 datetime formatting adapted from
# https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python

print("-------------------------------------------")
print("Tim's Grocery Store")
print("WWW.TimsGroceryStore.COM")
print("-------------------------------------------")
print("CHECKOUT AT: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
print("-------------------------------------------")
print("SELECTED PRODUCTS:")

checkout_list = []
for i in shopping_list:
    for p in products:
        if i == p["id"]:
            checkout_list.append(p)

subtotal = 0.0
for item, mag in zip(checkout_list, shopping_list_price_adjuster):
    if float(mag) == 1.0:
        print(" ... " + item["name"] + " (" + to_usd(item["price"]) + ")")
        subtotal = subtotal + float(item["price"])
    else:
        print(" ... " + item["name"] + " (" + to_usd(float(item["price"])*float(mag)) + ")")
        subtotal = subtotal + ( float(item["price"]) * float(mag) )

tax_rate_env = float(os.environ.get("TAX_RATE"))
tax = subtotal * tax_rate_env

print("-------------------------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(subtotal + tax))
print("-------------------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("-------------------------------------------")