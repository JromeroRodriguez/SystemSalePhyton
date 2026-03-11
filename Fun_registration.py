# funciones_registrar.py

from Fun_inputs import input_sale
from Fun_calculations import calculate_total
from Fun_validations import validate_integer

def register_sales():
    """
    Registers all sales of the day and returns:
    - sales list
    - grand total
    """
    sales = []
    grand_total = 0

    num_sales = validate_integer("How many sales do you want to register? ")

    for _ in range(num_sales):
        sale = input_sale()
        sales.append(sale)
        grand_total += calculate_total(sale)

    return sales, grand_total