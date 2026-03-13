# Registration functions - manages the main sales flow

from Fun_inputs import input_sale
from Fun_calculations import calculate_total

def register_sales():
    sales_dict = {}   # empty dictionary to group sales by product name
    grand_total = 0   # accumulator that adds up the total of each sale
    continuar = "yes" # variable that controls the main loop

    while continuar == "yes":  # keeps registering while the user wants to continue
        sale = input_sale()    # captures and validates sale data
        product_name = sale["product"]  # extracts product name from dictionary
        
        if product_name in sales_dict:  # if product already exists in dictionary
            sales_dict[product_name]["quantity"] += sale["quantity"]  # adds new quantity to existing
        else:
            sales_dict[product_name] = sale  # if not exists, adds as new product
            
        grand_total += calculate_total(sale)  # adds this sale total to accumulator

        # inner loop validates that response is exactly "yes" or "no"
        continuar = input("Do you want to register another sale? (yes/no): ").strip().lower()
        while continuar != "yes" and continuar != "no":
            print("Error: Please enter 'yes' or 'no'.")
            continuar = input("Do you want to register another sale? (yes/no): ").strip().lower()

    # converts dictionary to list to iterate with for in display module
    # returns both values as implicit tuple to avoid creating two separate functions
    return list(sales_dict.values()), grand_total