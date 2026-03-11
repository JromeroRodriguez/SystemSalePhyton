# funciones_ingresar.py 
from Fun_validations import validate_text, validate_number, validate_integer

def input_sale():
    product = validate_text("Enter product name: ")
    price = validate_number("Enter product price: ")
    quantity = validate_integer("Enter quantity sold: ")
    return (product, price, quantity)