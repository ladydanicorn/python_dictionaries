# Assignment 1

# Task 1

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 2.99, "Tea": 4.50}

restaurant_menu["Main Course"]["Steak"] = 17.99

removed_item = restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)