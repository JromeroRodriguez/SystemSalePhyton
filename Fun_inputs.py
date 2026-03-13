# Input functions - separated because capturing data is a different responsibility than registering it

from Fun_validations import validate_text, validate_number

def input_sale():
    product = validate_text("Enter product name: ")           # validates text only, no numbers or symbols
    price = validate_number("Enter product price: ", float)   # validates decimal number greater than zero
    quantity = validate_number("Enter quantity sold: ", int)  # validates integer greater than zero
    
    # builds a dictionary to access data by name instead of by position
    return {
        "product": product,   # key "product" stores the product name
        "price": price,       # key "price" stores the unit price
        "quantity": quantity  # key "quantity" stores the quantity sold
    }