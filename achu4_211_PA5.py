'''
---------------------------------------------------------------------------------
Name: Amanda Chu
Assignment: PA 5
Due Date: 11/06/2023
---------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by professor and class syllabus.
---------------------------------------------------------------------------------
Comments and Assumptions: A note to the grader as to any problems or
uncompleted aspects of the assignment, as well as any assumptions.
You can write in N/A if you don’t have any comments/assumptions.
---------------------------------------------------------------------------------
NOTE: width of source code should be <=80 characters to be readable on-screen.
12345678901234567890123456789012345678901234567890123456789012345678901234567890
        10       20         30        40        50        60        70        80
---------------------------------------------------------------------------------
'''

def update_inventory(inventory, restock=False): 
    # Put your function body here
    if restock == False: 
        return inventory
    for item in restock: 
        product_name = item[0]
        if product_name in inventory.keys():
            # if inventory already, update
            # product tags
            inventory_tags = inventory[product_name][0]
            count_aisles = inventory[product_name][1]
            weight = inventory_tags[-1]
            inventory_tags = inventory_tags[:-1]
            # adding the tags to update
            for tag in item[1]: 
                if len(str(tag)) != 0:
                    inventory_tags.append(tag)
            inventory_tags.append(weight)
            inventory[product_name][0] = inventory_tags

            # add to quantity 
            inventory_quant = inventory[product_name][1][0]
            restock_quant = item[2][0]
            inventory[product_name][1][0] = restock_quant + inventory_quant
            # add to aisle location
            restock_aisle = item[2][1]
            inventory_aisles = inventory[product_name][1][1]
            if len(restock_aisle) != 0:
                inventory_aisles = inventory_aisles + ' ' + restock_aisle
            inventory[product_name][1][1] = inventory_aisles

        else: 
            # product name: [[tags, weight], [count, aisle]]
            inventory[product_name] = item[1:]
    
    return inventory

def merge_inventory (inventory, new_inventory=False):  
    # convert dict form to list format
    # pass into update_inventory(inventory, restock)
    # list to dict 
    dict_inventory = {}
    for item in inventory:
        prod_name = item[0]
        dict_inventory[prod_name] = [item[1], item[2]]

    # dict to list
    if new_inventory:
        my_restock = []
        # Iterates through new_inventory to append key and value to mini list
        for k, v in new_inventory.items():
            mini_list = []    
            mini_list.append(k) # Product name
            mini_list.append(v[0]) # Tags
            mini_list.append(v[1]) # Weight and store aisle
            my_restock.append(mini_list)
        dict_inventory = update_inventory(dict_inventory, my_restock)
    return dict_inventory

def products_info (products, products_detail, new_products_detail=False):  
    # Put your function body here
    # merge products into this form . list of list
    inventory = []
    for i in range(len(products)):
        product_name = products[i]
        product_tags = products_detail[i][0]
        product_aisles = products_detail[i][1]
        mini_list = [product_name, product_tags, product_aisles]
        inventory.append(mini_list)

    # merge new details or updates into form dictionary 
    if new_products_detail:
        new_inventory = {}
        # Iterating through products to extract the name, tags, and aisle
        # Then append to mini list
        for i in range(len(products)):
            if len(new_products_detail[i]) != 0:
                product_name = products[i]
                product_tags = new_products_detail[i][0]
                product_aisles = new_products_detail[i][1]
                mini_list = [product_tags, product_aisles]
                new_inventory[product_name] = mini_list
        inventory = merge_inventory(inventory, new_inventory)
    else:
        inventory = {}
        for i in range(len(products)):
            if len(products_detail[i]) != 0:
                product_name = products[i]
                product_tags = products_detail[i][0]
                product_aisles = products_detail[i][1]
                mini_list = [product_tags, product_aisles]
                inventory[product_name] = mini_list
    return(inventory)
 
def digits_summation (n):
    # Put your function body here
    if n < 10:  # Checks for a single digit
        return n  # Print number if it is a single digit
    else:  
    # Otherwise Just print the number divided by 10 plus floor dividing by 10
        total = n % 10 + digits_summation(n // 10)
    return total

def vowel_counts (some_str, result=None):
    # Initialize the result dictionary if not provided
    if result is None: # If result is not provided
        result = {} # Initialize the result dictionary
    vowels = set("aeiouAEIOU") # Initialize the vowels lower and capital 
    if len(some_str) == 0: 
    # Check if the length of the string is equal to zero, a.k.a. empty 
        return result # Return result
    char = some_str[0] 
    # Initialize a variable to check the first letter of the string
    # Check if the character is a vowel (either lowercase or uppercase)
    if char in vowels:
        if char in result.keys(): 
        # Checks if the letter is already in the dictionary
            result[char] = result[char] + 1 # Have the value added to one
        else: 
        # Otherwise add the letter to the dictionary, and have the value equal to one
            result[char] = 1
    # Recursively call the function with the remaining characters in the string
    return vowel_counts(some_str[1:], result)